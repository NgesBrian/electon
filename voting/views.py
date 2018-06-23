from django.http import HttpResponse

from django.shortcuts import render, redirect

from voting.forms import SignUpForm, UpdateProfile

from django.contrib.sites.shortcuts import get_current_site

from django.utils.encoding import force_bytes

from django.utils.http import urlsafe_base64_encode

from django.template.loader import render_to_string

from voting.tokens import account_activation_token

from django.contrib.auth import login

from django.contrib.auth.models import User

from django.utils.encoding import force_text

from django.utils.http import urlsafe_base64_decode

from .forms import ContactForm

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'voting/index.html')

def about(request):
    return render(request, 'voting/about.html')

def contact(request):
    args = {}
    if request.method == 'POST':    #form submitted
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            #display and alert upon successful sav
            msgInfo = "Your Feedback has been submitted!"
            args['msgInfo'] = msgInfo
            #return redirect('guest:update_profile_success')
    form = ContactForm()

    args['form'] = form
    return render(request, 'voting/contact.html', args)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your EVS Account'
            message = render_to_string('voting/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'voting/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'voting/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('authusers:home')
    else:
        return render(request, 'voting/account_activation_invalid.html')

def update_profile(request):
    args = {}
    if request.method == 'POST':    #form submitted
        form = UpdateProfile(request.POST, instance=request.user)
        #form.actual_user = request.user
        if form.is_valid():
            form.save()
            #display and alert upon successful sav
            msgInfo = "Your profile info successfully updated!"
            args['msgInfo'] = msgInfo

    user = request.user
    form = UpdateProfile(initial={'email': user.email, 'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name})

    args['form'] = form
    return render(request, 'voting/update_profile.html', args)