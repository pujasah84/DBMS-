from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, FormView, ListView, UpdateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect

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
        return redirect("create/customer")

class CustomerPage(LoginRequiredMixin,TemplateView):
    login_url = "login"
    model = Account
    fields = "__all__"
    template_name = "create_customer.html"
    # success_url = "customerlist"

    def get_context_data(self, **kwargs):
        context=  super().get_context_data(**kwargs)
        context["customerForm"] = customerForm()
        context["accountForm"] = accountForm()
        return context

    def post(self, request, *args, **kwargs):
        customer_form = customerForm(self.request.POST)
        account_form = accountForm(self.request.POST)

        if customer_form.is_valid() and account_form.is_valid():
            customer = customer_form.save()
            account = account_form.save()
            print(account,"account")
            customer.account = account
            customer.save()
            return HttpResponseRedirect(
                reverse_lazy('customer_list')
            )
        context = self.get_context_data()
        context["customerForm"] = customer_form
        context["accountForm"] = account_form
        return self.render_to_response(context)
        
        # return self.render_to_response(
        #     self.get_context_data(
        #         customerForm=customer_form,
        #         accountForm=account_form
        #     )
        # )
    
    
class View_Transaction(LoginRequiredMixin,ListView):
    login_url = "login"
    model = Transaction
    template_name = "view_transaction.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.all()

class customer(LoginRequiredMixin,ListView):
    login_url = "login"
    model = Customer
    template_name = "customer_list.html"
    context_object_name = "customers"

    def get_queryset(self):
        return Customer.objects.all()
