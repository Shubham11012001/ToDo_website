from django.db import models


# Create your models here.
class TodoModels(models.Model):
    complete = models.BooleanField(default=False)
    task = models.CharField(max_length=60)

    def __str__(self):
        return self.task
