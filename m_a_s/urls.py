from django.urls import path

from m_a_s.apps import MasConfig
from m_a_s.views import ClientOfServiceListView, NewsletterListView, ClientOfServiceDetailView, NewsletterDetailView

app_name = MasConfig.name


urlpatterns = [
    path('', ClientOfServiceListView.as_view(), name='m_a_s_list'),
    path('newsletters', NewsletterListView.as_view(), name='newsletters_list'),
    path('client_details/<int:pk>/', ClientOfServiceDetailView.as_view(), name='client_details'),
    path('news_letter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_details')
]
