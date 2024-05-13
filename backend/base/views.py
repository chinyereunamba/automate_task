from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, CreateUserForm

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        model = Product.objects.filter(user=request.user)
        context = {"products": model}
    else:
        return redirect("/login")
    return render(request, "index.html", context)


def login(request):
    if request.method=="POST":
        username = request.POST.get['username']
        password = request.POST.get['password']

        # user = 
    context = {}
    return render(request, "login.html", context)


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    context = {"form": form}

    return render(request, "register.html", context)


def create_form(request):
    form = ProductForm()
    title = "Add New Product"

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    context = {"form": form, "title": title}
    return render(request, "forms.html", context)


def update_form(request, pk):
    model = Product.objects.get(id=pk)
    form = ProductForm(instance=model)
    title = "Update Product"

    if request.method == "POST":
        form = ProductForm(request.POST, instance=model)
        if form.is_valid():
            form.save()

        return redirect("/")

    context = {"form": form, "title": title}

    return render(request, "forms.html", context)


def delete(request, pk):
    model = Product.objects.get(id=pk)
    if request.method == "POST":
        model.delete()
        return redirect("/")
    context = {"product": model}
    return render(request, "delete.html", context)
