from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("success/", success, name="success"),

    # PRODUCT
    path("product/", product_list, name="product_list"),
    path("product/create/", product_create, name="product_create"),
    path("product/update/<int:pk>/", product_update, name="product_update"),
    path("product/delete/<int:pk>/", product_delete, name="product_delete"),

    # STUDENT
    path("student/", student_list, name="student_list"),
    path("student/create/", student_create, name="student_create"),
    path("student/update/<int:pk>/", student_update, name="student_update"),
    path("student/delete/<int:pk>/", student_delete, name="student_delete"),

    # COURSE
    path("course/", course_list, name="course_list"),
    path("course/create/", course_create, name="course_create"),
    path("course/update/<int:pk>/", course_update, name="course_update"),
    path("course/delete/<int:pk>/", course_delete, name="course_delete"),
]