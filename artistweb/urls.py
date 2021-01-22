"""artistweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from products import views
from products.views import (
    registerPage,
    loginPage,
    logoutUser,
    product_create_view,
    WorkshopCreateView,
    # success,
    WorkshopListView,
    profile,
    # product_delete_view,
    # AlbumCreate,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", product_create_view, name="home"),
    path("register/", registerPage, name="register"),
    path("login/", loginPage, name="login"),
    path("logout/", logoutUser, name="logout"),
    path("add_workshop/", WorkshopCreateView.as_view(), name="add_workshop"),
    # path("success", success, name="success"),
    path("workshops/", WorkshopListView.as_view(), name="workshops"),
    path("profile/", profile, name="profile"),
    path("posts/", PostListView.as_view(), name="posts-page"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/update", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("posts/new/", PostCreateView.as_view(), name="post-create")
    # path("<int:id>/delete/", product_delete_view, name="product-delete")
    # path("add/", AlbumCreate, name="album-add"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
