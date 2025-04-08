from pymongo import MongoClient
from datetime import datetime, time

# Establish a connection to the MongoDB database
client = MongoClient('localhost', 27017)
db = client['octofit_db']

class User:
    collection = db['users']

    @staticmethod
    def create_user(username, email, password):
        user = {
            "username": username,
            "email": email,
            "password": password,
            "date_joined": datetime.now()
        }
        return User.collection.insert_one(user)

    @staticmethod
    def find_user_by_email(email):
        return User.collection.find_one({"email": email})

class Team:
    collection = db['teams']

    @staticmethod
    def create_team(name, members):
        team = {
            "name": name,
            "members": members,
            "created_at": datetime.now()
        }
        return Team.collection.insert_one(team)

class Activity:
    collection = db['activities']

    @staticmethod
    def log_activity(user_id, activity_type, duration, calories_burned, date):
        # Convert date to datetime
        date_as_datetime = datetime.combine(date, time.min)
        activity = {
            "user_id": user_id,
            "activity_type": activity_type,
            "duration": duration,
            "calories_burned": calories_burned,
            "date": date_as_datetime
        }
        return Activity.collection.insert_one(activity)

class Leaderboard:
    collection = db['leaderboards']

    @staticmethod
    def update_leaderboard(team_id, total_points):
        return Leaderboard.collection.update_one(
            {"team_id": team_id},
            {"$set": {"total_points": total_points, "last_updated": datetime.now()}},
            upsert=True
        )

class Workout:
    collection = db['workouts']

    @staticmethod
    def create_workout(name, description, difficulty_level, duration):
        workout = {
            "name": name,
            "description": description,
            "difficulty_level": difficulty_level,
            "duration": duration
        }
        return Workout.collection.insert_one(workout)