from atexit import register
from django.contrib import admin
from Dict_app.models import WordMeaning

# admin.site.register(WORD)
# admin.site.register(MEANING)

@admin.register(WordMeaning)
class MeaningAdmin(admin.ModelAdmin):
    list_display = ["word", "origin", "definition", "synonyms", "antonyms"]

# Register your models here.
