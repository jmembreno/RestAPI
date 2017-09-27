"""dogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dog.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/breeds/$',BreedList.as_view(), name='breed_list_api' ),
    url(r'^api/breeds/(?P<id>[0-9]+)$',BreedDetail.as_view(), name='breed_detail_api' ),
    url(r'^api/dogs/$',DogList.as_view(), name='dog_list_api' ),
    url(r'^api/dogs/(?P<id>[0-9]+)$',DogDetail.as_view(), name='dog_detail_api' ),



]
