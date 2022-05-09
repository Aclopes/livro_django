# from django.http import HttpResponse
from django.shortcuts import render, redirect
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



def add_favorite_view(request):
    page = request.POST.get('page')
    name = request.POST.get('name')
    speciality = request.POST.get('speciality')
    neighborhood = request.POST.get('neighborhood')
    city = request.POST.get('city')
    state = request.POST.get('state')
    id = request.POST.get('id')
    msg = None
    _type = None

    try:
        profile = Profile.objects.filter(user=request.user).first()
        medic = Profile.objects.filter(user__id=id).first()
        profile.favorites.add(medic.user)
        profile.save()
        # msg = "Doctor added to Favorites"
        # _type = 'success'
    except Exception as e:
        print("ERROR: %s" % e)
        msg = "An error when try to save a Doctor in Favorites"
        _type = 'danger'
    
    arguments = "?page=1"
    if page:
        arguments = "?page=%s" % (page)    
    if name:
        arguments += "&name=%s" % name
    if speciality:
        arguments += "&specinality=%s" % speciality
    if neighborhood:
        arguments += "&neighborhood=%s" % neighborhood
    if city:
        arguments += "&city=%s" % city
    if state:
        arguments += "&state=%s" % state
    if msg and _type:
        arguments += "&msg=%s&type=%s" % (msg, _type)

    return redirect(to="/medic/%s" % arguments)