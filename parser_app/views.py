from django.shortcuts import render, HttpResponse
from . import models, forms
from django.views import generic

class RezkaListView(generic.ListView):
    template_name = 'parser/rezka_list.html'
    context_object_name = 'rezka'
    model = models.RezkaModel
    paginate_by = 3
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class RezkaFormView(generic.FormView):
    template_name = 'parser/rezka_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('STATUS 200')
        else:
            return super(RezkaFormView, self).post(request, *args, **kwargs)

