from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
     
    path('',views.home,name='home'),
    path('show_record',views.show_record,name='show_record'),
    path('show_record/details/<int:id>',views.details,name='details'),
    path('login',views.login_user,name='login'),
    path('signup',views.signup_user,name='signup'),
    path('search',views.search,name='search'),
    path('add_details',views.add_details,name='add_details'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('hosinfo',views.hosinfo,name='hosinfo'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('details_text',views.details_text,name='details_text'),
    path('details_csv',views.details_csv,name='details_csv'),
    path('details_pdf',views.details_pdf,name='details_pdf'),
    path('detail_text/<int:id>',views.detail_text,name='detail_text'),
]
