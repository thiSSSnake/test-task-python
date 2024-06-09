from django.db import models


class Ads(models.Model):
    title = models.CharField(max_length=300, blank=False)
    author = models.CharField(max_length=150, blank=False)
    views_count = models.IntegerField()
    position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
