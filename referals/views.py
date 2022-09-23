from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# Create your views here.

def home(request):

    #get the logged in users profile
    profile = Profile.objects.get(user=request.user)

    #get the list of profiles recommeded by the user
    my_recs = profile.get_recommend_profiles()

    context = {
        'my_recs': my_recs,
    }
    return render(request, 'referals/index.html', context)


def signUpView(request):
    #store the id of the user that recommeded someone as a variable 
    profile_id = request.session.get('ref_profile')
    print('profile_id', profile_id)

    #user creation form
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        if profile_id is not None:

            #get profile of the recommender
            recommended_by_profile = Profile.objects.get(id=profile_id)
            #save form
            instance = form.save()
        
            registered_user = User.objects.get(id=instance.id)
            #get the registered user
            registered_profile = Profile.objects.get(user=registered_user)
            #assign the recommnder to the profile of the registered user
            registered_profile.recommended_by = recommended_by_profile.user
            registered_profile.save()
        else:
            form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)

        #delete the recommnders code in the session variable after new user has logged in
        if 'ref_profile' in request.session:
            del request.session['ref_profile']

        return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'referals/sign-up.html', context)


def ref_sign_up(request, *args, **kwargs):
    #get reference code
    code = str(kwargs.get('ref_code'))
    try:
        #get recommnders profile
        profile= Profile.objects.get(code=code)
        # store recommnders profile id in a session variable
        request.session['ref_profile'] = profile.id
        print('id', profile.id)
    except:
        pass
    print(request.session.get_expiry_date())
    return render(request, 'referals/referal-page.html', {})
