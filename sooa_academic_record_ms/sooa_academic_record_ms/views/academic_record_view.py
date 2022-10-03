from sooa_academic_record_ms.models.academic_record_model import Academic_record
from sooa_academic_record_ms.serializers.academic_record_serializer import Academic_recordSerializer
from rest_framework import mixins
from rest_framework import generics

class Academic_recordList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    queryset = Academic_record.objects.all()
    serializer_class = Academic_recordSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Academic_recordDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
                     
    queryset = Academic_record.objects.all()
    serializer_class = Academic_recordSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
