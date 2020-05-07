from django.db import models


class Post(models.Model):
    post_name = models.CharField(max_length=256)
    post_text = models.TextField()
    post_image = models.ImageField()
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_name
