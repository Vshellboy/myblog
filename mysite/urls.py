from django.conf.urls import include, url
from django.contrib import admin
from django.urls import  path

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', admin.site.urls),
    url(r'^blog/', include(("blog.urls","blog"), namespace='blog')),
    # url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),

]

#import debug_toolbar
#urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
