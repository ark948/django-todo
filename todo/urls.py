from django.urls import path
from todo.views import TodoHomePage

app_name = "todo"
urlpatterns = [
    path("", TodoHomePage.as_view(), name="index"),
]