from django.conf.urls import url, include
from users import views

urlpatterns = [
#	url(r'^staff/', views.staff)
#	url(r'^users/', views.form),
	url(r'^login/', views.user_login),
	url(r'^logout/', views.user_logout),
	url(r'^inornot/', views.inorout),
	url(r'^register/', views.register),
]