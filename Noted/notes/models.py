from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    task_title = models.CharField(max_length=1000)
    task_author = models.ForeignKey(User, on_delete=models.CASCADE)
    task_time = models.DateField()
    task_priority = models.BooleanField()

    def __str__(self):
        return f'{self.task_title}'

    def get_absolute_url(self):
        return f'/main/{self.id}'


class Note(models.Model):
    note_title = models.CharField(max_length=250)
    note_text = models.TextField()
    note_time = note_time = models.DateField(blank=True)
    note_author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.note_title}'

    def get_absolute_url(self):
        return f'/main/{self.id}'



