from django.utils.translation import ugettext
from rest_framework import serializers


class ErrorMessagesTranslationMixin(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            for error_type in self.fields[field].error_messages:
                self.fields[field].error_messages[error_type] = ugettext(
                    self.fields[field].error_messages[error_type]
                )
