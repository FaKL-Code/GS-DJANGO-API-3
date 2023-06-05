from django.contrib import admin
from .models import Doacao, DoacaoSeries


class DoacaoSeriesAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'subtitle',
        'slug',
        'author',
    ]


class DoacaoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {"fields": [
         'title', 'subtitle', 'doacao_slug', 'series', 'author', 'endereco']}),
        ("Date", {"fields": ['modified']}),
    ]


# Register your models here.
admin.site.register(Doacao, DoacaoAdmin)
admin.site.register(DoacaoSeries, DoacaoSeriesAdmin)
