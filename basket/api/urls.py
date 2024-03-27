from django.urls import path
from . import views

app_name = "basket_api"


urlpatterns = [
    path("list/", views.BasketListView.as_view(), name="list"),
    path("create/", views.BasketCreateView.as_view(), name="create"),
    path("edit/<id>/", views.BasketEditView.as_view(), name="edit"),
]

