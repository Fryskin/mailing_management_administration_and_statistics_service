from django.contrib import admin

from m_a_s.models import Newsletter, ClientOfService, Message, NewsletterLogs


@admin.register(ClientOfService)
class ClientOfServiceAdmin(admin.ModelAdmin):
    list_display = ('last_first_middle_name', 'contact_email', 'comment',)
    list_filter = ('last_first_middle_name',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('newsletter_status', 'time_of_sending_the_newsletter', 'interval',)
    list_filter = ('newsletter_status', 'time_of_sending_the_newsletter',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message_title', 'message_content',)
    list_filter = ('message_title',)


@admin.register(NewsletterLogs)
class NewsletterLogsAdmin(admin.ModelAdmin):
    list_display = ('datatime_of_last_try', 'status_of_try', 'response_of_mail_server',)
    list_filter = ('status_of_try',)
