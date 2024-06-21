from django.views import generic
from django.shortcuts import render

# Create your views here.
def about_page(request):
    """
    View that renders the about.html page.
    """

    return render(
        request,
        "about/about.html"
    )