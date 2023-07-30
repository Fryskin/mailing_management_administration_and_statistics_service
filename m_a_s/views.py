from django.shortcuts import render
from django.views.generic import ListView

from m_a_s.models import ClientOfService, Newsletter


class ClientOfServiceListView(ListView):
    model = ClientOfService


class NewsletterListView(ListView):
    model = Newsletter

