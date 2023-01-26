from django.urls import path
from . import views

urlpatterns = [
     path('simpleapi', views.simpleapi, name='simple_api'),
     path('login', views.login, name='login_api'),
     path('medicinedetails', views.medicinedetails, name='medicine_name_api'),

     path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
     path("update/<int:id>/",views.UpdateTodoAPIView.as_view(),name="update_todo"),
     path("delete/<int:id>/",views.DeleteTodoAPIView.as_view(),name="delete_todo")
    
]


