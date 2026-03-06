from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User(email='captain@marvel.com', name='Captain America', team='marvel'),
            User(email='batman@dc.com', name='Batman', team='dc'),
            User(email='superman@dc.com', name='Superman', team='dc'),
        ]
        for user in users:
            user.save()

        # Add users to teams
        marvel.members.add(users[0], users[1])
        dc.members.add(users[2], users[3])

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, date='2026-03-06')
        Activity.objects.create(user=users[1], type='cycle', duration=45, date='2026-03-06')
        Activity.objects.create(user=users[2], type='swim', duration=25, date='2026-03-06')
        Activity.objects.create(user=users[3], type='walk', duration=60, date='2026-03-06')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='medium')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
