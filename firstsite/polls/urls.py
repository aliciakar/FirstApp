from django.urls import path
from . import views

app_name="polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/resultat/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/rosta/", views.vote, name="vote"),
]
