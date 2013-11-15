from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from sessions.views import SessionView
from users.views import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',

    # Authentication
    url(r'^session/$', SessionView.as_view()),

    # API
    url(r'api/', include(router.urls)),

    url(r'^admin/', include(admin.site.urls)),
    # Application
    url(r'^$', TemplateView.as_view(template_name='application.html'))
)
