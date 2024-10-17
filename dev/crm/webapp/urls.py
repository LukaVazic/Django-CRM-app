
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name = ""),
    path('register', views.register, name = "register"),
    path('login', views.login, name = "login"),
    path('logout', views.logout, name = "logout"),

    # CRUD

    # Create
    path('create', views.create, name = "create"),

    # Read
    path('dashboard', views.dashboard, name = "dashboard"),
    path('record/<int:pk>', views.read_record, name = "record" ),

    # Update
    path('update/<int:pk>', views.update, name = "update"),    

    # Delete
    path('delete/<int:pk>', views.delete, name = "delete"),

    
]
 