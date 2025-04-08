from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime

def test_models():
    # Test User model
    print("Testing User model...")
    user_id = User.create_user("testuser", "testuser@example.com", "password123")
    print("User created with ID:", user_id.inserted_id)
    user = User.find_user_by_email("testuser@example.com")
    print("User found:", user)

    # Test Team model
    print("\nTesting Team model...")
    team_id = Team.create_team("Test Team", [user_id.inserted_id])
    print("Team created with ID:", team_id.inserted_id)

    # Test Activity model
    print("\nTesting Activity model...")
    activity_id = Activity.log_activity(
        user_id.inserted_id, "Running", 30, 300, datetime.now().date()
    )
    print("Activity logged with ID:", activity_id.inserted_id)

    # Test Leaderboard model
    print("\nTesting Leaderboard model...")
    leaderboard_result = Leaderboard.update_leaderboard(team_id.inserted_id, 100)
    print("Leaderboard updated:", leaderboard_result.modified_count)

    # Test Workout model
    print("\nTesting Workout model...")
    workout_id = Workout.create_workout(
        "Morning Yoga", "A relaxing yoga session", "Beginner", 60
    )
    print("Workout created with ID:", workout_id.inserted_id)

if __name__ == "__main__":
    test_models()
