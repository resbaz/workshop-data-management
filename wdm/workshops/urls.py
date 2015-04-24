from django.conf.urls import url, patterns

from .views import WorkshopList, WorkshopDetail, WorkshopCreate, WorkshopUpdate, WorkshopDelete, PersonList, PersonCreate, PersonDetail

urlpatterns = patterns('',
    url(r'^$', WorkshopList.as_view(), name='index'),
    url(r'^workshops/$', WorkshopList.as_view(), name='workshop_index'),
    url(r'^workshops/add/$', WorkshopCreate.as_view(), name='workshop_add'),
    url(r'^workshops/(?P<slug>[-\w]+)/$', WorkshopDetail.as_view(), name='workshop_detail'),
    url(r'^workshops/(?P<slug>[-\w]+)/update/$', WorkshopUpdate.as_view(), name='workshop_update'),
    url(r'^workshops/(?P<slug>[-\w]+)/delete/$', WorkshopDelete.as_view(), name='workshop_delete'),
    url(r'^people/$', PersonList.as_view(), name='person_index'),
    url(r'^people/add/$', PersonCreate.as_view(), name='person_add'),
    url(r'^people/(?P<slug>[-\w]+)/$', PersonDetail.as_view(), name='person_detail'),

)

