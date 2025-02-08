from django.db import models
import uuid


class Audio(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    audio_file = models.FileField(upload_to='audio_files/')
    transcribed_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Audio {self.id}"


class FIR(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    case_id = models.CharField(max_length=20, unique=True)
    # ✅ Fix: Ensure it's a ForeignKey
    audio = models.ForeignKey(
        Audio, on_delete=models.SET_NULL, null=True, blank=True)
    original_text = models.TextField()
    fir_text = models.TextField()
    fir_pdf = models.FileField(upload_to='fir_pdfs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.case_id:
            self.case_id = f"CASE-{uuid.uuid4().hex[:10].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"FIR {self.case_id}"
