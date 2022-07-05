from django.db import models

class News(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.FileField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'

    
