from django.conf.urls import url
import views



urlpatterns=[
        url(r"^$",views.index,name="index"),
        url(r"^play",views.inInstance,name="inInstance"),
        url(r"^instance/(?P<instanceID>\w+)", views.instanceDetail.as_view()),
        url(r"^people/(?P<instanceID>\w+)",views.peopleByInstance.as_view()),
        url(r"^score/(?P<personPk>\d+)",views.ScoreUpdate.as_view()),
       ]
