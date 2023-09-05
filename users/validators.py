"""Validators for users app."""

from django.core.validators import RegexValidator


class HandleValidator(RegexValidator):
    """Custom validator for user handle."""

    def __call__(self, value):
        """Customize error messages."""
        if value[0] == '_' or value[-1] == '_':
            self.message = 'Handle cannot start or end with underscore (_)'
        elif value[0].isdigit():
            self.message = 'Handle cannot start with a number'
        else:
            self.message = 'Handle can only contain alphabets, numbers or underscore (_)'
        return super().__call__(value)
