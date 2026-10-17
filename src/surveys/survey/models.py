from django.db import models

class Survey(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(null=False)
    owner_id = models.BigIntegerField(null=False)
    created_date = models.DateTimeField(auto_now_add=True, null=False)
    updated_date = models.DateTimeField(auto_now=True, null=False)
    is_deleted = models.BooleanField(default=False, null=False)

