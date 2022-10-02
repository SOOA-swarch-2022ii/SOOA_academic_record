from SOOA_academic_record_ms.models.course_record_model import Course_record
from SOOA_academic_record_ms.serializers.course_record_serializer import Course_recordSerializer
from rest_framework import mixins
from rest_framework import generics

class Course_recordList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    queryset = Course_record.objects.all()
    serializer_class = Course_recordSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Course_recordDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
                     
    queryset = Course_record.objects.all()
    serializer_class = Course_recordSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
