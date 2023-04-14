from django.db import models


class Task(models.Model):
    Name = models.CharField(
        max_length=50,
        null=False,
    )
    Description = models.TextField()


class Diet(models.Model):
    Name = models.CharField(max_length=25, null=False)
    Description = models.TextField()

