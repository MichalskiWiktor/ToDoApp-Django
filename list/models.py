from django.db import models

# Create your models here.
class ListItem(models.Model):
    text = models.TextField(max_length=200)
    deadline = models.DateField(null = True, blank = True)
    status = models.BooleanField(null = True)

    def __str__(self):
        return self.text