from django.views.generic import TemplateView


class AboutTemplateView(TemplateView):
    template_name = 'pages/about.html'


class ContactsTemplateView(TemplateView):
    template_name = 'pages/contacts.html'

class DeliveryTemplateView(TemplateView):
    template_name = 'pages/delivery.html'