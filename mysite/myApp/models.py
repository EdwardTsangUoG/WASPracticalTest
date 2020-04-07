from django.db import models

class newsArticle(models.Model):
    article_heading = models.CharField(max_length=200)
    article_text = models.CharField(max_length=1024)
    pub_date = models.DateTimeField('date published')

# Create your models here.
