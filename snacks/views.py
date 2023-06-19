from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack
from django.urls import reverse_lazy

# Create your views here.
class ListPageView(ListView):
    template_name='snack_list_view.html'
    model = Snack
    context_object_name = 'snacks'

class DetailPageView(DetailView):
    template_name='snack_detail_view.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name='create_snack.html'
    model=Snack
    fields = [
        'name',
        'description',
        'purchaser'
        ]
    
class SnackUpdateView(UpdateView):
    template_name='update_snack.html'
    model=Snack
    fields = [
        'name',
        'description',
        'purchaser'
        ]
    
class SnackDeleteView(DeleteView):
    template_name='delete_snack.html'
    model=Snack
    success_url=reverse_lazy('snack_list')