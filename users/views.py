from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect
 

from .forms import ProfileUpdateForm, UserForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.


class SignUp(generic.CreateView):
    form_class = UserForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'Account created successfully for {form.cleaned_data.get("username")}')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    
    
    
@login_required

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)