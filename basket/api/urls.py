from . import views
from django.urls import path

app_name = "basket_api"


urlpatterns = [
    path("list/", views.BasketListView.as_view(), name="list"),
    path("edit/<id>/", views.BasketEditView.as_view(), name="edit"),
    path("create/", views.BasketCreateView.as_view(), name="create"),
]

