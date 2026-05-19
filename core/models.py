from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords
from safedelete.models import SOFT_DELETE_CASCADE


class HistoricalModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
