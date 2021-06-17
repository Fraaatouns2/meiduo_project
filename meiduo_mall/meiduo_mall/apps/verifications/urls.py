from django.conf.urls import url

from . import views


urlpatterns = [
    # 图片验证码
    url(r'^image_codes/(?P<image_code_id>[\w-]+)/$', views.ImageCodeView.as_view()),
]