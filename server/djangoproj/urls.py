from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from djangoapp import views as dj_views

# NEW: ovo dodajemo da Django sigurno servira /static/* iz STATICFILES_DIRS
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),

    # Statične HTML stranice (frontend/static)
    path('', TemplateView.as_view(template_name='home.html')),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('contact/', TemplateView.as_view(template_name='Contact.html')),

    # REACT stranice (frontend/build/index.html)
    path('login/', TemplateView.as_view(template_name='index.html')),
    path('register/', TemplateView.as_view(template_name='index.html')),
    path('dealers/', TemplateView.as_view(template_name='index.html')),

    # Podrška i bez završne kose crte (nije obavezno)
    path('register', TemplateView.as_view(template_name='index.html')),
    path('dealers', TemplateView.as_view(template_name='index.html')),

    # Backend JSON login (bez kose crte)
    path('login', dj_views.login_user, name='login'),

    # Django app prefiks (backend: /djangoapp/login, /djangoapp/logout, /djangoapp/register)
    path('djangoapp/', include('djangoapp.urls')),
]

# NEW: ovo ubaci NA DNO — osigurava da /static/* radi iz STATICFILES_DIRS
urlpatterns += staticfiles_urlpatterns()
