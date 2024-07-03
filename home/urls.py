from . import views
from django.urls import path

def homepage_view(request):
    raise Exception("This is a test error")

urlpatterns = [
    path('', views.index_page, name='home'),
    path("500/", homepage_view),
]
