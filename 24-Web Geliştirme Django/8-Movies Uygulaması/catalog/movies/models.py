from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=50, verbose_name="Film Adi")
    description = models.TextField(
    max_length=200, verbose_name="Film Açiklamasi")
    image = models.CharField(max_length=50, verbose_name="Image")
    created_date = models.DateTimeField(auto_now_add=True)
    isPublished = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.name
    def get_image_path(self):
        return '/img/' + self.image
