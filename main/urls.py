from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('shop/', views.product_list, name='product_list'),
    path('catalog/<slug:category_slug>/', views.product_list, name='category_slug'),
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
]