from django.db import models
from django.utils import timezone

from url_shortening_app.utils import generate_random_string


###############################################################
# Original URL Table
###############################################################


class OriginalUrl(models.Model):
    original_url_id = models.CharField(
        primary_key=True,
        max_length=5,
        null=False,
        default=generate_random_string(),
    )
    original_url = models.CharField(max_length=500, null=False)
    date_created = models.DateTimeField(default=timezone.now, null=True)
