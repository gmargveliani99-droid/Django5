from django.shortcuts import render, redirect
from .forms import ProductForm, StudentForm, CourseForm
from .models import Product, Student, Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_list.html", {"courses": courses})

def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})

def product_view(request):

    form = ProductForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():

            Product.objects.create(
                name=form.cleaned_data["name"],
                price=form.cleaned_data["price"]
            )

            return redirect("success")

    return render(request, "product_form.html", {"form": form})
    
def student_view(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("success")

    else:
        form = StudentForm()

    return render(request, "student_form.html", {"form": form})


def course_view(request):

    if request.method == "POST":

        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("success")

    else:
        form = CourseForm()

    return render(request, "course_form.html", {"form": form})


def success(request):
    return render(request, "success.html")

def home(request):
    return render(request, "home.html")