import random

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from django.conf import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    success_url = reverse_lazy('mas:m_a_s_list')
    form_class = UserRegisterForm
    template_name = "users/register.html"

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Here we go.',
            message='Now you are registered, dear User.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]

        )

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    success_url = reverse_lazy('mas:m_a_s_list')
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Here we go.',
            message=f'You are successfully changed your info, dear {new_user.first_name}.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]

        )

        return super().form_valid(form)


def generate_new_password(request):
    chars = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
             'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
             'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while True:
        new_password = ''.join([random.choice(chars) for _ in range(8)])
        title_letter_count = 0
        lower_letter_count = 0
        int_count = 0
        for i in range(len(new_password)):
            if new_password[i].isdigit():
                int_count += 1
            elif new_password[i].istitle():
                title_letter_count += 1

            elif new_password[i].islower():
                lower_letter_count += 1
        if title_letter_count < 1 and int_count < 1 and lower_letter_count < 1:
            continue
        else:
            break
    send_mail(
        subject='The new password.',
        message=f'Your new password is "{new_password}"',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]

    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:log_in'))