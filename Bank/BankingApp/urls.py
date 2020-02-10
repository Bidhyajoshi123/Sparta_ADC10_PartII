from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('add_new', views.add_new, name="add_new"),
    path('show_all', views.show_all, name="show_all"),
    path('edit_delete', views.edit_delete, name="edit_delete"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('search/', views.search, name="search"),
    path('upload/', views.upload, name="upload"),
    path('signup/',views.signup, name="signup"),
    
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)