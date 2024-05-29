from django.db import models

class Phone(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField()
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, verbose_name=name)

