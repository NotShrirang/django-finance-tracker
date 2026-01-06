import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finance_tracker.settings")
django.setup()

from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

email = "track.my.rupee.app@gmail.com"
try:
    user = User.objects.get(email=email)
    print(f"User found: {user.username}")
    
    social_accounts = SocialAccount.objects.filter(user=user)
    if social_accounts.exists():
        print(f"Social accounts found: {[sa.provider for sa in social_accounts]}")
    else:
        print("No social accounts found for this user.")
        
except User.DoesNotExist:
    print(f"User with email {email} does not exist.")
