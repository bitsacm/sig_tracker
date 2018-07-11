from django.db import models

class dev(models.Model):
    topic = models.CharField(max_length=2000)
    summary = models.TextField(blank =True)
    contact = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add =True)
# include feedback

    def __str__(self):
        return self.topic
    