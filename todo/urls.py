from django.urls import path
from . import views
urlpatterns = [
    path('add-task/', views.add_task, name='add_task'),
    # Mark as done 
    path('mark-task/<int:id>/', views.update_task, name='update_task'),
    # Mark as Undone
    path('unmark-task/<int:id>/', views.unmark_task, name='unmark_task'),
    # Edit Task
    path('edit_task/<int:id>/', views.edit_task, name='edit_task'),
    # Delete Task
    path('delete_task/<int:id>/', views.delete_task, name='delete_task')

]

