from django.views.generic.edit import CreateView

from .models import Product
from django.http import HttpResponseRedirect


class Add(CreateView):
    model = Product
    fields = ('name','weight','price')
    template_name = 'product.html'
    success_url = '/product/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
 