from django.db import models


class WordMeaning(models.Model):
    word= models.CharField(max_length=100)
    part_of_speech = models.CharField(max_length=30)
    origin = models.CharField(max_length=100)
    definition = models.CharField(max_length=300)
    synonyms = models.CharField(max_length=200)
    antonyms = models.CharField(max_length=200)

    def __str__(self):
        return f"WORD: {self.word}  ORIGIN: {self.origin}"




