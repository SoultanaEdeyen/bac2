from rest_framework.serializers import ModelSerializer
from.models import Etudiant
from.models import Prop
from.models import Anno

class EtudiantSerializer(ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'
        
class PropSerializer(ModelSerializer):
    class Meta:
        model = Prop
        fields = '__all__'
class AnnoSerializer(ModelSerializer):
    class Meta:
        model = Anno
        fields = '__all__'
