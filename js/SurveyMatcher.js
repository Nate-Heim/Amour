//Nate Heim

//To call use the SurveyMatcher.matchSurveys(surveys) function with an array of surveys as input. 
//The function will return an array of objects, each containing the indices of the surveys that are considered similar based on the Jaccard 
//similarity threshold of 0.75. This will probably be changed in the future
class SurveyMatcher {
    static NUM_HASH_FUNCTIONS = 100;
    static BANDS = 10;
    static ROWS_PER_BAND = SurveyMatcher.NUM_HASH_FUNCTIONS / SurveyMatcher.BANDS;

    static matchSurveys(surveys) {
        const hashBuckets = new Map();
        const candidatePairs = [];

        // Min-hashing
        const signatures = surveys.map(survey =>
            Array.from({ length: SurveyMatcher.NUM_HASH_FUNCTIONS }, (_, j) =>
                SurveyMatcher.minHash(survey, j)
            )
        );

        // LSH
        signatures.forEach((signature, i) => {
            for (let b = 0; b < SurveyMatcher.BANDS; b++) {
                const hashValue = SurveyMatcher.hashBand(signature, b);
                if (!hashBuckets.has(hashValue)) {
                    hashBuckets.set(hashValue, []);
                }
                hashBuckets.get(hashValue).push(i);
            }
        });

        // Candidate Pairs and Similarity Calculation
        for (const bucket of hashBuckets.values()) {
            for (let i = 0; i < bucket.length; i++) {
                for (let j = i + 1; j < bucket.length; j++) {
                    const survey1 = bucket[i];
                    const survey2 = bucket[j];
                    const similarity = SurveyMatcher.jaccardSimilarity(
                        surveys[survey1],
                        surveys[survey2]
                    );
                    if (similarity >= 0.75) {
                        candidatePairs.push({ first: survey1, second: survey2 });
                    }
                }
            }
        }
        return candidatePairs;
    }

    static minHash(survey, hashFunction) {
        let minHashValue = Infinity;
        survey.forEach(bitIndex => {
            const hashedValue = SurveyMatcher.hash(bitIndex, hashFunction);
            minHashValue = Math.min(minHashValue, hashedValue);
        });
        return minHashValue;
    }

    static hash(value, hashFunction) {
        // Example hash function
        return value % (2 ** (hashFunction + 1));
    }

    static hashBand(signature, bandIndex) {
        let hashValue = 0;
        for (
            let i = bandIndex * SurveyMatcher.ROWS_PER_BAND;
            i < (bandIndex + 1) * SurveyMatcher.ROWS_PER_BAND;
            i++
        ) {
            hashValue = hashValue * 31 + signature[i];
        }
        return hashValue;
    }

    static jaccardSimilarity(set1, set2) {
        const intersection = set1.filter(value => set2.includes(value)).length;
        const union = new Set([...set1, ...set2]).size;
        return intersection / union;
    }
}

// Example usage:
const surveys = [
    [1, 3, 5], // Survey represented as arrays of "bit" indices
    [2, 3, 5],
    [1, 4, 6]
];

const matches = SurveyMatcher.matchSurveys(surveys);
console.log("Matched Surveys:", matches);