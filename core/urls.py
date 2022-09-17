from django.urls import path
from core import views

urlpatterns = [

    path('login/', views.login, name='manager-login'),
    path('create-account/', views.login, name='manager-create-account'),
    path('dashboard/', views.dashboard, name='manager-dashboard'),
    path('artists/', views.artists, name='artists'),
    path('newartist/', views.new_artist, name='new-artist'),
    path('studios/', views.studios, name='studios'),
    path('newstudio/', views.new_studio, name='new-studio'),
    path('updatestudio/<str:pk>', views.update_studio, name='update-studio'),
    path('deletestudio/', views.delete_studio, name='delete-studio'),
    path('albums/', views.albums, name='albums'),
    path('studiosessions/', views.studio_sessions, name='studio-sessions'),
    path('viewartist/<str:pk>', views.view_artist, name='view-artist'),
    path('deleteartist/', views.delete_artist, name='delete-artist'),
    path('updateartist/<str:pk>', views.update_artist, name='update-artist'),
    path('newstudiosession/', views.add_studio_sessions, name='add-studio-sessions'),
    path('addalbum/', views.add_album, name='add-album'),
    path('deletealbum/', views.delete_album, name='delete-album'),
    path('updatealbum/<str:pk>', views.update_album, name='update-album'),
    path('shows-tours/', views.show_tour, name='show-tour'),
    path('addshows-tours/', views.add_show_tour, name='add-show-tour'),
    path('updateshows-tours/<str:pk>', views.update_show, name='update-show'),
    path('payroll/', views.payroll, name='payroll'),
    path('logout/', views.logout, name='logout'),
    path('addpayroll/', views.add_payroll, name='add-payroll'),
    path('updatepayroll/<str:pk>', views.update_payroll, name='update-payroll'),
    path('updatesession/<str:pk>', views.update_session, name='update-session'),
    path('deletesession/<str:pk>', views.delete_session, name='delete-session'),
    path('viewalbum/<str:pk>', views.view_album, name='view-album'),
    path('deletepayroll/<str:pk>', views.delete_payroll, name='delete-payroll'),

]
