from django.db import models
from django.urls import reverse

from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    slug = models.SlugField(_('slug'), max_length=255, unique=True, blank=True)
    code = models.CharField(_('code'), max_length=2, unique=True)
    flag = models.ImageField(_('flag'), upload_to='countries/flags/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('locations:country_detail', kwargs={'slug': self.slug})


class County(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    country = models.ForeignKey(Country, related_name='states', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Counties"
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(County, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('locations:detail', kwargs={'slug': self.slug})

