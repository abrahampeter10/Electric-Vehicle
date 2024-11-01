
from django.urls import path
from . import views

urlpatterns = [
    
    path('MarketReg',views.MarketReg,name="MarketReg"),
    path('Mlogin',views.Mlogin,name="Mlogin"),
    path('CmpUser',views.CmpUser,name="CmpUser"),
    path('Addvehicle',views.Addvehicle,name="Addvehicle"),
    path('MProfile',views.MProfile,name="MProfile"),
    path('Medit',views.Medit,name="Medit"),
    path('Viewvehicle',views.Viewvehicle,name="Viewvehicle"),
    path('Viewdetails<int:xid>',views.Viewdetails,name="Viewdetails"),
    path('Mupdate<int:Mid>',views.Mupdate,name="Mupdate"),
    path('mdel<int:id>',views.mdel,name="mdel"),
    path('Mbookings<int:mk>',views.Mbookings,name="Mbookings"),
    path('mapproved<int:id>',views.mapproved,name="mapproved"),
    path('mreject<int:id>',views.mreject,name="mreject"),



    


   

   
]