# from django.http import HttpResponse
from django.shortcuts import render
from medicSearch.models import Profile
from django.db.models import Q
from django.core.paginator import Paginator

def list_medic_view(request):
    name = request.GET.get("name")
    speciality = request.GET.get("speciality")
    neighborhood = request.GET.get('neighborhood')
    city = request.GET.get('city')
    state = request.GET.get('state')

    medics = Profile.objects.filter(role=2)

    if name:
        medics = medics.filter(Q(user__first_name__contains=name)|Q(user__username__contains=name))
    if speciality:
        medics = medics.filter(speciality__id=speciality)
    if neighborhood:
        medics = medics.filter(addresses__neighborhood__id=neighborhood)
    if city:
        medics = medics.filter(addresses__neighborhood__city=city)
    if state:
        medics = medics.filter(addresses__neighborhood__city__state=state)
    
    print("***************DEBUG******************")
    print("Name: " + str(name))
    print("Specialty: " + str(speciality))
    print("Neighborhood: " + str(neighborhood))
    print("City: " + str(city))
    print("State: " + str(state))
    print(medics)
    print("*************END DEBUG*****************")

    if len(medics) > 0:
        paginator = Paginator(medics, 8)
        page = request.GET.get('page')
        medics = paginator.get_page(page)

    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()

    context = {
        'medics': medics,
        'parameters': parameters
    }

    return render(request=request, template_name='medic/medics.html', context=context, status=200)
    #return HttpResponse('Listagem de 1 ou mais medicos %s' % str(medic.all().values('id')))
