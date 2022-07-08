from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError


class ImageSizeValidation:

    def __call__(self, image):
        file_size = image.file.size
        limit_kb = 150
        if file_size > limit_kb * 1024:
            raise ValidationError("Max size of file %s KB" % limit_kb)
