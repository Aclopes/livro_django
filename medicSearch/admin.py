from django.contrib import admin
from pkg_resources import empty_provider
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_at'
    list_display = ('user', 'role', 'birthday', 'specialitiesList')
    list_filter = ('user', 'user__is_active', 'role', 'birthday')
    list_display_links = ('user', 'role')
    empty_value_display = '-'
    exclude = ('favorites', 'updated_at')
    search_fields = ('user__username',)

    def specialitiesList(self, obj):
        return [i.name for i in obj.speciality.all()]
    
    class Media:
        css = {
            "all": ('css/custom.css',)
        }
        js = ("js/custom.js")


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)