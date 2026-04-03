from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile']

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','stock','description','about','category','product_image']
        widgets = {
            'name': forms.TextInput(attrs={'maxlength': 120}),
            'description': forms.Textarea(attrs={'rows': 6}),
            'about': forms.Textarea(attrs={'rows': 6}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    @staticmethod
    def _normalize_multiline_text(value):
        if not value:
            return value
        lines = [line.strip() for line in value.replace('\r\n', '\n').split('\n') if line.strip()]
        return '\n'.join(lines)

    def clean_description(self):
        return self._normalize_multiline_text(self.cleaned_data.get('description'))

    def clean_about(self):
        return self._normalize_multiline_text(self.cleaned_data.get('about'))

# address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    first_name = forms.CharField(max_length=150, label='First name')
    new_password1 = forms.CharField(widget=forms.PasswordInput, label='New password')
    new_password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm new password')

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('new_password1')
        p2 = cleaned_data.get('new_password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Passwords do not match.')
        if p1 and len(p1) < 6:
            raise forms.ValidationError('Password must be at least 6 characters long.')
        return cleaned_data

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Order
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)], attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Write your review here...'}),
        }

class CouponForm(forms.ModelForm):
    class Meta:
        model = models.Coupon
        fields = ['code', 'discount_percent', 'active', 'expiry']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'discount_percent': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 100}),
            'expiry': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class ApplyCouponForm(forms.Form):
    code = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter coupon code'}))


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = models.Complaint
        fields = ['product', 'complaint_type', 'subject', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'complaint_type': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief summary of your complaint'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe your complaint in detail...'}),
        }
