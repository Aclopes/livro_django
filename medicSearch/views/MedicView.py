from django.http import HttpResponse
from medicSearch.models import Profile

def list_medic_view(request):
    name = request.GET.get("name")
    speciality = request.GET.get("speciality")
    neighborhood = request.GET.get('neighborhood')
    city = request.GET.get('city')
    state = request.GET.get('state')

    medic = Profile.objects.all()
    print(medic)

    return HttpResponse('Listagem de 1 ou mais medicos %s' % state)
