"""Views of the profile app."""

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from users.profile.forms import UserProfileForm

User = get_user_model()


class UserProfileView(DetailView):
    """User Profile View."""

    template_name = 'user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        """Return User object."""
        try:
            user = User.objects.get(handle=self.kwargs['handle'])
            return user
        except User.DoesNotExist:
            raise Http404


class UserProfileEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """User Profile Edit View."""

    template_name = 'edit_user_profile.html'
    form_class = UserProfileForm
    success_message = 'Profile updated successfully.'

    def get_success_url(self):
        """Return success url."""
        return reverse_lazy('user_profile', kwargs={'handle': self.request.user.handle})

    def get_object(self, queryset=None):
        """Allow users to only change their own profile."""
        try:
            user = User.objects.get(handle=self.kwargs['handle'])
            if user == self.request.user:
                return user
            else:
                raise Http404
        except User.DoesNotExist:
            raise Http404
