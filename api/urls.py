from django.urls import path
from .views import (
    upload_audio,
    convert_audio_to_fir,
    get_fir_details
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Upload Audio API
    path('upload/', upload_audio, name='upload-audio'),

    # Convert Audio to FIR
    path('fir/<uuid:audio_id>/', convert_audio_to_fir,
         name='convert-audio-to-fir'),

    # Get FIR Details by Case ID
    path('fir/<str:case_id>/', get_fir_details, name='get-fir-details'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
