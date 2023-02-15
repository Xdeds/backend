"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from apps.main.views import MainListView, AboutUsView, CartView, ResultView, leo, add_to_cart, delete, search, category
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', MainListView.as_view(), name='main'),
    path('result/<int:id>', leo, name='result'),
    path('add_to_cart/<int:id>', add_to_cart, name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    # path('category/<slug:slug>', CategoryView.as_view(), name='category'),
    path('category/<slug:slug>', category, name='category'),
    path('delete/<int:id>', delete, name='delete'),
    path('search/', search, name='search'),
    path('result/', ResultView.as_view(), name='result'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
]