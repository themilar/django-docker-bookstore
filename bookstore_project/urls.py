"""bookstore_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth.views import LoginView

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),

    # overriding django auth defaults
    # path(
    #     route='accounts/login/',
    #     view=LoginView.as_view(template_name='login'),
    #     name='login'
    # ),

    # user management
    path('accounts/', include('allauth.urls')),

    # local apps
    path('', include('pages.urls', namespace='page')),
    path('books/', include('books.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
