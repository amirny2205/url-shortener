from rest_framework import serializers

from shortener.models import LinkModel

from django.conf import settings


def shorten(seed):
    return "test"


class LinkSerializer(serializers.ModelSerializer):


    def to_internal_value(self, data):
        print('flag_A')
        print(type(data))
        print(data)
        new_link = []
        new_link['redirect_to'] = data['redirect_to']
        if 'shortened' in data:
            new_link['shortened'] = data['shortened']
        else:
            new_link['shortened'] = shorten(data['redirect_to'])

        return super().to_internal_value(new_link)


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['shortened'] = settings.DOMAIN + representation['shortened']

        return representation


    class Meta:
        model = LinkModel
        fields = '__all__'