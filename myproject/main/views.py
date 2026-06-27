from django.shortcuts import render, redirect
from .forms import ProductForm, StudentForm, CourseForm
from .models import Product, Student, Course


# ---------------- HOME ----------------
def home(request):
    return render(request, "home.html")


def success(request):
    return render(request, "success.html")


# ---------------- PRODUCT ----------------
def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})


def product_create(request):
    form = ProductForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("product_list")

    return render(request, "product_form.html", {"form": form})


def product_update(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)

    return render(request, "product_form.html", {"form": form})


def product_delete(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(request, "product_delete.html", {"product": product})


# ---------------- STUDENT ----------------
def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})


def student_create(request):
    form = StudentForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("student_list")

    return render(request, "student_form.html", {"form": form})


def student_update(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(request.POST or None, instance=student)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("student_list")

    return render(request, "student_form.html", {"form": form})


def student_delete(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "student_delete.html", {"student": student})


# ---------------- COURSE ----------------
def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_list.html", {"courses": courses})


def course_create(request):
    form = CourseForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("course_list")

    return render(request, "course_form.html", {"form": form})


def course_update(request, pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(request.POST or None, instance=course)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("course_list")

    return render(request, "course_form.html", {"form": form})


def course_delete(request, pk):
    course = Course.objects.get(id=pk)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(request, "course_delete.html", {"course": course})