from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Task(models.Model):
    task_title = models.CharField(max_length=1000)
    task_author = models.ForeignKey(User, on_delete=models.CASCADE)
    task_time = models.DateField()
    add_at = models.DateTimeField(blank=True)
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
    add_at = models.DateTimeField(blank=True)
    note_author = models.ForeignKey(User, on_delete=models.CASCADE)
    note_trash = models.BooleanField(default=False)
    note_file = models.FileField(null=True, blank=True, upload_to='documents')

    def __str__(self):
        return f'{self.note_title}'

    def get_absolute_url(self):
        return f'/main/{self.id}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='/avatars/user_male_circle_icon.svg',
                               upload_to='avatars')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)



