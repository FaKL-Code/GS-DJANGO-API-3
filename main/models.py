from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model

VOLUME = (
    ('small', 'Small - Under 3Kg'),
    ('medium', 'Medium - Under 10Kg'),
    ('large', 'Large - Over 10Kg')
)


class DoacaoSeries(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    slug = models.SlugField(
        "Series Slug", null=False, blank=False, unique=True)
    published = models.DateTimeField("Date published", default=timezone.now())
    author = models.ForeignKey(
        get_user_model(), default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']

# Create your models here.


class Doacao(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(
        max_length=200, choices=VOLUME, default="small")
    endereco = models.CharField(
        max_length=200, null=False, blank=False, default="")
    doacao_slug = models.SlugField(
        "Doacao Slug", null=False, blank=False, unique=True)
    published = models.DateTimeField("Date published", default=timezone.now())
    modified = models.DateTimeField("Date modified", default=timezone.now())
    author = models.ForeignKey(
        get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    series = models.ForeignKey(
        DoacaoSeries, default="", verbose_name="Series", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.series.slug + "/" + self.doacao_slug

    class Meta:
        verbose_name_plural = "Doacao"
        ordering = ['title', '-published']
