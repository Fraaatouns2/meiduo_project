from django.shortcuts import render
from rest_framework.views import APIView
from django_redis import get_redis_connection
from django.http import HttpResponse

from meiduo_mall.libs.captcha.captcha import captcha
from . import constants
# Create your views here.


# url(r'^image_codes/(?P<image_code_id>[\w-]+)/$', views.ImageCodeView.as_view()),
class ImageCodeView(APIView):
    """图片验证码"""

    def get(self, request, image_code_id):
        """提供图片验证码"""

        # 生成图片验证码的内容和图片
        text, image = captcha.generate_captcha()

        # 将图片验证码的内容存储到redis
        redis_conn = get_redis_connection('verify_codes')
        redis_conn.set('img_%s' % image_code_id, text, constants.IMAGE_CODE_REDIS_EXPIRES)

        # 将图片响应给用户
        return HttpResponse(image, content_type='image/jpg')