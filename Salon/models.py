from django.db import models


# Create your models here.

class Cars(models.Model):
    brand = models.CharField(max_length=100, verbose_name='Brand of car')
    model = models.CharField(max_length=200, verbose_name='Model of car')
    image = models.ImageField(upload_to='car_main_photo/', null=True, blank=True, verbose_name="Car's main photo")
    description = models.TextField(verbose_name='Description')
    price = models.FloatField(verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creating')
    slug = models.SlugField(unique=True, null=True)
    color = models.CharField(max_length=30, verbose_name='Color')
    engine = models.CharField(max_length=30, verbose_name='Engine')
    quantity = models.IntegerField(verbose_name='Quantity of cars')

    def __str__(self):
        return f'{self.brand}: {self.model}'

    def get_car_photo(self):
        try:
            return self.image.url
        except:
            return 'https://lh3.googleusercontent.com/proxy/MkIVno1PBYcVTf88nGoaXGqqzTP4N9rXVfXkQyw30kBOxfYFpAd-stsbsPIanKQR2kYHLpBWU_od2RIShvism-1kDA9W1HYCo8W3uODRthB9HLFz_YkYZ-WzUKNztkLcjap1qSw0ikNWy3HuRGQwxQ'

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Gallery(models.Model):
    image = models.ImageField(upload_to='cars/', verbose_name='Photos of cars')
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
