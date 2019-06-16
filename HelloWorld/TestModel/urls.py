from django.conf.urls import url
from . import views
app_name = 'TestModel'

urlpatterns = [
    url(r'^$', views.index,name='blog_index'),
    url(r'^(?P<blog_id>[0-9]+)', views.detail,name='blog_detail'),
    url(r'^show/',views.lists,name='movie_show'),
    url(r'^selemiun_show/',views.phone_msg,name="phone_show"),

]
#HelloWorld.asd.getImage()