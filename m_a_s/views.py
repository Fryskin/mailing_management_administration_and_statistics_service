from django.shortcuts import render
from django.views.generic import ListView, DetailView

from m_a_s.models import ClientOfService, Newsletter


class ClientOfServiceListView(ListView):
    model = ClientOfService


class ClientOfServiceDetailView(DetailView):
    model = ClientOfService


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(DetailView):
    model = Newsletter



