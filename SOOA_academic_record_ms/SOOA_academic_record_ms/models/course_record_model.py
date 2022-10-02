from django.db import models

class Course_record(models.Model):

    course_id = models.AutoField(primary_key = True)
    course_name = models.CharField(max_length = 120)
    course_topology = models.CharField(max_length = 20)
    number_credits = models.IntegerField()
    course_grade = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        app_label = 'academic_record_ms'