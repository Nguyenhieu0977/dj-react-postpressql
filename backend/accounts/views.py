from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

class SingupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email đã tồn tại'})
            else:
                if len(password) < 6:
                    return Response({'error': 'Mật khẩu phải lớn hơn 6 ký tự'})
                else:
                    user = User.objects.create_user(email=email, password=password, name=name)

                    user.save()
                    return Response({'success': 'Tạo tài khoản thành công'})
        else:
                return Response({'error': 'Mật khẩu không trùng khớp'})

