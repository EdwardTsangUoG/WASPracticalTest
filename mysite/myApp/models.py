from django.db import models
from django.utils.timezone import now

class newsArticle(models.Model):
    article_heading = models.CharField(max_length=200)
    article_text = models.CharField(max_length=1024)
    pub_date = models.DateTimeField('date published', default=now)

# Create your models here.
