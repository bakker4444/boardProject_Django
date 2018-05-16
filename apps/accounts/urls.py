from django.urls import path, include
from . import views as accounts_views
urlpatterns = [
    path("", accounts_views.signup, name="signup"),
]