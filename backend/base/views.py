from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.


def home(request):
    model = Product.objects.all()
    context = {"products": model}
    return render(request, "index.html", context)


def create_form(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    context = {"form": form}
    return render(request, "forms.html", context)


def update_form(request, pk):
    model = Product.objects.get(id=pk)
    form = ProductForm(instance=model)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=model)
        if form.is_valid():
            form.save()

        return redirect("/")

    context = {"form": form}

    return render(request, "forms.html", context)
