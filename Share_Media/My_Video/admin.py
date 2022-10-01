from django.contrib import admin
from  embed_video.admin  import  AdminVideoMixin
from .models  import  Collection
#Register your models here.


class  CollectionAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Collection, CollectionAdmin)
