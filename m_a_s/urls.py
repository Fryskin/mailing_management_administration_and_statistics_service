from django.urls import path
from django.views.decorators.cache import cache_page

from m_a_s.apps import MasConfig
from m_a_s.views import ClientOfServiceListView, NewsletterListView, ClientOfServiceDetailView, NewsletterDetailView, \
    MessageDetailView, StatView, ClientOfServiceCreateView, ClientOfServiceUpdateView, NewsletterUpdateView, \
    NewsletterCreateView, NewsletterDeleteView, ClientOfServiceDeleteView, start_mailing

app_name = MasConfig.name


urlpatterns = [
    path('', cache_page(60)(ClientOfServiceListView.as_view()), name='m_a_s_list'),
    path('client_details/<int:pk>/', ClientOfServiceDetailView.as_view(), name='client_details'),
    path('add_client', ClientOfServiceCreateView.as_view(), name='add_client'),
    path('edit_client/<int:pk>/', ClientOfServiceUpdateView.as_view(), name='edit_client'),
    path('delete_client/<int:pk>/', ClientOfServiceDeleteView.as_view(), name='delete_client'),

    path('newsletters',  cache_page(60)(NewsletterListView.as_view()), name='newsletters_list'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_details'),
    path('edit_newsletter/<int:pk>/', NewsletterUpdateView.as_view(), name='edit_newsletter'),
    path('add_newsletter', NewsletterCreateView.as_view(), name='add_newsletter'),
    path('delete_newsletter/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_newsletter'),

    path('message/<int:pk>/', cache_page(60)(MessageDetailView.as_view()), name='message_details'),

    path('main_page', StatView.as_view(), name='main_page'),
    path('main_page/send_page/', start_mailing, name='send_page')

]
