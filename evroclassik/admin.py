from django.contrib import admin

from evroclassik.models import Catalog, Furniture, CatalogPlumbing, Plumbing, HeadSlider, Slider, InfoCompany
admin.site.register(Catalog)

class FurnitureAdmin(admin.ModelAdmin):
	list_display =('name', 'name_furniture', 'price', 'date_added')
	list_display_links = ('name', 'name_furniture')
	search_fields = ('name', 'name_furniture')

admin.site.register(Furniture, FurnitureAdmin)

admin.site.register(CatalogPlumbing)

class PlumbingAdmin(admin.ModelAdmin):
	list_display =('name', 'name_plumbing', 'price', 'date_added')
	list_display_links = ('name', 'name_plumbing')
	search_fields = ('name', 'name_plumbing')

admin.site.register(Plumbing, PlumbingAdmin)

admin.site.register(HeadSlider)
admin.site.register(Slider)
admin.site.register(InfoCompany)

