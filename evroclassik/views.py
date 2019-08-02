from django.shortcuts import render
from .models import Catalog, CatalogPlumbing, HeadSlider, Slider, InfoCompany


# Главная страница сайта
def index(request):
    headslider = HeadSlider.objects.all()
    slider = Slider.objects.all()
    info_company = InfoCompany.objects.all()
    context = {'headslider': headslider, 'slider': slider, 'info_company': info_company}
    return render(request, "evroclassik/index.html", context)


# Каталог мебели
def catalogs(request):
    catalogs = Catalog.objects.order_by('date_added')
    context = {'catalogs': catalogs}
    return render(request, 'evroclassik/catalogs.html', context)


def catalog(request, catalog_id):
    catalog = Catalog.objects.get(id=catalog_id)
    furnitures = catalog.furniture_set.order_by('-date_added')
    context = {'catalog': catalog, 'furnitures': furnitures}
    return render(request, 'evroclassik/catalog.html', context)


# Каталог сантехники
def catalogs_plumbing(request):
    catalogs_plumbing = CatalogPlumbing.objects.order_by('date_added')
    context = {'catalogs_plumbing': catalogs_plumbing}
    return render(request, 'evroclassik/catalogs_plumbing.html', context)


def plumbing(request, plumbing_id):
    plumbing = CatalogPlumbing.objects.get(id=plumbing_id)
    plumbings = plumbing.plumbing_set.order_by('-date_added')
    context = {'plumbing': plumbing, 'plumbings': plumbings}
    return render(request, 'evroclassik/plumbing.html', context)

