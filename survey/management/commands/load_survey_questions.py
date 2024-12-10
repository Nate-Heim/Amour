import logging

from django.core.management.base import BaseCommand
from ...models import SurveyQuestion  # Assuming your model is in survey/models.py
import json

logger = logging.getLogger(__name__)  # Get logger for this module


class Command(BaseCommand):
    help = 'Load survey questions from JSON file'

    def handle(self, *args, **options):
        try:
            with open('survey_questions.json') as f:
                questions_data = json.load(f)
                logger.info("Successfully opened JSON file")

                for question in questions_data:
                    SurveyQuestion.objects.create(
                        question_text=question['question'],
                        question_type=question['type'],
                        options=question.get('options', ''),
                    )
                logger.info(f"Successfully loaded {len(questions_data)} survey questions")

        except FileNotFoundError as e:
            logger.error(f"Error loading JSON file: {str(e)}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")