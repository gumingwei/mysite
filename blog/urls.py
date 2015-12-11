from django.conf.urls import include, url
from blog.views import archive

urlpatterns = [
    url(r'^$', archive),
]
