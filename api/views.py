from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from rest_framework import generics
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import userSerializer, productSerializer, customerSerializer, ordersSerializer, feedbackSerializer
from fameza.models import User, Product, Customer, Orders, Feedback


# Create your views here.

class listaUsuario(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class detalleUsuario(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class listaProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class detalleProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class listaCustomer(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = customerSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class detalleCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = customerSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class listaOrders(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = ordersSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class detalleOrders(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = ordersSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class listaFeedback(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = feedbackSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class detalleFeedback(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = feedbackSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('api:user_list', 'api:product_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, *kwargs)

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        token, _ = Token.objects.get_or_create(user=user)
        if token:
            login(self.request, form.get_user())
            return super(Login, self).form_valid(form)


class Cerrar(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)
