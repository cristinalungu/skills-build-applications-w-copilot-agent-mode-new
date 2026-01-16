from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com'),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com'),
            User.objects.create_user(username='batman', email='batman@dc.com'),
            User.objects.create_user(username='superman', email='superman@dc.com'),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com'),
        ]

        # Activities
        Activity.objects.create(name='Run', user_email='ironman@marvel.com', team='Marvel')
        Activity.objects.create(name='Swim', user_email='cap@marvel.com', team='Marvel')
        Activity.objects.create(name='Fly', user_email='superman@dc.com', team='DC')
        Activity.objects.create(name='Fight', user_email='batman@dc.com', team='DC')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 50 pushups', user_email='ironman@marvel.com')
        Workout.objects.create(name='Yoga', description='30 min yoga', user_email='wonderwoman@dc.com')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
