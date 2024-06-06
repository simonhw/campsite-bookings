from django.shortcuts import render
from django.views import generic

# Create your views here.
# class HomePage(generic.DetailView):
#     queryset = Booking.objects.all().order_by('arrival')
#     template_name = 'home/index.html'

def index_page(request):
    '''
    View that renders the index.html page.
    '''

    return render(
        request,
        "home/index.html"
    )