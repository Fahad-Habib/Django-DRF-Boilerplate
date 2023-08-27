"""Mixins of the users app."""

from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OnlyUnauthenticatedMixin(AccessMixin):
    """Mixin to restrict access to views only for unauthenticated users."""

    def dispatch(self, request, *args, **kwargs):
        """Redirect authenticated users to home page."""
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
