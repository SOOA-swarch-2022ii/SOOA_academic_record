from django.db import models
import json

class Professoral_record(models.Model):

    id = models.AutoField(primary_key = True)
    professor_id = models.CharField(max_length = 20)
    approved_subjects = models.TextField(max_length = 100, blank=True)
    course_record = models.TextField(max_length = 100, blank=True)
    campus = models.CharField(max_length = 20)
    faculty = models.CharField(max_length = 50)

    def set_approved_subjects(self, x):
        self.approved_subjects = json.dumps(x)

    def get_approved_subjects(self):
        return json.loads(self.approved_subjects)

    def set_course_record(self, x):
        self.course_record = json.dumps(x)

    def get_course_record(self):
        return json.loads(self.course_record)

    class Meta:
        app_label = 'sooa_academic_record_ms'