from django.urls import path
from payment import views


urlpatterns=[
    
    path('request_view/',views.request_view,name="request"),
    path('verify/<transId>',views.verify,name="verify"),
]

