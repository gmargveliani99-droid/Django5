from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),   # მთავარი გვერდი
    path("product/", views.product_view, name="product"),
    path("student/", views.student_view, name="student"),
    path("course/", views.course_view, name="course"),
    path("success/", views.success, name="success"),
    path("products/", views.product_list, name="product_list"),
    path("students/", views.student_list, name="student_list"),
    path("courses/", views.course_list, name="course_list"),
]