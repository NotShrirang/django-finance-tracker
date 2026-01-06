import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finance_tracker.settings")
django.setup()

from django.contrib.auth.models import User
from expenses.forms import ProfileUpdateForm

email = "track.my.rupee.app@gmail.com"
try:
    user = User.objects.get(email=email)
    form = ProfileUpdateForm(instance=user)
    
    print(f"Checking form for user: {user.username}")
    print(f"Auth Email Disabled: {form.fields['auth_email'].disabled}")
    print(f"First Name Disabled: {form.fields['first_name'].disabled}")
    
    # Check if widget attrs have it
    print(f"Auth Email Widget Attrs: {form.fields['auth_email'].widget.attrs}")

except User.DoesNotExist:
    print("User not found")
except Exception as e:
    print(f"Error: {e}")
