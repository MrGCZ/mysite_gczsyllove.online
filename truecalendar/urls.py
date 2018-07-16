from django.conf.urls import url
from . import views

urlpatterns=[
		url(r'^show-calendar/$',views.show_calendar,name="show_calendar"),
		url(r'^calendardetails/(?P<id>\d+)/$',views.show_details,name="show_details"),
		url(r'^add/$',views.add,name="add"),
		url(r'^show-calendar/delete/(?P<id>\d+)/$',views.delete,name="delete"),
		url(r'^show-calendar/finish/(?P<id>\d+)/$',views.finish,name="finish"),
		url(r'^todolist/$',views.todolish,name="todolish"),
		url(r'^todolist/finish/(?P<id>\d+)/$',views.finish,name="finish_tdl"),
		url(r'^finished/$',views.finished,name="finished"),
		url(r'^finished/delete/$',views.deletefinished,name="deletefinished"),
        ]
