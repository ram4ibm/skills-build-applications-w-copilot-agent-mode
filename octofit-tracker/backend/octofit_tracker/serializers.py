from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    date_joined = serializers.DateTimeField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField())
    created_at = serializers.DateTimeField()

class ActivitySerializer(serializers.Serializer):
    user_id = serializers.CharField()
    activity_type = serializers.CharField(max_length=50)
    duration = serializers.IntegerField()  # in minutes
    calories_burned = serializers.FloatField()
    date = serializers.DateTimeField()

class LeaderboardSerializer(serializers.Serializer):
    team_id = serializers.CharField()
    total_points = serializers.IntegerField()
    last_updated = serializers.DateTimeField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    difficulty_level = serializers.CharField(max_length=50)
    duration = serializers.IntegerField()  # in minutes
