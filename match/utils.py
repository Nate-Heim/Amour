#match/utils.py

from survey.models import UserResponse
from django.db.models import Q

def calculate_match_percentage(user1, user2):
    # Fetch responses for both users
    user1_responses = UserResponse.objects.filter(user=user1)
    user2_responses = UserResponse.objects.filter(user=user2)

    if not user1_responses.exists() or not user2_responses.exists():
        return 0  # If either user has no responses, return 0% match

    # Convert responses to dictionaries for easier comparison
    user1_dict = {response.question.id: response.response for response in user1_responses}
    user2_dict = {response.question.id: response.response for response in user2_responses}

    # Find common questions
    common_questions = set(user1_dict.keys()).intersection(set(user2_dict.keys()))
    if not common_questions:
        return 0  # No common questions mean no match

    # Calculate matching answers
    matching_answers = sum(
        1 for qid in common_questions if user1_dict[qid] == user2_dict[qid]
    )
    total_questions = len(common_questions)

    # Return the percentage of matches
    return (matching_answers / total_questions) * 100
