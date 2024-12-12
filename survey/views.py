from django.shortcuts import render, redirect
from .models import SurveyQuestion, UserResponse
from .forms import SurveyForm

def survey_thank_you(request):
    return render(request, 'survey_thank_you.html')

def take_survey(request):
    # Check if the user has already taken the survey
    if UserResponse.objects.filter(user=request.user).exists():
        return redirect('survey-thank-you')

    # Load survey questions from the database
    questions = SurveyQuestion.objects.all()

    if request.method == 'POST':
        # Create a form with the submitted data
        form = SurveyForm(request.POST, questions=questions)
        if form.is_valid():
            # Process the form and save responses
            for field, value in form.cleaned_data.items():
                question_id = int(field.split('_')[1])  # Extract question ID from field name
                question = SurveyQuestion.objects.get(id=question_id)
                UserResponse.objects.create(user=request.user, question=question, response=value)
            return redirect('survey-thank-you')  # Redirect to thank-you page
    else:
        # Create an empty form with questions
        form = SurveyForm(questions=questions)

    return render(request, 'survey_form.html', {'form': form})