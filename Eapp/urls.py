from django.urls import path
from .import views

urlpatterns = [

    path('cart/', views.cart, name='cart'),
    path('login_index2/', views.login_index1, name='login_index1'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cartlist/', views.cartlist, name='cartlist'),

    path('users/', views.users, name="users"),

    path('edit_item/<int:CartItem_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:CartItem_id>/',views. delete_item, name='delete_item'),

    path('dashboardmain/', views.dashboardmain, name="dashboardmain"),


    path('logout/', views.logout,name='logout'),
    path('add_to_cart/<int:product_id>/',  views.add_to_cart, name='add_to_cart'),

]