from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import generic
from .models import Feedback
from .forms import FeedbackModelForm
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackModelForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        response = super().form_valid(form)
        name = form.cleaned_data.get('name')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        from_email = form.cleaned_data.get('from_email')
        send_mail(subject.strip(),
                  message,
                  from_email,
                  ['d.khomyk@gmail.com'])
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return response