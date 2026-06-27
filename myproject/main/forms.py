from django import forms
from .models import Student, Course

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("ფასი უნდა იყოს 0-ზე მეტი.")
        
        return price
    
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = "__all__"

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = "__all__"

    def clean_duration(self):
        duration = self.cleaned_data["duration"]

        if duration < 1:
            raise forms.ValidationError("კურსის ხანგრძლივობა უნდა იყოს მინიმუმ 1.")

        return duration
    
        

        