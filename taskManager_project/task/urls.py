from django.urls import path

from . import views

app_name="task"
urlpatterns = [
	path('', views.list, name='list'),
	path('details', views.details, name='details'),
	path('create', views.create, name='create'),
	path('delete', views.delete, name='delete'),
]