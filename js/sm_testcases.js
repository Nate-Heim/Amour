//Nate Heim

// TEST CASES
function testSurveyMatcher() {
    const surveys1 = [
        [1, 2, 3],
        [1, 2, 3], // Identical to survey 0
        [4, 5, 6],
        [1, 2, 4], // Partial overlap with survey 0
    ];

    const surveys2 = [
        [10, 20, 30],
        [40, 50, 60], // Completely disjoint
    ];

    const surveysEmpty = [];

    console.log("Test 1: Identical surveys");
    console.log(SurveyMatcher.matchSurveys(surveys1));

    console.log("\nTest 2: Completely disjoint surveys");
    console.log(SurveyMatcher.matchSurveys(surveys2));

    console.log("\nTest 3: Empty surveys");
    console.log(SurveyMatcher.matchSurveys(surveysEmpty));

    console.log("\nTest 4: Partial overlap");
    const matches = SurveyMatcher.matchSurveys(surveys1);
    console.log(matches);
}

testSurveyMatcher();
