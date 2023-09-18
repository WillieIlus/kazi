from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

from locations.models import County
User = settings.AUTH_USER_MODEL


class Company(models.Model):
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255, unique=True, blank=True)
    description = models.TextField(_('description'), blank=True)
    county = models.ForeignKey(County, verbose_name=_('county'), blank=True, null=True, related_name='companies', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_('user'), blank=True, null=True, related_name='companies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    is_active = models.BooleanField(_('is active'), default=True)
    address = models.CharField(_('address'), max_length=255, blank=True)
    phone = models.CharField(_('phone'), max_length=255, blank=True)
    email = models.EmailField(_('email'), max_length=255, blank=True)
    website = models.URLField(_('website'), max_length=255, blank=True)
    logo = models.ImageField(_('logo'), upload_to='companies/logos', blank=True)
    cover = models.ImageField(_('cover'), upload_to='companies/covers', blank=True)

    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companies')
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('companies:company_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Company, self).save(*args, **kwargs)

    def get_logo_url(self):
        if self.logo:
            return self.logo.url
        return '/static/images/default-company-logo.png'


