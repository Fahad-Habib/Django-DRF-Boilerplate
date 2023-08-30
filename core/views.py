"""Views of the core app."""

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Home Page View."""

    template_name = 'home.html'
