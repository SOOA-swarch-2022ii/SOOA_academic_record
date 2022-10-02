from django.db import models

class Academic_record(models.Model):

    id = models.AutoField(primary_key = True)
    student_id = models.CharField(max_length = 20)
    pensum = models.TextField(null=True)
    academic_history = models.TextField(null=True)
    current_courses = models.TextField(null=True)
    papa = models.FloatField()
    papi = models.FloatField()
    status = models.BooleanField()
    campus = models.CharField(max_length = 20)
    faculty = models.CharField(max_length = 50)
    career = models.CharField(max_length = 50)

    class Meta:
        app_label = 'SOOA_academic_record_ms'