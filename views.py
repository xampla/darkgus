from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Dork, Result
from .forms import DomainCheckForm, LoginForm, RegisterForm

def index(request):
    form = DomainCheckForm()
    context = {'form': form}
    return render(request, 'argusdorker/index.html', context)

def pricing(request):
    return render(request, 'argusdorker/pricing.html')

def user_view(request):
    return render(request, 'argusdorker/user.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('app:index'))  # Replace 'app:index' with the appropriate namespace and URL name for your app's index page
            else:
                return render(request, 'argusdorker/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = LoginForm()
    return render(request, 'argusdorker/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        plan = request.POST.get('plan', None)
        create_account_only = request.POST.get('create_account_only', False)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect the user to the selected plan or the home page
            if not create_account_only and plan:
                return redirect(reverse('app:pricing') + f'?plan={plan}')  # Replace 'app:pricing' with the appropriate namespace and URL name for your app's pricing page
            return redirect('app:index')  # Replace 'app:index' with the appropriate namespace and URL name for your app's index page
        else:
            errors = {field: errors[0] for field, errors in form.errors.items()}
            return JsonResponse({'status': 'error', 'errors': errors})
    else:
        form = RegisterForm()
    return render(request, 'argusdorker/register.html', {'form': form})


# API LIKE endpoints
def check_domain(request):
    domain = request.GET.get('domain', '')
    form = DomainCheckForm(request.POST)
    if form.is_valid():
        if domain:
            exists_in_db = Result.objects.filter(url__icontains=domain).exists()
            response = {'domain_found': exists_in_db}
        else:
            response = {'error': 'Invalid domain'}
    else:
        response = {'error': 'Do the captcha'}

    return JsonResponse(response)

def get_stats(request):
    dorks_count = Dork.objects.count()
    urls_count = Result.objects.count()
    domains_count = Result.objects.values("url").distinct().count()

    data = {
        "dorks_count": dorks_count,
        "urls_count": urls_count,
        "domains_count": domains_count,
    }

    return JsonResponse(data)