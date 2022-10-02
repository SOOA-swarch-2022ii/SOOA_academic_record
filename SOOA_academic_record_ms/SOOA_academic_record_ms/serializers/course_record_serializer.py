from rest_framework import serializers
from SOOA_academic_record_ms.models.course_record_model import Course_record

class Course_recordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course_record
        fields = ['course_id', 'course_name', 'course_topology', 'number_credits', 'course_grade']
