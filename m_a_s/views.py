import os
import random

from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from blogs.models import Blog
from m_a_s.forms import ClientForm, NewsletterForm, MessageForm

from m_a_s.models import ClientOfService, Newsletter, Message


class ClientOfServiceListView(ListView):
    model = ClientOfService

    def get_queryset(self, *args, **kwargs):

        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_relevant=True)
        return queryset


class ClientOfServiceDetailView(DetailView):
    model = ClientOfService

    def cache_create(self):

        if settings.CACHE_ENABLED:
            key = f'client_of_service_list_{self.object.pk}'
            client_of_service_list = cache.get(key)
            if client_of_service_list is None:
                client_of_service_list = ClientOfService.objects.all()
                cache.set(key, client_of_service_list)
        else:
            client_of_service_list = ClientOfService.objects.all()

        return client_of_service_list


class ClientOfServiceCreateView(CreateView):
    model = ClientOfService
    success_url = reverse_lazy('mas:m_a_s_list')
    form_class = ClientForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()

        return super().form_valid(form)


class ClientOfServiceUpdateView(UpdateView):
    model = ClientOfService
    success_url = reverse_lazy('mas:m_a_s_list')
    form_class = ClientForm


class ClientOfServiceDeleteView(DeleteView):
    model = ClientOfService
    success_url = reverse_lazy("mas:m_a_s_list")


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterCreateView(CreateView):
    model = Newsletter
    success_url = reverse_lazy('mas:newsletters_list')
    form_class = NewsletterForm

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        context_data = self.get_context_data()

        formset = context_data['formset']
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        newsletter_formset = inlineformset_factory(Newsletter, Message, form=MessageForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = newsletter_formset(self.request.POST)
        else:
            context_data['formset'] = newsletter_formset()
        return context_data


class NewsletterDetailView(DetailView):
    model = Newsletter

    def cache_create(self):

        if settings.CACHE_ENABLED:
            key = f'newsletters_list_{self.object.pk}'
            newsletters_list = cache.get(key)
            if newsletters_list is None:
                newsletters_list = Newsletter.objects.all()
                cache.set(key, newsletters_list)
        else:
            newsletters_list = Newsletter.objects.all()

        return newsletters_list


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    success_url = reverse_lazy('mas:newsletters_list')
    form_class = NewsletterForm

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']

        if form.is_valid():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        newsletter_formset = inlineformset_factory(Newsletter, Message, form=MessageForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = newsletter_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = newsletter_formset(instance=self.object)
        return context_data

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)

        return self.object


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy("mas:newsletters_list")


class MessageDetailView(DetailView):
    model = Message


class StatView(TemplateView):
    template_name = 'm_a_s/stat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_of_newsletters'] = Newsletter.objects.count()
        context['count_of_active_newsletters'] = Newsletter.objects.filter(newsletter_status='launched').count()
        context['unique_clients_count'] = ClientOfService.objects.count()

        blogs_count = Blog.objects.count()
        random_pk_1 = random.randint(0, int(blogs_count)-1)
        random_pk_2 = random.randint(0, int(blogs_count) - 1)
        random_pk_3 = random.randint(0, int(blogs_count) - 1)

        blog_1 = Blog.objects.all()[random_pk_1]
        context['random_blog_1'] = blog_1
        blog_2 = Blog.objects.all()[random_pk_2]
        context['random_blog_2'] = blog_2
        blog_3 = Blog.objects.all()[random_pk_3]
        context['random_blog_3'] = blog_3

        return context


def start_mailing(request):
    os.system('python manage.py jobs')

    return redirect(reverse('m_a_s:main_page'))
