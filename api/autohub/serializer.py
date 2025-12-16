from rest_framework import serializers
from autohub.models import Cars, Body, Brand, Sale, Rent, Transmission


# class CarModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Apartment
#         fields = '__all__'


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    picture = serializers.ImageField(required=False, allow_null=True)
    name = serializers.CharField()
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), required=False, allow_null=True)
    model = serializers.CharField()
    price = serializers.IntegerField()
    body = serializers.PrimaryKeyRelatedField(queryset=Body.objects.all(), required=False, allow_null=True)
    color = serializers.CharField()
    seats = serializers.IntegerField()
    sale = serializers.PrimaryKeyRelatedField(queryset=Sale.objects.all(), required=False, allow_null=True)
    rent = serializers.PrimaryKeyRelatedField(queryset=Rent.objects.all(), required=False, allow_null=True)
    transmission = serializers.PrimaryKeyRelatedField(queryset=Transmission.objects.all(), required=False, allow_null=True)
    year = serializers.IntegerField()
    description = serializers.CharField()
    join_date = serializers.DateField()


    def validate(self, attrs):
        print(attrs.get("name"))
        print(attrs)
        if attrs.get("year") <= 1950:
            raise serializers.ValidationError("Year too old")
        return super().validate(attrs)

    def create(self, validate_date):
        return Cars.objects.create(**validate_date)
    
    def update(self, instance, validate_data):
        instance.picture = validate_data.get('picture', instance.picture)
        instance.name = validate_data.get('name', instance.name)
        instance.brand = validate_data.get('brand', instance.brand)
        instance.model = validate_data.get('model', instance.model)
        instance.price = validate_data.get('price', instance.price)
        instance.body = validate_data.get('body', instance.body)
        instance.color = validate_data.get('color', instance.color)
        instance.seats = validate_data.get('seats', instance.seats)
        instance.sale = validate_data.get('sale', instance.sale)
        instance.rent = validate_data.get('rent', instance.rent)
        instance.transmission = validate_data.get('transmission', instance.transmission)
        instance.year = validate_data.get('year', instance.year)
        instance.description = validate_data.get('description', instance.description)
        instance.join_date = validate_data.get('join_date', instance.join_date)
        instance.save()
        return instance
    

class SaleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def validate(self, attrs):
        print(attrs.get("name"))
        print(attrs)
        return super().validate(attrs)

    def create(self, validate_date):
        return Sale.objects.create(**validate_date)
    
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.save()
        return instance
    

class RentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def validate(self, attrs):
        print(attrs.get("name"))
        print(attrs)
        return super().validate(attrs)

    def create(self, validate_date):
        return Rent.objects.create(**validate_date)
    
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.save()
        return instance
    

class TransmissionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def validate(self, attrs):
        print(attrs.get("name"))
        print(attrs)
        return super().validate(attrs)

    def create(self, validate_date):
        return Transmission.objects.create(**validate_date)
    
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.save()
        return instance
    

class BodySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def validate(self, attrs):
        print(attrs.get("name"))
        print(attrs)
        return super().validate(attrs)

    def create(self, validate_date):
        return Body.objects.create(**validate_date)
    
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.save()
        return instance
    

class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    logo = serializers.ImageField(required=False, allow_null=True)

    def validate(self, attrs):
        print(attrs.get("name"))
        print(attrs)
        return super().validate(attrs)

    def create(self, validate_date):
        return Brand.objects.create(**validate_date)
    
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.logo = validate_data.get('logo', instance.logo)
        instance.save()
        return instance
    

class CarModelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Cars
        fields = ("id", "name", "description", 'price', "owner", "picture", "brand", "model", 
                  "body", "color", "seats", "sale", "rent", "transmission", "year", "join_date")
        

class CarsDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Cars
        fields = "__all__"


class CarsCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'