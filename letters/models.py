from django.db import models

class Letter(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Letter #{}' .format(self.id)