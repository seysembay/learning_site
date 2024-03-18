from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
import django_rq
from .tasks import send_to_admin, send_to_user


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/course/list'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        django_rq.enqueue(send_to_admin, name=name, email=email, message=message)
        django_rq.enqueue(send_to_user, email=email, message=message)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
