from django.contrib.auth import get_user_model
from django.db import models

from base.models import TimeStampedModel


User = get_user_model()


class Content(TimeStampedModel):
    id = models.CharField(primary_key=True, max_length=45)
    content = models.TextField(null=True, blank=True, default=None)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.id
