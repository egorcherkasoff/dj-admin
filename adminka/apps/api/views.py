from ..users.models import User
from django.contrib.auth.models import Group
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer
from django.http import Http404
from django.utils import timezone

# Create your views here.


class UsersList(APIView):
    def get(self, request, format=None):
        users = User.objects.filter(deleted__isnull=True)
        serializer = UserSerializer(users, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            if user.deleted is not None:
                raise Http404
            return user
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
            user = self.get_object(pk)
            if user.deleted is not None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.deleted = timezone.now()
        user.is_active = False
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailsGroups(APIView):
    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            if user.deleted is not None:
                raise Http404
            return user
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        groups = user.groups.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, u_id, pk):
    #     user = self.get_object(u_id)
    #     try:
    #         user.groups.add(pk)
    #         serializer = UserSerializer(user)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Group.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)