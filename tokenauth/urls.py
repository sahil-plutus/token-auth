
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from home import views
from rest_framework.authtoken.views import obtain_auth_token
from home.auth import CustomAuthToken


router = DefaultRouter()

router.register('stu', views.StudentModelViewSet, basename = 'student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', CustomAuthToken.as_view()),
]
