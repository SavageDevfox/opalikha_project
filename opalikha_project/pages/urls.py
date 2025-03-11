from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('contacts/', views.ContactsTemplateView.as_view(), name='contacts'),
    path('delivery/', views.DeliveryTemplateView.as_view(), name='delivery')
]
