from django.db import models

class WebApp(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='Web_pics')

    def __str__(self):
        return f'{self.image} picture'
