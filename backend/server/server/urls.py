from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from eTone import views as eTone_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'template_name': 'logout.html'}, name='logout'),
    url(r'^signup/$', eTone_views.signup, name='signup'),
    url(r'^upload/$', eTone_views.upload_file, name='upload'),
    url(r'^game/$', eTone_views.select_sound_game, name='game'),
    url(r'^stats/$', eTone_views.get_stats, name='stats'),
    url(r'^api/upload/(?P<typeID>[^/]?)/(?P<filename>[^/]+)$', eTone_views.FileUploadView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
