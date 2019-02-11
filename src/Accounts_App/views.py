from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.shortcuts import get_object_or_404
from .forms import ProfileForm,UserForm
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm

def accounts(request):
    return HttpResponse('Hello')
#######################################################
#                  register Users                     #
#######################################################
def register_users(request):
    return render(request,'signup.html',{})
def register_backend(request):
    try:
        cr = [
        request.POST['username'],
        request.POST['password'],
        request.POST['email']
    ]
        new_user = User.objects.create_user(cr)
        new_user.first_name = request.POST['first_name']
        new_user.last_name = request.POST['last_name']
        new_user.save()
        return redirect('/notes')
    except:
        return HttpResponse('User is Exist')
#######################################################
#                   login User                        #
#######################################################
def login_user(request):
    return render(request,'login.html',{})
def login_user_backend(request):
    u = request.POST['username']
    p = request.POST['password']
    registered_user = authenticate(username = u, password = p)
    if registered_user is not None :
        login(request, registered_user)
        login_profile = '/accounts/user_profile/'+ str(registered_user)
        return HttpResponseRedirect(login_profile)
    else :
        return HttpResponse('User Is Not Exist')
#######################################################
#                User   Profile                       #
#######################################################
def user_profile(request, user):
    #profile = get_object_or_404(Profile, user=user)
    context = {'profile':user}
    return render(request,'user_profile.html',context)
#######################################################
#                   logout User                       #
#######################################################
def logout_user(request):
    logout(request)
    return redirect('/')
#######################################################
#Form                Edit User                        #
#######################################################
def edit_profile(request, user):
    profile = get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        User_Form    = UserForm(request.POST, request.user)
        Profile_Form = ProfileForm(request.POST, reqest.FILES, instance = profile)
        if User_Form.is_valid() and Profile_Form.is_valid():
            User_Form.save()
            new_user = Profile_Form.save()
            #new_profile.user = request.user  #old virgin
            #new_profile.save()               #old virgin
            return redirect('/notes')
    else:
        User_Form    = UserForm(instance = request.user)
        Profile_Form = ProfileForm(instance = profile)
    context = {'User_Form':User_Form, 'Profile_Form':Profile_Form}
    return render(request, 'edit_profile.html',context)
#######################################################
#Form               Change Password User              #
#######################################################
def change_password(request, user):
    profile = get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
        return redirect ('/')
    else :
        password_form = PasswordChangeForm(request.user)
    context = {'password_form':password_form}
    return render(request,'change_password.html',context)
#######################################################
#                                                     #
#######################################################
