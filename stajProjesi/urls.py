
from django.contrib import admin
from django.urls import path,re_path
from django.views.static import serve
from appUser.views import *
from appMy.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    # appMY
    path('',dashboardPage, name='dashboardPage'),
    path('forumDetail',forumDetail, name='forumDetail'),
    path('forumlar/<str:pk>',forumDetail, name='forumDetail'),
    path('search/', Query, name='Query'),

    # appUser
    path('loginPage', loginPage , name='loginPage'),
    path('blog/<category>/<str:pk>',postDetail, name='postDetail'),
    path('message/<str:game_slug>',messagePost, name='messagePost'),
    path('logout',logoutUser, name='logoutUser'),
    path('accountUser', accountUser, name='accountUser'),
    
]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "appMy.views.view_404"
handler500 = "appMy.views.view_500"