from django.db import models
from django.contrib.postgres.fields import ArrayField

class Professoral_record(models.Model):

    id = models.AutoField(primary_key = True)
    professor_id = models.CharField(max_length = 20)
    approved_subjects = ArrayField(
            models.CharField(max_length = 20, blank=True)
        )
    course_record = ArrayField(
            models.CharField(max_length = 20, blank=True)
        )
    campus = models.CharField(max_length = 20)
    faculty = models.CharField(max_length = 50)

    class Meta:
        app_label = 'SOOA_academic_record_ms'