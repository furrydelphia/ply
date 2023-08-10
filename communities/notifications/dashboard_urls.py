from django.urls import path
from communities.notifications import dashboard_views

urlpatterns = [
    path('all', dashboard_views.all_notifications),
    path('mentions', dashboard_views.all_mentions)
    #path('upload',dashboard_views.upload_content),
    #path('api/',include('core.api_urls')),
    #path('upload/lighttable/',dashboard_views.upload_lighttable)
]
