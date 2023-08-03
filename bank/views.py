from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, FormView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
def index(request):
    return render(request, "index.html")

class LoginPage(FormView):
    form_class = LoginForm
    template_name = "login.html"
    

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        if "next" in self.request.GET:
            return redirect(self.request.GET.get("next"))
        return reverse_lazy("bank:create_customer")

class CustomerPage(LoginRequiredMixin,CreateView):
    # login_url = redirect("create/customer")
    model = Customer
    fields = "__all__"
    template_name = "create_customer.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)