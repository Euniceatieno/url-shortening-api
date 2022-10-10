from django.db import models
from django.utils import timezone
import uuid


###############################################################
# Original URL Table
###############################################################


class OriginalUrl(models.Model):
    original_url_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    original_url = models.CharField(max_length=500, null=False)
    date_created = models.DateTimeField(default=timezone.now, null=True)
