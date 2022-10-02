from django.db import models

class Professoral_record(models.Model):

    id = models.AutoField(primary_key = True)
    professor_id = models.CharField(max_length = 20)
    approved_subjects = models.TextField(null=True)
    course_record = models.TextField(null=True)
    current_courses = models.TextField(null=True)
    campus = models.CharField(max_length = 20)
    faculty = models.CharField(max_length = 50)

    class Meta:
        app_label = 'SOOA_academic_record_ms'