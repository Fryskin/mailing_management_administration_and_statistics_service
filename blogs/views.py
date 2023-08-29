from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from blogs.forms import BlogForm
from blogs.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blogs:blog_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blogs:blog_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()

        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()

        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blogs:blog_list")


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):

        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save(update_fields=['count_of_views'])
        return self.object


