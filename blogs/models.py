from django.conf import settings
from django.db import models

from m_a_s.models import NULLABLE


class Blog(models.Model):
    """Blog model for promotion the service."""
    title = models.CharField(max_length=1000, verbose_name='title')
    content = models.TextField(max_length=5000, verbose_name='content')
    preview = models.ImageField(upload_to='blogs/', verbose_name='preview', **NULLABLE)
    count_of_views = models.PositiveIntegerField(default=0, verbose_name='count of views', editable=False)
    date_of_publish = models.DateField(auto_now_add=True, verbose_name='date of creation')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='owner')

    def get_title(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
        ordering = ('title',)
