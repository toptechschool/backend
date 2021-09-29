from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from knox.models import AuthToken
from rest_framework import generics, permissions, views, viewsets, mixins, generics, status
from rest_framework.response import Response
from users.models import User, Profile
from users.serializers import UserSerializer, RegisterSerializer, LoginSerializer, ProfileSerializer
from users.tokens import account_activation_token


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        _, token = AuthToken.objects.create(user)

        # For email activation
        message = render_to_string('account_activation_email.html', {
            'user': user,
            # TODO: Frontend link, frontend gets the uid and token and sends back to backend for verification
            'domain': settings.ROOT_URL,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        send_mail('Email address confirmation', message,
                  'admin@gmail.com', [user.email],  fail_silently=False,)

        return Response({
            # "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        })


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response({
            # "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        })


class EmailActivationAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(self.kwargs.get('uidb64')))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, self.kwargs.get('token')):
            profile = Profile.objects.get(user=user)
            profile.email_varified = True
            profile.save()
            return Response({'msg': 'YES'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'NO'}, status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
