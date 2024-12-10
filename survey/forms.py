from django import forms
from .models import SurveyQuestion

class SurveyForm(forms.ModelForm):
    class Meta:
        model = SurveyQuestion
        fields = ['question_text', 'question_type', 'options']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if field.model_field.name == 'question_type' and field.initial == 'boolean':
                field.widget = forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')])