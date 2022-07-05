from django.db import models
import os
from datetime import datetime

def convert_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{:%Y-%m-%d-%H-%M-%S-%f}.{}'.format(datetime.now(), ext)
    return os.path.join('./uploads', filename)

class News(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.FileField(upload_to=convert_file_name)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'


