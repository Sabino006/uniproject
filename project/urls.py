"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home,create_client,criar_cliente,criar_admin,create_admin,logar,logando,dashboard,dashboard_admin,logouts,newpass,changePassword,create_pedido,criar_pedido,view_pedidos,view_usuarios


urlpatterns = [
    path('', home),
    path('create/cliente/', create_client),
    path('create/admin/', create_admin),
    path('create/pedido/', create_pedido),
    path('criar/admin/', criar_admin),
    path('criar/cliente/', criar_cliente),
    path('criar/pedido/', criar_pedido),
    path('login/', logar),
    path('logando/', logando),
    path('dashboard/', dashboard),
    path('dashboard/admin/', dashboard_admin),
    path('logouts/', logouts),
    path('newpass/', newpass),
    path('password/', changePassword),
    path('view/pedidos/', view_pedidos),
    path('view/usuarios/', view_usuarios),
]