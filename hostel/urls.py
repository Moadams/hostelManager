from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginPage, name = 'loginPage'),
    path('logout/',views.logoutUser, name = 'logoutUser'),
    
    path('dashboard/',views.homePage, name = 'homePage'),
    path('login/',views.loginPage, name = 'loginPage'),
    path('rooms/',views.rooms, name = 'rooms'),
    path('workers/',views.workers, name = 'workers'),
    path('occupants/',views.occupants, name = 'occupants'),

    path('rooms/add-room/',views.addRoom, name = 'addRoom'),
    path('workers/add-worker/',views.addWorker, name = 'addWorker'),
    path('occupants/add-occupant/',views.addOccupant, name = 'addOccupant'),

    path('occupants/update-occupant/<str:pk>', views.updateOccupant, name = 'updateOccupant'),
    path('rooms/update-room/<str:pk>', views.updateRoom, name = 'updateRoom'),
    path('workers/update-worker/<str:pk>', views.updateWorker, name = 'updateWorker'),

    path('occupant/delete/<str:pk>', views.deleteOccupant, name = 'deleteOccupant'),
    path('worker/delete/<str:pk>', views.deleteWorker, name = 'deleteWorker'),
    path('room/delete-room/<str:pk>',views.deleteRoom, name='deleteRoom')
]