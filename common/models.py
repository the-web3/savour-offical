import uuid
from django.db import models

BoolYesOrNoSelect = [
    (x, x) for x in ["Yes", "No"]
]

class BaseModel(models.Model):
    uuid = models.CharField(
        max_length=100,
        blank=True,
        unique=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, db_index=True
    )

    class Meta:
        abstract = True

    @property
    def UUID(self):
        return uuid.UUID(hex=self.uuid)

    def generate_uuid(self):
        self.uuid = uuid.uuid4().hex

    def save(self, *args, **kw):
        if not self.uuid:
            self.generate_uuid()
        return super(BaseModel, self).save(
            *args, **kw
        )


class DecField(models.DecimalField):
    def __init__(self, **kw):
        kw.setdefault("max_digits", 65)
        kw.setdefault("decimal_places", 30)
        super(DecField, self).__init__(**kw)


class IdField(models.CharField):
    def __init__(self, **kwargs):
        kwargs.setdefault("max_length", 100)
        super(IdField, self).__init__(**kwargs)
