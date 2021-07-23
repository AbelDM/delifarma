from rest_framework import serializers
from fameza.models import User, Product, Customer, Orders, Feedback


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ordersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class feedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
