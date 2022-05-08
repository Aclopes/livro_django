from django.urls import path
from medicSearch.views.MedicView import list_medic_view, add_favorite_view

urlpatterns = [
    path("", list_medic_view, name='medics'),
    path("favorite", add_favorite_view, name='medic-favorite'),
]