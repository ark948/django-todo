from django.urls import path
from accounts.views import SignupPageView

# unused - replaced by django-allauth (entire file - urls.py)
app_name = "accounts"
urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
]