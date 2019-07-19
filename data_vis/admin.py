from django.contrib import admin
from data_vis.models import DataVis, DataVisFigure

# Register your models here.

# class SeoKeywordInLine(admin.TabularInline):
#     model = SeoKeyword


class DataVisFigureInLine(admin.TabularInline):
    model = DataVisFigure


class DataVisAdmin(admin.ModelAdmin):
    #fieldsets = []
    inlines = [DataVisFigureInLine]


#admin.site.unregister(DataVis)
admin.site.register(DataVis, DataVisAdmin)