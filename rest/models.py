from django.db import models

class WordStatistic(models.Model):
    word_of_intrest = models.TextField(primary_key=True)
    occurance_count = models.IntegerField()

    class Meta:
        ordering = ['-occurance_count']
