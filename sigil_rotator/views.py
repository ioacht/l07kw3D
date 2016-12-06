from django.http import HttpResponse
from django.template import loader

from .models import Sigil

def index(request):
    sigils_list = Sigil.objects.order_by('-upload_date')[:5]
    template = loader.get_template('sigil_rotator/index.html')
    context = {
        'sigils_list': sigils_list,
    }
    return HttpResponse(template.render(context, request))

def show(request, sigil_id):
    response = "Showing sigil '%s'!"
    return HttpResponse(response % sigil_id)