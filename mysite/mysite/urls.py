"""mysite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^model/(\d+)$', views.model),
    url(r'^save_user_profile/$', views.save_user_profile,name='save_user_profile'),
    url(r'^api/', include('api.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^get_strategy_list/', include('get_strategy_list.urls')),
    url(r'^monte/', views.show_monte_carlo_result),
    url(r'^admin/', admin.site.urls),
    url(r'^create_portfolio/$',views.create_portfolio,name="create_portfolio")
]
