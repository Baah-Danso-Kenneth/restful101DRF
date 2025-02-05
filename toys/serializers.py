from rest_framework.serializers import ModelSerializer
from toys.models import Toy

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('id',
                  'name',
                  'release_date',
                  'toy_category',
                  'was_included_in_home')
