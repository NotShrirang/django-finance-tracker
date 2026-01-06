import os
import django
from django.db.models import Count

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finance_tracker.settings")
django.setup()

from django.contrib.auth.models import User

# Find emails that appear more than once
duplicates = User.objects.values('email').annotate(count=Count('email')).filter(count__gt=1)

print("Duplicate Emails found:")
for entry in duplicates:
    print(f"Email: '{entry['email']}' - Count: {entry['count']}")
    users = User.objects.filter(email=entry['email'])
    for u in users:
        print(f"  - User: {u.username} (ID: {u.id})")

if not duplicates:
    print("No duplicate emails found.")
