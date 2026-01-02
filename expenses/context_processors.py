from .models import UserProfile

def currency_symbol(request):
    """Provides the user's preferred currency symbol to all templates."""
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            return {'currency_symbol': profile.currency}
        except UserProfile.DoesNotExist:
            return {'currency_symbol': '₹'}
    return {'currency_symbol': '₹'}
