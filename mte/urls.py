from django.conf.urls import url
from mte.views import *


urlpatterns = [
    url(r'^markdown/$', MarkdownAPIView.as_view(), name='markdown'),
    url(r'^convert/$', MarkdownToEvernoteView.as_view(), name='convert'),
    url(r'^test/$', TestInputView.as_view(), name='test'),
]