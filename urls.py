from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('history_and_future_of_the_book.urls')),
]
