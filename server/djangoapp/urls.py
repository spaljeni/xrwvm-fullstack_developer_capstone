from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Static pages (from frontend/static)
    path('', TemplateView.as_view(template_name='home.html')),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('contact/', TemplateView.as_view(template_name='Contact.html')),

    # React login page (served from frontend/build -> index.html)
    path('login/', TemplateView.as_view(template_name='index.html')),

    # Django app routes (includes /login without trailing slash -> views.login_user)
    path('', include('djangoapp.urls')),
]