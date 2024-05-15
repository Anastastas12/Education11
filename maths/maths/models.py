from django.db import models

class MathTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    correct_answer = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
