from django import forms
from .models import SurveyQuestion

class SurveyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', None)
        super().__init__(*args, **kwargs)

        if questions:
            for question in questions:
                field_name = f"question_{question.id}"
                field_label = question.question_text

                if question.question_type == 'text':
                    self.fields[field_name] = forms.CharField(
                        label=field_label,
                        required=True,
                        widget=forms.TextInput(attrs={
                            'class': 'input',
                            'placeholder': 'Enter your answer...'
                        })
                    )
                elif question.question_type == 'boolean':
                    self.fields[field_name] = forms.ChoiceField(
                        label=field_label,
                        required=True,
                        choices=[(True, 'Yes'), (False, 'No')],
                        widget=forms.RadioSelect(attrs={'class': 'radio'})
                    )
                elif question.question_type == 'choice':
                    self.fields[field_name] = forms.ChoiceField(
                        label=field_label,
                        required=True,
                        choices=[(option, option) for option in question.options],
                        widget=forms.Select(attrs={'class': 'select'})
                    )