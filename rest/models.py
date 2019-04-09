from django.db import models

class Author(models.Model):
    url = models.TextField(primary_key=True)
    full_name = models.TextField()

class StatsVersion(models.Model):
    version_number = models.AutoField(primary_key=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    ready = models.BooleanField(default=False)

class Word(models.Model):
    word_of_interest = models.TextField(primary_key=True)

class AuthorStatistic(models.Model):
    occurance_count = models.IntegerField()
    word = models.ForeignKey('Word', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    version = models.ForeignKey('StatsVersion', on_delete=models.CASCADE)

    class Meta:
        ordering = ['author','-occurance_count']

class GloballStatistic(models.Model):
    occurance_count = models.IntegerField()
    word = models.ForeignKey('Word', on_delete=models.CASCADE)
    version = models.ForeignKey('StatsVersion', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-occurance_count']
