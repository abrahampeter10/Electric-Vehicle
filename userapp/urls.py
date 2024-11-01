from django.urls import path
from . import views

urlpatterns = [
    path('ureg',views.ureg,name="ureg"),
    path('ulogin',views.ulogin,name="ulogin"),
    path('uprofile',views.uprofile,name="uprofile"),
    path('uhome',views.uhome,name="uhome"),
    path('ueditprofile',views.ueditprofile,name="ueditprofile"),
    path('orders',views.orders,name="orders"),
    path('stations',views.stations,name="stations"),
    path('udetails<int:dtid>',views.udetails,name="udetails"),
    path('renting',views.renting,name="renting"),
    path('viewstations<int:vsid>',views.viewstations,name="viewstations"),
    path('Avstations<str:id>',views.Avstations,name="Avstations"),
    path('viewvehicle<int:vhid>',views.viewvehicle,name="viewvehicle"),
    path('Avehicles<str:id>',views.Avehicles,name="Avehicles"),
    path('vdetails<int:vtid>',views.vdetails,name="vdetails"),
    # path('checkout<str:id>',views.checkout,name="checkout"),
    path('checkout',views.checkout,name="checkout"),

    path('spay<int:id>',views.spay,name="spay"),
    path('vpay<int:id>',views.vpay,name="vpay"),


    # path('dpay<int:uid>',views.dpay,name="dpay"),
    path('bdetails',views.bdetails,name="bdetails"),
    # path('uuserpay',views.uuserpay,name="uuserpay"),
    path('cubook<int:id>',views.cubook,name="cubook"),




]


