from django import forms

from blogs.models import Blog


class BlogForm(forms.ModelForm):
    """Form for blog."""
    class Meta:
        model = Blog
        exclude = ('count_of_views', 'date_of_publish', 'owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
