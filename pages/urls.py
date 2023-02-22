from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name = 'login'),
    path('home.html', views.home, name='home'),
    path('Active-inactive.html', views.Active, name='Active'),
    path('department.html', views.Department, name='Department'),
    path('edit.html/<int:ID>/', views.edit, name='edit'),
    path('help.html', views.help, name='help'),
    path('search.html', views.searchPage, name='search'),
    path('search', views.search, name='searchLive'),
    path('search.html/<str:ID>', views.search, name='searchPage'),
    path('Add.html', views.Add_student, name='add'),
    path('Update/<int:ID>/',views.Update,name='update'),
    path('Logout',views.LogoutPage,name='Logout'),    
    path('delete/<int:Id>/',views.deleteStudent,name='delete'),


]