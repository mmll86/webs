from django.contrib import admin

from evroclassik.models import Catalog, Furniture, CatalogPlumbing, Plumbing
admin.site.register(Catalog)
admin.site.register(Furniture)
admin.site.register(CatalogPlumbing)
admin.site.register(Plumbing)

