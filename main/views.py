from django.shortcuts import render
from django.http import HttpResponse
from .models import Doacao, DoacaoSeries


# Create your views here.


def homepage(request):
    matching_series = DoacaoSeries.objects.all()

    return render(request=request, template_name='main/home.html', context={"objects": matching_series})


def series(request, series: str):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            matching_series = Doacao.objects.filter(series__slug=series).all()
        else:
            matching_series = Doacao.objects.filter(
                series__slug=series, author=request.user).all()
    else:
        matching_series = None

    return render(request=request, template_name='main/home.html', context={"objects": matching_series})


def doacao(request, series: str, doacao: str):
    matching_doacao = Doacao.objects.filter(
        series__slug=series, doacao_slug=doacao).first()

    return render(request=request, template_name='main/doacao.html', context={"object": matching_doacao})
