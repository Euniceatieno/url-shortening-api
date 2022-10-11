from django.db import models
from django.utils import timezone

###############################################################
# Original URL Table
###############################################################


class OriginalUrl(models.Model):
    original_url_id = models.CharField(max_length=10, null=False, unique=True)
    original_url = models.CharField(max_length=500, null=False, unique=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)
