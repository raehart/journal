from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Entry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return "{}: {}".format(self.created, self.title)
