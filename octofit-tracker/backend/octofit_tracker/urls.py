"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import views

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': request.build_absolute_uri('users/'),
        'teams': request.build_absolute_uri('teams/'),
        'activities': request.build_absolute_uri('activities/'),
        'leaderboards': request.build_absolute_uri('leaderboards/'),
        'workouts': request.build_absolute_uri('workouts/'),
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path("admin/", admin.site.urls),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<str:email>/', views.UserDetail.as_view(), name='user-detail'),
    path('teams/', views.TeamList.as_view(), name='team-list'),
    path('teams/<str:team_id>/', views.TeamDetail.as_view(), name='team-detail'),
    path('activities/', views.ActivityList.as_view(), name='activity-list'),
    path('activities/<str:activity_id>/', views.ActivityDetail.as_view(), name='activity-detail'),
    path('leaderboards/', views.LeaderboardList.as_view(), name='leaderboard-list'),
    path('leaderboards/<str:team_id>/', views.LeaderboardDetail.as_view(), name='leaderboard-detail'),
    path('workouts/', views.WorkoutList.as_view(), name='workout-list'),
    path('workouts/<str:workout_id>/', views.WorkoutDetail.as_view(), name='workout-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
