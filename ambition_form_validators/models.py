from django.conf import settings

if settings.APP_NAME == 'ambition_form_validators':
    from ambition_form_validators import models
