from django.conf.urls import url, include
from west import views

urlpatterns = [
	url(r'^$', views.first_page)
]