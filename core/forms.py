"""Forms of the core app."""

from core.constants import PLACE_HOLDERS


class BaseForm:
    """Base form class."""

    def change_style(self):
        """Add styling to the fields."""
        for field in self.fields:
            if field in PLACE_HOLDERS:
                self.fields[field].widget.attrs['class'] = 'form-control'
                self.fields[field].widget.attrs['placeholder'] = PLACE_HOLDERS[field]
                self.fields[field].label = ''
                self.fields[field].help_text = None
