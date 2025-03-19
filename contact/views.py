from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy

from contact.models import Contact

class ContactView(CreateView):
    template_name = 'contact/contact.html'
    model = Contact
    fields = ['name', 'email', 'message', 'location']
    success_url = reverse_lazy('contact')
    
    # ✅ Add success_message back
    success_message = "Your message has been sent successfully!"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)  # ✅ Now this works

        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':  # ✅ Safer AJAX check
            return JsonResponse({'message': self.success_message})
        return response

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'errors': form.errors}, status=400)
        return super().form_invalid(form)
