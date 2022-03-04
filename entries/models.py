from cgitb import text
from django.db import models
from .models import Entry
class  Entry(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'entry #{}' .format(self.id)

    class meta:
        verbose_name_plural ='entries'