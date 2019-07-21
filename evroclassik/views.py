from django.shortcuts import render
from .models import Catalog, Furniture


def index(request):
	return render(request, "evroclassik/index.html")


def catalogs(request):
	catalogs = Catalog.objects.order_by('date_added')
	context = {'catalogs': catalogs}
	return render(request, 'evroclassik/catalogs.html', context)


def catalog(request, catalog_id):
	catalog = Catalog.objects.get(id=catalog_id)
	furnitures = catalog.furniture_set.order_by('-date_added')
	context = {'catalog': catalog, 'furnitures': furnitures}
	return render(request, 'evroclassik/catalog.html', context)
