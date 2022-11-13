from django.urls import path
from contribution import views

urlpatterns = [
    path('<str:products>/', views.mark_shipment_products),
    path('<str:money>/', views.mark_shipment_money),
    path('<str:services>/', views.mark_shipment_services),
    path('<str:food>/', views.mark_shipment_food),
    path('', views.get_all_contribution)
]