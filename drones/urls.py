from django.urls import path
from drones import views
from drones.views import PilotList, PilotDetail, CompetitionList, CompetitionDetails

urlpatterns = [
    path('drone-categories/', views.DroneCategoryList.as_view(),
         name=views.DroneCategoryList.name),
    path('drone-categories/<pk>/', views.DroneCategoryDetail.as_view(),
         name=views.DroneCategoryDetail.name),

    path('drones/', views.DroneList.as_view(),
         name=views.DroneList.name),
    path('drone/<pk>/', views.DroneDetail.as_view(),
         name=views.DroneDetail.name),

    path('pilots/', views.PilotList.as_view(),
          name=PilotList.name),
    path('pilots/<pk>/', views.PilotDetail.as_view(),
         name=PilotDetail.name),

    path('competitions/', views.CompetitionList.as_view(),
         name=CompetitionList.name),
    path('competition/<pk>/', views.CompetitionDetails.as_view(),
         name=CompetitionDetails.name),

    path('api-root/',views.ApiRoot.as_view(),
         name=views.ApiRoot.name)
]