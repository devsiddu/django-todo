from django.urls import path
from . import views
urlpatterns = [
    path('add-task/', views.add_task, name='add_task'),
    path('update-task/<int:id>/', views.update_task, name='update_task'),

]

