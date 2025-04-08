from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# Register models in the admin interface
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'activity_type', 'duration', 'calories_burned', 'date')

class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('team_id', 'total_points', 'last_updated')

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty_level', 'duration')

# Remove registration of pymongo-based models
# Pymongo models cannot be registered in the Django admin interface
# admin.site.register(User, UserAdmin)
# admin.site.register(Team, TeamAdmin)
# admin.site.register(Activity, ActivityAdmin)
# admin.site.register(Leaderboard, LeaderboardAdmin)
# admin.site.register(Workout, WorkoutAdmin)
