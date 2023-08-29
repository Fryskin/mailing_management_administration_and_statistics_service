from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview', 'count_of_views', 'date_of_publish',)
    list_filter = ('title', 'count_of_views', 'date_of_publish',)

