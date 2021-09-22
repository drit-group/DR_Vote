from account.mixins import formMixin
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from django.views.generic import ListView ,CreateView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin
=======
from django.views.generic import ListView,CreateView,UpdateView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import formMixin
>>>>>>> 24175081143c5fa32d25d2666f8f9eabcd4cee1c
from django.urls import reverse_lazy
# Create your views here.

class DashBoard(LoginRequiredMixin,ListView):
    # model=Article
    login_url = '/admin/login/'
    template_name = "profile/main.html"
    def get_queryset(self):
        return Article.objects.filter(writer=self.request.user)

class addArticle(formMixin,LoginRequiredMixin,CreateView):
    model = Article
    template_name = "profile/addArticle.html"
<<<<<<< HEAD
    fields=['title','slug','thumbnail','description','status']
    success_url=reverse_lazy("account:dashboard")
=======
    fields = ['title','slug','thumbnail','description','status']
    success_url = reverse_lazy("account:dashboard")

>>>>>>> 24175081143c5fa32d25d2666f8f9eabcd4cee1c

class editArticle(LoginRequiredMixin,UpdateView):
    model = Article
    template_name = "profile/addArticle.html"
    fields = ['title','slug','thumbnail','description','status']
    success_url = reverse_lazy("account:dashboard")