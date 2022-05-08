# Cap anterior
# from django.http import HttpResponse
# def list_profile_view(request, id=None):
#     if id:
#         return HttpResponse('<h1>User ID %s</h1>' % id)
#     if request.user.is_authenticated:
#         id = request.user.id
#         return HttpResponse('<h1>Logged User ID %s name %s</h1>' % (id, request.user.username))
#     return HttpResponse('<h1>No user was informed</h1>')
from django.shortcuts import render, redirect
from medicSearch.models import Profile
from django.core.paginator import Paginator


def list_profile_view(request, id=None):
    profile = None

    # diff of the book
    if id:
        profile = Profile.objects.filter(user__id=id).first()
    
    if not id and request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()

    if not profile:
        # TODO create a page to no user
        return redirect(to='/')
    
    favorites = profile.show_favorites()
    if len(favorites) > 0:
        paginator = Paginator(favorites, 8)
        page = request.GET.get('page')
        favorites = paginator.get_page(page)

    context = {
        'profile' : profile,
        'favorites' : favorites
    }

    return render(request=request, template_name='profile/profile.html', context=context, status=200)
