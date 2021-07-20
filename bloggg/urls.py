"""bloggg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from blogapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home.as_view(),name='home'),
    path('regapp/', include('regapp.urls')),
    path('regapp/regapp/', include('regapp.urls')),
    path('add/',views.add,name='add'),
    path('detail/<int:pk>/',views.detail.as_view(),name='detail'),
    path('regapp/detail/<int:pk>',views.detail.as_view(),name='detail'),
    path('detail/<int:p>/update/<int:pk>', views.update.as_view(), name='update'),
    path('detail/<int:p>/delete/<int:pk>', views.deleto.as_view(), name='delete'),

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)