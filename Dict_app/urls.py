from django.urls import path
from Dict_app.views import WordMeaningAPIView


urlpatterns =[
    path("all_words/", view= WordMeaningAPIView.as_view()),
  

]
