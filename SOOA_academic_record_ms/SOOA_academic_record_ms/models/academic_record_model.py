from django.db import models
from django.contrib.postgres.fields import ArrayField

class Academic_record(models.Model):

    id = models.AutoField(primary_key = True)
    student_id = models.CharField(max_length = 20)
    subjects_pending = ArrayField(
            models.CharField(max_length = 20, blank=True)
        )
    subjects_record = ArrayField(
            models.CharField(max_length = 20, blank=True)
        )
    papa = models.FloatField()
    papi = models.FloatField()
    status = models.BooleanField()
    campus = models.CharField(max_length = 20)
    faculty = models.CharField(max_length = 50)
    career = models.CharField(max_length = 50)

    class Meta:
        app_label = 'SOOA_academic_record_ms'