from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    fhir_patient_id = models.PositiveBigIntegerField(
        null=True, blank=True, default=None
    )
    fhir_practitioner_id = models.PositiveBigIntegerField(
        null=True, blank=True, default=None
    )


class Client(models.Model):
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    redirect_uris = models.TextField()
    grant_type = models.CharField(max_length=32)
    scopes = models.TextField()

    def __str__(self) -> str:
        return self.client_id


class Attachment(models.Model):
    class AttachmentTypeChoice(models.TextChoices):
        IMAGE = "image"
        VIDEO = "video"
        DOCUMENT = "document"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attachment = models.FileField(upload_to="attachments/")
    attachment_type = models.CharField(
        max_length=255, choices=AttachmentTypeChoice.choices
    )
