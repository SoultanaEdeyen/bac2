
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignupSerializer
from django.contrib.auth import authenticate, login
from .models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProprietaireSignupSerializer, EtudiantSignupSerializer

class ProprietaireSignupView(APIView):
    def post(self, request):
        serializer = ProprietaireSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Proprietaire created successfully.', 'user_id': user.id})
        return Response(serializer.errors, status=400)

class EtudiantSignupView(APIView):
    def post(self, request):
        serializer = EtudiantSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Etudiant created successfully.', 'user_id': user.id})
        return Response(serializer.errors, status=400)


"""
class SignupView(APIView):

    @csrf_exempt

    def post(self, request):

        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(validated_data=serializer.validated_data)
        user = User.objects.get(email=data.email)
        # login the user
        login(request, user)
             # generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        # serialize the user and return the response
        user_serializer = SignupSerializer(user)
        return Response({
            'user': user_serializer.data,
            'access_token': str(access),
            'refresh_token': str(refresh)
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        # authenticate the user
        user = authenticate(request=request, email=email, password=password)
        if not user:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
       # login the user
        #login(request, user)
        # generate access token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        # serialize the user and return the response
        user_serializer = SignupSerializer(user)
        return Response({
            'user': user_serializer.data,
            'access_token': access_token,
            'refresh_token': str(refresh)
        }, status=status.HTTP_200_OK)
"""
""""

@api_view(['POST'])

def register(request):

    data = request.data
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return Response({'error': 'Username, email, and password are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
    )
    user.save()
    return Response({'success': 'User created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])

def login_view(request):

    email = request.data.get('email')

    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    if user is not None:

        login(request, user)

        return Response({'success': 'Connexion réussie.'}, status=status.HTTP_200_OK)

    else:

        return Response({'error': 'Nom d\'utilisateur ou mot de passe invalide.'}, status=status.HTTP_401_UNAUTHORIZED)

 

@csrf_exempt

def aPage(request):

    user:User=User.objects.get(pk=1)

    username= request.POST.get("username")

    email= request.POST.get("email")

    print(username)

    print(email)

    return JsonResponse({"UserName":username,

                         "email":email})

 

# Create your views here.

 
"""""
"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignupSerializer, ProprietaireSignupSerializer, EtudiantSignupSerializer, UserSerializer
from django.contrib.auth import authenticate, login
from .models import User, Proprietaire, Etudiant
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken



class SignupView(APIView):
    @csrf_exempt
    def post(self, request):
        user_type = request.data.get('user_type')

        if user_type == 'proprietaire':
            serializer = ProprietaireSignupSerializer(data=request.data)
        elif user_type == 'etudiant':
            serializer = EtudiantSignupSerializer(data=request.data)
        else:
            return Response({'detail': 'Invalid user type'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)
        data = serializer.create(validated_data=serializer.validated_data)
        user = User.objects.get(email=data.email)
        # login the user
        login(request, user)
        # generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        # serialize the user and return the response
        user_serializer = SignupSerializer(user)
        return Response({
            'user': user_serializer.data,
            'access_token': str(access),
            'refresh_token': str(refresh)
        }, status=status.HTTP_201_CREATED)
    








class LoginView(APIView):
    @csrf_exempt
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user_type = request.data.get('user_type')

        if user_type == 'proprietaire':
            user = authenticate(request, email=email, password=password)
        elif user_type == 'etudiant':
            # Utilisez le champ approprié pour l'authentification des étudiants (par exemple, username)
            user = authenticate(request, username=email, password=password)
        else:
            return Response({'detail': 'Invalid user type'}, status=status.HTTP_400_BAD_REQUEST)

        if user is not None:
            login(request, user)

            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            return Response({
                'access_token': str(access),
                'refresh_token': str(refresh)
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
"""
"""class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        # authenticate the user
        user = authenticate(request=request, email=email, password=password)
        if not user:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        # login the user
        login(request, user)
        # generate access token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        # serialize the user and return the response
        user_serializer = SignupSerializer(user)
        return Response({
            'user': user_serializer.data,
            'access_token': access_token,
            'refresh_token': str(refresh)
        }, status=status.HTTP_200_OK)
"""
