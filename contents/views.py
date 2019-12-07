from django.shortcuts import render

# Create your views here.
from django.views import generic

import contents
from .models import Contents

class CategoryView(generic.ListView):
    model = Contents
    template_name = 'contents/category.html'
    def get_context_data(self, *args, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['essay_list'] = Contents.objects.filter(main_text=True)
        context['contents_list'] = Contents.objects.filter(category= self.kwargs['pk'])
        return context