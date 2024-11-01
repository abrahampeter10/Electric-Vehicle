from django.urls import path
from . import views

urlpatterns = [
    path('creg',views.creg,name="creg"),
    path('clog',views.clog,name="clog"),
    path('chome',views.chome,name="chome"),
    path('add',views.add,name="add"),
    path('cprofile',views.cprofile,name="cprofile"),
    path('view',views.view,name="view"),
    path('select<int:sid>',views.select,name="select"),
    path('cdel<int:id>',views.cdel,name="cdel"),
    path('update<int:tid>',views.update,name="update"),
    path('edit<int:etid>',views.edit,name="edit"),
    path('booking<str:pk>',views.booking,name="booking"),
    path('approved<int:id>',views.approved,name="approved"),
    path('reject<int:id>',views.reject,name="reject"),




    









    
]


