from django.urls import path
from .views import MyFunctionView

urlpatterns = [
    path('my-function/', MyFunctionView.as_view(), name='my_function'),
]
