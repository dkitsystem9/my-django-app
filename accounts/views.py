from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .models import User
from django.contrib import messages

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully!")
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                request.session['user_id'] = user.id  # Store user in session
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('home')  # ✅ redirect to home page
            except User.DoesNotExist:
                messages.error(request, "Invalid username or password.")
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('login')
def home_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, "You must be logged in to access this page.")
        return redirect('login')
    user = User.objects.get(id=user_id)
    return render(request, 'accounts/home.html', {'user': user})
