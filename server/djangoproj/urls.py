from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from djangoapp import views as dj_views  # /login (backend bez kos crte)

urlpatterns = [
    path('admin/', admin.site.urls),

    # statične HTML stranice
    path('', TemplateView.as_view(template_name='home.html')),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('contact/', TemplateView.as_view(template_name='Contact.html')),

    # React stranice iz frontend/build/index.html
    path('login/', TemplateView.as_view(template_name='index.html')),
    path('register/', TemplateView.as_view(template_name='index.html')),

    # backend login JSON (bez završne kos crte)
    path('login', dj_views.login_user, name='login'),

    # app prefiks za /djangoapp/login, /djangoapp/logout, /djangoapp/register
    path('djangoapp/', include('djangoapp.urls')),
]
