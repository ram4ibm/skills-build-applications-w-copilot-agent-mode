from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserList(APIView):
    def get(self, request):
        users = list(User.collection.find())
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            User.create_user(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get(self, request, email):
        user = User.find_user_by_email(email)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class TeamList(APIView):
    def get(self, request):
        teams = list(Team.collection.find())
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            Team.create_team(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamDetail(APIView):
    def get(self, request, team_id):
        team = Team.collection.find_one({"_id": team_id})
        if team:
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class ActivityList(APIView):
    def get(self, request):
        activities = list(Activity.collection.find())
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            Activity.log_activity(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityDetail(APIView):
    def get(self, request, activity_id):
        activity = Activity.collection.find_one({"_id": activity_id})
        if activity:
            serializer = ActivitySerializer(activity)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class LeaderboardList(APIView):
    def get(self, request):
        leaderboards = list(Leaderboard.collection.find())
        serializer = LeaderboardSerializer(leaderboards, many=True)
        return Response(serializer.data)

class LeaderboardDetail(APIView):
    def get(self, request, team_id):
        leaderboard = Leaderboard.collection.find_one({"team_id": team_id})
        if leaderboard:
            serializer = LeaderboardSerializer(leaderboard)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class WorkoutList(APIView):
    def get(self, request):
        workouts = list(Workout.collection.find())
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            Workout.create_workout(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutDetail(APIView):
    def get(self, request, workout_id):
        workout = Workout.collection.find_one({"_id": workout_id})
        if workout:
            serializer = WorkoutSerializer(workout)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
