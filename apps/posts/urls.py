from django.urls import path
from . import views

app_name='posts'
urlpatterns = [
    path('crear-post/', views.Nuevo_post.as_view(), name='crear_post'),
]