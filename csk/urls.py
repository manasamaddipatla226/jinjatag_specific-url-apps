from csk.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('jingatag/',jingatag,name='jingatag'),
]