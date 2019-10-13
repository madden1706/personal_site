from django.contrib import admin
from data_vis.models import DataVis, DataVisFigure, DataVisInteractive

# Register your models here.

# class SeoKeywordInLine(admin.TabularInline):
#     model = SeoKeyword


class DataVisFigureInLine(admin.TabularInline):
    model = DataVisFigure


class DataVisAdmin(admin.ModelAdmin):
    #fieldsets = []
    inlines = [DataVisFigureInLine]

# class DataVisInteractiveAdmin(admin.ModelAdmin):
#     model



#admin.site.unregister(DataVis)
admin.site.register(DataVis, DataVisAdmin)
admin.site.register(DataVisInteractive)