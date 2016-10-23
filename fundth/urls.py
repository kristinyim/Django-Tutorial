from django.conf.urls import patterns, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # ex: /fundth/
    url(r'^$', views.index, name='index'),
    url(r'^organizationLogin/$', views.organizationLogin, name='organizationLogin'),
  	url(r'^businessLogin/$', views.businessLogin, name='businessLogin'),
  	url(r'^businessNewAccount/$', views.businessNewAccount, name='businessNewAccount'),
  	url(r'^organizationNewAccount/$', views.organizationNewAccount, name='organizationNewAccount'),
]
