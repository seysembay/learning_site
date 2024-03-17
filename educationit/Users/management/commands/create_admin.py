from django.core.management.base import BaseCommand, CommandError
from Users.models import CustomUser


class Command(BaseCommand):
    help = "Fill db with test data"

    def handle(self, *args, **options):
        try:
            CustomUser.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        except:
            self.stdout.write(
                self.style.SUCCESS('Already Exists')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('Done')
            )
