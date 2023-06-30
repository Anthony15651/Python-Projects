from django.urls import path
from . import views


# Setting up the URL paths for each html page.
urlpatterns = [
    path('', views.home, name="index"),
    path('create/', views.create_account, name="create"),
    path('<int:pk>/balance/', views.balance, name="balance"),
    path('transaction/', views.transaction, name="transaction"),
]