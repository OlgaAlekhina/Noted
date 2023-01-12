from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Note(models.Model):

    LOW = 0
    NORMAL = 1
    HIGH = 2
    PRIORITIES = [
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
    ]
    note_title = models.CharField(max_length=250)
    note_text = models.TextField()
    note_priority = models.IntegerField(max_length=1, choices=PRIORITIES, default=0)
    note_time = models.DateField(auto_now=True)
    note_author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.note_title}'



