from django.urls import path
from .views import *

urlpatterns = [
    path('', start, name = 'start'),
    path('dbg/', dbg, name = 'dbg'),
    path('detect_face/', detect_face, name = 'detect_face'),
    path('detect_person/', detect_person, name = 'detect_person'),
    path('detect_mask/', detect_mask, name = 'detect_mask'),
    path('recognize_face', recognize_face, name = 'recognize_face')
]