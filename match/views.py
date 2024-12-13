#match/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .utils import calculate_match_percentage 

User = get_user_model()

@login_required
def find_matches(request):
    current_user = request.user
    all_users = User.objects.exclude(id=current_user.id)  # Exclude the current user

    # Calculate match percentage for each user
    matches = []
    for user in all_users:
        match_percentage = calculate_match_percentage(current_user, user)
        if match_percentage >= 60:  # Threshold for match
            matches.append({
                'user': user,
                'match_percentage': match_percentage,
            })

    return render(request, 'match_list.html', {'matches': matches})