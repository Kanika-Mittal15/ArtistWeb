from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product, Profile, Post
from django.http import HttpResponse
from .forms import *
from .forms import ProfileUpdateForm, UserUpdateForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import os


TEMP_PROFILE_IMAGE_NAME = "temp_profile_image.png"

# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import Album

# Create your views here.


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account was created for " + user)

                return redirect("login")

        context = {"form": form}
        return render(request, "products/register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username OR password is incorrect")

        context = {}
        return render(request, "products/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")  # put above every view to restrict them
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/home.html", context)


# class AlbumCreate(CreateView):
# model = Album
# fields = ["artist", "album_title", "genre", "album_logo"]


# @login_required(login_url="login")
class WorkshopCreateView(LoginRequiredMixin, CreateView):
    model = Workshop
    fields = ["name", "Main_Img", "Description"]
    template_name = "products/workshop_form.html"


# def hotel_image_view(request):

#     if request.method == "POST":
#         form = WorkshopForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()

#             return redirect("hotel_images")
#             # return redirect("success")
#     else:
#         form = WorkshopForm()
#     return render(request, "products/hotel_image_form.html", {"form": form})


# def success(request):
# return HttpResponse("successfully uploaded")


# Python program to view
# for displaying images


# @login_required(login_url="login")
class WorkshopListView(ListView):
    model = Workshop
    template_name = "products/Workshop.html"
    context_object_name = "workshops"
    ordering = ["-date_posted"]


# def display_hotel_images(request):

#     if request.method == "GET":

#         # getting all the objects of hotel.
#         Workshops = Workshop.objects.all()
#         return render(
#             request, "products/display_hotel_images.html", {"hotel_images": Workshops}
#         )


# def product_delete_view(request, id):
# obj = get_object_or_404(Product, id=id)
# POST request
# if request.method == "POST":
# confirming delete
#   obj.delete()
#  return redirect("../../")
# context = {"object": obj}
# return render(request, "products/product_delete.html", context)
@login_required(login_url="login")
def profile(request):
    if request.method == "POST":
        # profile = request.user.profile
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        # if request.method == "POST":
        if u_form.is_valid() and p_form.is_valid:
            u_form.save()
            p_form.save()

            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "products/profile.html", context)


class PostListView(ListView):
    model = Post
    template_name = "products/posts.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class UserPostListView(ListView):
    model = Post
    template_name = "products/user_posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(artist=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Post
    template_name = "products/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "description", "painting"]
    template_name = "products/post_form.html"

    def form_valid(self, form):
        form.instance.artist = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "description", "painting"]

    def form_valid(self, form):
        form.instance.artist = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.artist:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/posts/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.artist:
            return True
        return False
