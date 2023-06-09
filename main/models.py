from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from users.models import CustomUser
import datetime

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


class Doacao(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(
        max_length=200, choices=VOLUME, default="small")
    endereco = models.CharField(
        max_length=200, null=False, blank=False, default="")
    doacao_slug = models.SlugField(
        "Doacao Slug", null=False, blank=False, unique=True)
    published = models.DateTimeField("Date published", default=timezone.now())
    retirada = models.DateField(
        "Data de retirada", default=datetime.date.today() + datetime.timedelta(days=1))
    author = models.ForeignKey(
        get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    series = models.ForeignKey(
        DoacaoSeries, default="", verbose_name="Series", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Doacao.objects.filter(doacao_slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.doacao_slug:
            self.doacao_slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    @property
    def slug(self):
        return self.series.slug + "/" + self.doacao_slug

    class Meta:
        verbose_name_plural = "Doacao"
        ordering = ['title', '-published']
