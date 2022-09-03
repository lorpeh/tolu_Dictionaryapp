
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from Dict_app.models import WordMeaning
from Dict_app.serializers import WordMeaningSerializer

class WordMeaningAPIView(APIView):
    def get(self, request):
        all_words = WordMeaning.objects.all()
        serializer = WordMeaningSerializer(all_words, many= True)
        return Response(serializer.data)




# Create your views here.
