from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    task_title = models.CharField(max_length=1000)
    task_author = models.ForeignKey(User, on_delete=models.CASCADE)
    task_date = models.DateField()
    add_at = models.DateTimeField(blank=True)
    task_time = models.TimeField(blank=True, null=True)
    task_priority = models.BooleanField(default=False)
    task_deleted = models.BooleanField(default=False)
    task_trash = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task_title}'

    def get_absolute_url(self):
        return f'/main/{self.id}'


class Note(models.Model):
    note_title = models.CharField(max_length=250)
    note_text = models.TextField()
    note_date = models.DateField(blank=True, null=True)
    add_at = models.DateTimeField(blank=True)
    note_author = models.ForeignKey(User, on_delete=models.CASCADE)
    note_trash = models.BooleanField(default=False)
    note_file = models.FileField(null=True, blank=True, upload_to='documents')
    note_pin = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.note_title}'

    def get_absolute_url(self):
        return f'/main/{self.id}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='/avatars/Noted_avatar.png', upload_to='avatars')
    name = models.CharField(max_length=20, default='Username')

    def __str__(self):
        return self.user.username







