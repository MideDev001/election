from django.urls import path
from . import views

urlpatterns = [
    path('polling-unit/<int:uniqueid>/', views.polling_unit_results, name='polling_unit_results'),
    path('lga-results/', views.lga_results, name='lga_results'),
    path('add-polling-unit-results/', views.add_polling_unit_results, name='add_polling_unit_results'),


]
