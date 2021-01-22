from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product
from .models import *
from .models import Profile
from PIL import Image
from django.core.files import File
from .models import Post


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description"]


# class WorkshopForm(forms.ModelForm):
#     class Meta:
#         model = Workshop
#         fields = ["name", "Main_Img"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["profile_pic"]


# class PostForm(forms.ModelForm):
#     x = forms.FloatField(widget=forms.HiddenInput())
#     y = forms.FloatField(widget=forms.HiddenInput())
#     width = forms.FloatField(widget=forms.HiddenInput())
#     height = forms.FloatField(widget=forms.HiddenInput())

#     class Meta:
#         model = Post
#         fields = (
#             "painting",
#             "x",
#             "y",
#             "width",
#             "height",
#         )

#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)

#     def save(self):
#         post = super(PostForm, self).save()

#         x = self.cleaned_data.get("x")
#         y = self.cleaned_data.get("y")
#         w = self.cleaned_data.get("width")
#         h = self.cleaned_data.get("height")

#         image = Image.open(post.painting)
#         cropped_image = image.crop(x, y, w + x, h + y)
#         resized_image = cropped_image.resize((1200, 600), Image.ANTIALIAS)
#         resized_image.save(post.painting.path)

#         return post