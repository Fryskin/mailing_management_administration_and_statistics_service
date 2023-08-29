from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Newsletter(models.Model):
    """Newsletter model for mailing."""
    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    INTERVAL_CHOICES = [
        (DAILY, 'DAILY'),
        (WEEKLY, 'WEEKLY')
    ]

    COMPLETED = 'completed'
    CREATED = 'created'
    LAUNCHED = 'launched'
    STATUS_CHOICES = [
        (COMPLETED, 'completed'),
        (CREATED, 'created'),
        (LAUNCHED, 'launched')
    ]
    newsletter_title = models.CharField(max_length=100, verbose_name='title', **NULLABLE)
    clients = models.ManyToManyField('ClientOfService', verbose_name='clients')
    time_of_sending_the_newsletter = models.TimeField(auto_now=False, auto_now_add=False,
                                                      verbose_name='time of sending the newsletter')
    interval = models.CharField(max_length=100, choices=INTERVAL_CHOICES, default=DAILY)

    newsletter_status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=CREATED)

    is_relevant = models.BooleanField(default=True, verbose_name='relevant status', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='owner')

    def __str__(self):
        return f'{self.newsletter_title}>'

    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'
        ordering = ('time_of_sending_the_newsletter',)


class ClientOfService(models.Model):
    """Client which will got the newsletter. """
    contact_email = models.EmailField(max_length=254, unique=True, verbose_name='contact email')
    last_first_middle_name = models.CharField(max_length=150, verbose_name='full name')
    comment = models.TextField(max_length=5000, verbose_name='comment')
    is_relevant = models.BooleanField(default=True, verbose_name='relevant status', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='owner')

    def __str__(self):
        return f'{self.last_first_middle_name} ({self.contact_email})'

    class Meta:
        verbose_name = 'client of service'
        verbose_name_plural = 'clients of service'
        ordering = ('contact_email',)


class Message(models.Model):
    """Message will be inside the newsletter"""
    message_title = models.CharField(max_length=250, verbose_name='message title')
    message_content = models.TextField(max_length=5000, verbose_name='message content')
    newsletter = models.OneToOneField('Newsletter', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.message_content}'

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ('message_title',)


class NewsletterLogs(models.Model):
    """This is info about results of mailing."""

    datatime_of_last_try = models.DateTimeField(verbose_name='datatime of last try')
    status_of_try = models.BooleanField(verbose_name='status of try')
    response_of_mail_server = models.BooleanField(verbose_name='response of mail server')
    newsletter = models.OneToOneField('Newsletter', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.datatime_of_last_try}, {self.status_of_try}, {self.response_of_mail_server}, {self.newsletter}.'

    class Meta:
        verbose_name = 'newsletter logs'
        verbose_name_plural = 'newsletters logs'
        ordering = ('datatime_of_last_try',)

