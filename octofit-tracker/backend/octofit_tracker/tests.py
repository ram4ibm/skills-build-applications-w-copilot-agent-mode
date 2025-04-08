from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class OctoFitTrackerTests(APITestCase):

    def test_create_user(self):
        response = self.client.post('/users/', {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
            "date_joined": "2025-04-08T00:00:00Z"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user(self):
        User.create_user("testuser", "testuser@example.com", "password123")
        response = self.client.get('/users/testuser@example.com/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], "testuser@example.com")

    def test_create_team(self):
        user_id = User.create_user("testuser", "testuser@example.com", "password123").inserted_id
        response = self.client.post('/teams/', {
            "name": "Test Team",
            "members": [str(user_id)],
            "created_at": "2025-04-08T00:00:00Z"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_log_activity(self):
        user_id = User.create_user("testuser", "testuser@example.com", "password123").inserted_id
        response = self.client.post('/activities/', {
            "user_id": str(user_id),
            "activity_type": "Running",
            "duration": 30,
            "calories_burned": 300,
            "date": "2025-04-08T00:00:00Z"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_leaderboard(self):
        team_id = Team.create_team("Test Team", []).inserted_id
        response = self.client.get(f'/leaderboards/{team_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_workout(self):
        response = self.client.post('/workouts/', {
            "name": "Morning Yoga",
            "description": "A relaxing yoga session",
            "difficulty_level": "Beginner",
            "duration": 60
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
