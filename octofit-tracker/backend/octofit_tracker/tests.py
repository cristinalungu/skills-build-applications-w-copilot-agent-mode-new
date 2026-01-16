from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

class BasicModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(name='Test Activity', user_email='test@example.com', team='Test Team')
        self.assertEqual(activity.name, 'Test Activity')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=42)
        self.assertEqual(leaderboard.points, 42)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc', user_email='test@example.com')
        self.assertEqual(workout.name, 'Test Workout')

    def test_user_creation(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', email='testuser@example.com')
        self.assertEqual(user.email, 'testuser@example.com')
