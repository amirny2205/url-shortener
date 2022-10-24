from django.db import models

class LinkModel(models.Model):
    shortened = models.CharField(max_length=200, primary_key=True)
    redirect_to = models.CharField(max_length=200)