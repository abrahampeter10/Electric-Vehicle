from django.urls import path
from . import views

urlpatterns = [
    path('plog',views.plog,name="plog"),

    path('Pindex',views.Pindex,name="Pindex"),
    # path('reg',views.reg,name="reg"),
    path('sreg',views.sreg,name="sreg"),
    path('slot',views.slot,name="slot"),
    path('sbook',views.sbook,name="sbook"),
    path('preg',views.preg,name="preg"),
    path('cadd',views.cadd,name="cadd"),
    path('mbook',views.mbook,name="mbook"),
    path('rreg',views.rreg,name="rreg"),
    path('statbook',views.statbook,name="statbook"),
    path('mveh',views.mveh,name="mveh"),
    



    

   
]


