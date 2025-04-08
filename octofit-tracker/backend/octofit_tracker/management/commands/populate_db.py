from django.core.management.base import BaseCommand # type: ignore
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Test data for users, teams, activities, leaderboards, and workouts
        users = [
            {"username": "user1", "email": "user1@example.com", "password": "password1", "date_joined": datetime(2025, 4, 8)},
            {"username": "user2", "email": "user2@example.com", "password": "password2", "date_joined": datetime(2025, 4, 8)},
        ]

        teams = [
            {"name": "Team A", "members": [], "created_at": datetime(2025, 4, 8)},
            {"name": "Team B", "members": [], "created_at": datetime(2025, 4, 8)},
        ]

        activities = [
            {"user_id": "user1_id", "activity_type": "Running", "duration": 30, "calories_burned": 300, "date": datetime(2025, 4, 8)},
            {"user_id": "user2_id", "activity_type": "Cycling", "duration": 45, "calories_burned": 450, "date": datetime(2025, 4, 8)},
        ]

        leaderboards = [
            {"team_id": "team_a_id", "total_points": 100, "last_updated": datetime(2025, 4, 8)},
            {"team_id": "team_b_id", "total_points": 200, "last_updated": datetime(2025, 4, 8)},
        ]

        workouts = [
            {"name": "Morning Yoga", "description": "A relaxing yoga session", "difficulty_level": "Beginner", "duration": 60},
            {"name": "HIIT", "description": "High-intensity interval training", "difficulty_level": "Advanced", "duration": 30},
        ]

        # Populate users
        for user in users:
            User.create_user(user['username'], user['email'], user['password'])

        # Populate teams
        for team in teams:
            Team.create_team(team['name'], team['members'])

        # Populate activities
        for activity in activities:
            Activity.log_activity(activity['user_id'], activity['activity_type'], activity['duration'], activity['calories_burned'], activity['date'])

        # Populate leaderboards
        for leaderboard in leaderboards:
            Leaderboard.update_leaderboard(leaderboard['team_id'], leaderboard['total_points'])

        # Populate workouts
        for workout in workouts:
            Workout.create_workout(workout['name'], workout['description'], workout['difficulty_level'], workout['duration'])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
