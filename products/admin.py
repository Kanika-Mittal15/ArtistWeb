from django.contrib import admin
from .models import Product, Workshop, Profile, Post
from image_cropping import ImageCroppingMixin
from django.forms import TextInput, Textarea
from django.db import models

# from .forms import PostForm

# Register your models here.
# class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
#   pass
class PostAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super(PostAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["description"].widget.attrs["style"] = "width: 45em;"
        return form


admin.site.register(Post, PostAdmin)
admin.site.register(Product)
admin.site.register(Workshop)
admin.site.register(Profile)

# class PostAdminInline(admin.TabularInline):
#     model = Post  # from models.py
#     form = PostForm  # from forms.py, sets
