from django.http import HttpResponse

def list_profile_view(request, id=None):
    if id:
        return HttpResponse('<h1>User ID %s</h1>' % id)
    
    if request.user.is_authenticated:
        id = request.user.id
        return HttpResponse('<h1>Logged User ID %s name %s</h1>' % (id, request.user.username))
    
    return HttpResponse('<h1>No user was informed</h1>')
    