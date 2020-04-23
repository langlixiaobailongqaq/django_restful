"""django_restful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path            # 路径模块
from django.conf.urls import include    # 控制添加路径的模块
from rest_framework import routers      # 路由配置模块
from api import views                   # 视图模块

# 导入辅助函数 get_schema_view
from rest_framework.schemas import get_schema_view
# 导入两个类
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

# 利用辅助函数引入所导入的两个类
schema_view = get_schema_view(title='API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

router = routers.DefaultRouter()  # 生成路由对象
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),         # 代表位于根路径的主域名(http://127.0.0.1:8000/)
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),  # api-auth对应授权登录 url
    path('docs/', schema_view, name='docs'),   # 配置docs的 url 路径
]
