from django.conf.urls import url, include
from west import views

urlpatterns = [
#	url(r'^staff/', views.staff)
#	url(r'^form/', views.form),
	url(r'^investigate/', views.investigate),
]