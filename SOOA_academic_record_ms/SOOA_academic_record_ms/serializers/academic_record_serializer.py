from rest_framework import serializers
from SOOA_academic_record_ms.models.academic_record_model import Academic_record

class Academic_recordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Academic_record
        fields = ['id','student_id', 'pensum', 'academic_history', 'current_courses', 'papa', 'papi', 'status', 'campus', 'faculty', 'career']
