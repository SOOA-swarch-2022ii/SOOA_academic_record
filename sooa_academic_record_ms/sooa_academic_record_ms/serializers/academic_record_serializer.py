from rest_framework import serializers
from sooa_academic_record_ms.models.academic_record_model import Academic_record

class Academic_recordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Academic_record
        fields = ['id','student_id', 'subjects_pending', 'subjects_record', 'papa', 'papi', 'status', 'campus', 'faculty', 'career']
