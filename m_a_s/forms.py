from django import forms

from m_a_s.models import ClientOfService, Newsletter, Message


class ClientForm(forms.ModelForm):
    """Form for creating/updating the client."""
    class Meta:
        model = ClientOfService
        exclude = ('owner', 'is_relevant',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class NewsletterForm(forms.ModelForm):
    """Form for creating/updating the newsletter."""
    class Meta:
        model = Newsletter
        exclude = ('owner', 'is_relevant',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MessageForm(forms.ModelForm):
    """Form for creating/updating the message."""
    class Meta:
        model = Message
        fields = ('message_title', 'message_content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
