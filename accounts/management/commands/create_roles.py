from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from accounts.constants import Roles

class Command(BaseCommand):
    help = 'Create default user roles'

    def handle(self, *args, **options):
        for role_name, _ in Roles.CHOICES:
            group, created = Group.objects.get_or_create(name=role_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Role "{role_name}" created'))
            else:
                self.stdout.write(self.style.WARNING(f'Role "{role_name}" already exists'))
