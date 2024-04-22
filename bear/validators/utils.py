from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from ..models import Player


def valid_age(date_birth, age_min):
    today = datetime.now().date()
    age = today.year - date_birth.year - ((today.month, today.day) < (date_birth.month, date_birth.day))
    if age > age_min:
        return True

def document_exist(model_class, field_name, field_value):
    if model_class.objects.filter(**{field_name: field_value}).exists():
        return True