from django.urls import path
from . import views

app_name = 'restapi'
urlpatterns = [
    path('customers/',views.customer_data),
    path('customers/<int:pk>/',views.get_customer),
    path('customers/new/', views.add_customer),
    path('customers/paginated/<int:page_num>/<int:num_data>/', views.customer_objects_pagination),
    path('customers/change/<int:pk>/', views.update_api_data),
]
