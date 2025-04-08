from datetime import datetime

def get_test_data():
    return {
        "users": [
            {"username": "user1", "email": "user1@example.com", "password": "password1", "date_joined": datetime(2025, 4, 8)},
            {"username": "user2", "email": "user2@example.com", "password": "password2", "date_joined": datetime(2025, 4, 8)},
        ],
        "teams": [
            {"name": "Team A", "members": [], "created_at": datetime(2025, 4, 8)},
            {"name": "Team B", "members": [], "created_at": datetime(2025, 4, 8)},
        ],
        "activities": [
            {"user_id": "user1_id", "activity_type": "Running", "duration": 30, "calories_burned": 300, "date": datetime(2025, 4, 8)},
            {"user_id": "user2_id", "activity_type": "Cycling", "duration": 45, "calories_burned": 450, "date": datetime(2025, 4, 8)},
        ],
        "leaderboards": [
            {"team_id": "team_a_id", "total_points": 100, "last_updated": datetime(2025, 4, 8)},
            {"team_id": "team_b_id", "total_points": 200, "last_updated": datetime(2025, 4, 8)},
        ],
        "workouts": [
            {"name": "Morning Yoga", "description": "A relaxing yoga session", "difficulty_level": "Beginner", "duration": 60},
            {"name": "HIIT", "description": "High-intensity interval training", "difficulty_level": "Advanced", "duration": 30},
        ],
    }
