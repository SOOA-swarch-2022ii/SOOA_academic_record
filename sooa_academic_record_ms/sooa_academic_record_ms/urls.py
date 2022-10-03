from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from sooa_academic_record_ms.views.academic_record_view import Academic_recordList
from sooa_academic_record_ms.views.academic_record_view import Academic_recordDetail
from sooa_academic_record_ms.views.professoral_record_view import Professoral_recordList
from sooa_academic_record_ms.views.professoral_record_view import Professoral_recordDetail

urlpatterns = [
    path('academic-record/', Academic_recordList.as_view()),
    path('academic-record/<int:pk>', Academic_recordDetail.as_view()),
    path('professoral-record/', Professoral_recordList.as_view()),
    path('professoral-record/<int:pk>', Professoral_recordDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)