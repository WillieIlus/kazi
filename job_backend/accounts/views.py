from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer

from .models import User

class ActivateEmailView(View):
    def get(self, request, **kwargs):
        email = request.GET.get('email', '')
        id = request.GET.get('id', '')

        if email and id:
            user = User.objects.get(id=id, email=email)
            user.is_active = True
            user.save()

            return HttpResponse('Your account has been activated successfully.')
        else:
            return HttpResponse('Your account has not been activated successfully.')


class ResetPasswordView(View):
    def get(self, request, **kwargs):
        email = request.GET.get('email', '')
        id = request.GET.get('id', '')

        if email and id:
            user = User.objects.get(id=id, email=email)
            user.is_active = True
            user.save()

            return HttpResponse('Your account has been activated successfully.')
        else:
            return HttpResponse('Your account has not been activated successfully.')


class ResetPasswordConfirmView(View):
    def get(self, request, **kwargs):
        email = request.GET.get('email', '')
        id = request.GET.get('id', '')

        if email and id:
            user = User.objects.get(id=id, email=email)
            user.is_active = True
            user.save()

            return HttpResponse('Your account has been activated successfully.')
        else:
            return HttpResponse('Your account has not been activated successfully.')


class UserListView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        users = User.objects.all()
        return users


class UserProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.all()
        return user

    def get_object(self):
        # use the UUID primary key from the URL to retrieve the user
        pk = self.kwargs.get('pk')
        return get_object_or_404(User, pk=pk)



