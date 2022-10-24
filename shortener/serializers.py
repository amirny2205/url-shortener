from rest_framework import serializers
from shortener.models import LinkModel
import re
import random
import string

def get_short_string():
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(6))


class LinkSerializer(serializers.ModelSerializer):
    shortened = serializers.CharField(max_length=200, required=False)


    def to_internal_value(self, data):
        new_link = {}
        new_link['redirect_to'] = data['redirect_to']
        if 'shortened' in data:
            new_link['shortened'] = data['shortened']
        else:
            new_link['shortened'] = get_short_string()
        return super().to_internal_value(new_link)

    def validate_redirect_to(self, value):
        r ="https?://www\..*"
        if not re.match(r, value):
            raise serializers.ValidationError('your redirect_to doesn\'t match re "https?://www\..*"')
        return value

    class Meta:
        model = LinkModel
        fields = '__all__'