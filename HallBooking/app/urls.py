from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('login/',views.login,name = 'login'),
    path('home/',views.home, name = 'home'),
    path('about/',views.about,name = 'about'),
    path('search/',views.search,name='search'),
    path('hallbook',views.hallbook,name = 'hallbook'),
    path('adminhm/',views.adminhm,name='adminhm'),
    path('staff_login/',views.staff_login,name='staff_login'),
    path('adminstf/',views.adminstf,name='adminstf'),
    path('adviewuser/',views.viewuser,name='adviewuser'),
    path('adviewbook/',views.viewbook,name='adviewbook'),
    path('download/<str:id>',views.download,name = 'download'),
    path('download1/<str:id>',views.download1,name = 'download1'),
    path('delete/<str:id>',views.delete_book,name = 'delete_book'),
    path('update/<str:id>',views.update_book,name = 'update_book'),
    path('approve/',views.approve,name='approve'),
    path('feedback/',views.feedback1,name='feedback'),

]