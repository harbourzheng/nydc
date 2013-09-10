from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView
from system.models import *
from django.db import models
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta:
       model = UserProfile
       exclude = ["user"]
def search_form(request): 
    return render_to_response(request,"member/search_form.html")
@login_required
def main(request):
	profile =UserProfile.objects.get(user=request.user.pk)
	return render_to_response("member/main.html", profile=profile)
def search(request):
      if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        cat = request.GET['my_options']
        users = UserProfile.objects.filter(nick_name__icontains=q)
        return render(request, 'member/search_form.html',
            {'users': users, 'cat': cat,'query':q})
    else:
        return HttpResponse('Please submit a search term.')
@login_required
def profile(request, pk):
    """Edit user profile."""
    profile = UserProfile.objects.get(user=pk)
    img = None

    if request.method == "POST":
        pf = ProfileForm(request.POST, request.FILES, instance=profile)
        if pf.is_valid():
            pf.save()
            # resize and save image under same filename
            imfn = pjoin(MEDIA_ROOT, profile.avatar.name)
            im = PImage.open(imfn)
            im.thumbnail((160,160), PImage.ANTIALIAS)
            im.save(imfn, "JPEG")
    else:
        pf = ProfileForm(instance=profile)

    if profile.avatar:
        img = "/media/" + profile.avatar.name
    return render_to_response("inner/profile.html", add_csrf(request, pf=pf, img=img))
