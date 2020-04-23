from django.shortcuts import render
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer
from api.models import User, Group

# Create your views here.
"""
在URL中会定义相应的规则到 ViewSets。ViewSets则通过 serializer_class找到相应的 Serializers
这里将User和Group的对象赋予queryset，并返回这些值。在UserSerializer和GroupSerializer中定义要返回的字段
"""

# viewsets 通过serializer_class 找到对应的serializers
class UserViewSet(viewsets.ModelViewSet):
	"""
		retrieve:
			Return a user instance

		list:
			Return all users, ordered by most recently joined.

		create:
			Remove an existing user.

		partial_update:
			Update a user.
	"""
	queryset = User.objects.all()  # 将User的所有对象赋给queryset，并返回对应值
	serializer_class = UserSerializer   # 指向UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
			retrieve:
				Return a group instance

			list:
				Return all group, ordered by most recently joined.

			create:
				Remove an existing group.

			partial_update:
				Update a group.
		"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer