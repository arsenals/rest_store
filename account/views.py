from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer


def send_activation_mail(user):
    code = user.create_activation_code()
    send_mail('Активация аккаунта',
              f'Вы успешно зарегистрировались. Пожалуйста активируйте свой аккаунт. Для этого пройдите по ссылке http://127.0.0.1:8000/activate/{code}/',
              'test@test.com',
              [user.email, ])

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_activation_mail(user)
            return Response('Аккаунт успешно создан')