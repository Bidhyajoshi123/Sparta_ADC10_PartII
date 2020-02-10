from django.urls import path
from . import views

app_name = 'restapi'
urlpatterns = [
    path('customers/',views.customer_data),
    path('customers/<int:pk>/',views.get_customer),
    path('customers/change/<int:pk>/', views.update_api_data),
    
   
]
