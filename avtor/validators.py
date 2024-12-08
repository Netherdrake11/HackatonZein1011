import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                _("Пароль должен содержать хотя бы одну заглавную букву."),
                code='password_no_upper',
            )
        if not re.search(r'[!@#$%^&*()]', password):
            raise ValidationError(
                _("Пароль должен содержать хотя бы один специальный символ."),
                code='password_no_special',
            )

    def get_help_text(self):
        return _("Пароль должен содержать хотя бы одну заглавную букву и один специальный символ.")