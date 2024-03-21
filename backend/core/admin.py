from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'title')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('project', 'name')


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Skills, SkillAdmin)
admin.site.register(Projects, ProjectAdmin)