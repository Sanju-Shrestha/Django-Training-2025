from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.http import HttpResponseForbidden
from .forms import CustomUserCreationForm, PostForm
from .models import CustomUser

def home(request):
    return render(request, 'accounts/home.html')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/login/'
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

@login_required
def profile(request):
    if request.user.is_banned:
        return HttpResponseForbidden("Your account is banned")
    return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
@permission_required('accounts.add_post', raise_exception=True)
def create_post(request):
    if request.user.is_banned:
        return HttpResponseForbidden("Your account is banned")
        
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'accounts/create_post.html', {'form': form})