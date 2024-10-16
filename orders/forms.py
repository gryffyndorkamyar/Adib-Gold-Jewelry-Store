from .models import Order
from django import forms 
from django.core.exceptions import ValidationError

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','phone_number','address','order_notes']
    
        widgets = {
            "first_name":forms.TextInput({"class":"form-control mb-4"}),
            "last_name":forms.TextInput({"class":"form-control mb-4"}),
            "phone_number":forms.TextInput({"class":"form-control mb-4"}),
            "address":forms.Textarea({"class":"form-control mb-4","rows":"6"}),
            "order_notes":forms.Textarea({"class":"form-control mb-4","rows":"5"}),
        }
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")

        if not phone_number.isdigit():
            raise ValidationError("شماره تلفن باید عدد باشد")

        if len(phone_number) != 11:
            raise ValidationError("شماره تماس باید 11 رقم باشد")
        
         
        if not phone_number.startswith("09"):
            raise ValidationError("شماره تلفن باید با 09 شروع شود")

        
        return phone_number
