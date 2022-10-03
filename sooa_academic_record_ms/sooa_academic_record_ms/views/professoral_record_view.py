from sooa_academic_record_ms.models.professoral_record_model import Professoral_record
from sooa_academic_record_ms.serializers.professoral_record_serializer import Professoral_recordSerializer
from rest_framework import mixins
from rest_framework import generics

class Professoral_recordList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    queryset = Professoral_record.objects.all()
    serializer_class = Professoral_recordSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Professoral_recordDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
                     
    queryset = Professoral_record.objects.all()
    serializer_class = Professoral_recordSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
