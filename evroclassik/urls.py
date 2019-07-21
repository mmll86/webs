from django.urls import path, re_path
from . import views

app_name = 'evroclassik'

urlpatterns = [
	path('', views.index, name='index'),
	path('catalogs/', views.catalogs, name='catalogs'),
    re_path('catalogs/(?P<catalog_id>\d+)/', views.catalog, name='catalog'),

	path('catalogs_plumbing/', views.catalogs_plumbing, name='catalogs_plumbing'),
    re_path('catalogs_plumbing/(?P<plumbing_id>\d+)/', views.plumbing, name='plumbing'),
]
