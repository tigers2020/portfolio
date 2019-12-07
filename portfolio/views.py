from django.views import generic

from contents.models import Contents


class IndexView(generic.ListView):
    model = Contents

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['essay_list'] = Contents.objects.filter(main_text=True)
        return context
