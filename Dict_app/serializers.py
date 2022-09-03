from dataclasses import fields
from rest_framework import serializers
from Dict_app.models import WordMeaning


class WordMeaningSerializer(serializers.ModelSerializer):
     class Meta:
         model = WordMeaning
         fields = "__all__"



