from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from image_cropping import ImageRatioField
from PIL import Image

# from image_cropping import ImageRatioField

# from django.core.urlresolvers import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)


class Workshop(models.Model):
    name = models.CharField(max_length=50)
    Main_Img = models.ImageField(upload_to="images/")
    Description = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("workshops")


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        null=True,
        blank=True,
        max_length=255,
        default="default.jpg",
        upload_to="profile_pics",
    )
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.user} Profile "


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    painting = models.ImageField(
        upload_to="posts/", null=True, blank=False, max_length=255
    )
    # cropping = ImageRatioField("painting", "430x360")
    # size is "width x height"
    # cropping = ImageRatioField("painting", "430x360")
    class Meta:
        verbose_name = "Post"

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.painting.path)

    #     if img.height > 400 or img.width > 400:
    #         output_size = (400, 400)
    #         img.thumbnail(output_size)
    #         img.save(self.painting.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("post-detail", kwargs={"pk": self.pk})
        return reverse("posts-page")
