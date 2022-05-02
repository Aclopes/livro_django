from django.urls import path
from medicSearch.views.MedicView import list_medic_view

urlpatterns = [
    path("", list_medic_view, name='medics'),
]