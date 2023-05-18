from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EtudiantSerializer
from .models import Etudiant
from .serializers import PropSerializer
from .models import Prop
from .serializers import AnnoSerializer
from .models import Anno

# Create your views here.

@api_view(['GET'])
def getEtudiants(request):
    etudiants = Etudiant.objects.all()
    serialser = EtudiantSerializer(etudiants,many=True)
    return Response(serialser.data)

@api_view(['GET'])

def getEtudiant(request,pk):
    etudiant = Etudiant.objects.get(id=pk)
    serialser = EtudiantSerializer(etudiant,many=False)
    return Response(serialser.data)


@api_view(['POST'])
def createEtudiant(request):
    data = request.data

    etudiant = Etudiant.objects.create(
        nom = data['nom'],
        prenom = data['prenom'],
        mail = data['mail'],
        mot_pass = data['mot_pass'],
        carte_etud = data['carte_etud'],
        )

    serialser = EtudiantSerializer(etudiant,many=False)
    return Response(serialser.data)


@api_view(['PUT'])
def updateEtudiant(request,pk):
    etudiant = Etudiant.objects.get(id=pk)
    
    serialser = EtudiantSerializer(etudiant, data=request.POST)
    if serialser.is_valid():
        serialser.save()

    return Response(serialser.data)

@api_view(['DELETE'])
def deleteEtudiant(request,pk):
    etudiant = Etudiant.objects.get(id=pk)
    etudiant.delete()
    return Response('Etudiant was deleted')

@api_view(['GET'])
def getProps(request):
    props = Prop.objects.all()
    serialser = PropSerializer(props,many=True)
    return Response(serialser.data)

@api_view(['GET'])
def getProp(request,pk):
    prop = Prop.objects.get(id=pk)
    serialser = PropSerializer(prop,many=False)
    return Response(serialser.data)


@api_view(['POST'])
def createProp(request):
    data = request.data

    prop = Prop.objects.create(
        nom = data['nom'],
        prenom = data['prenom'],
        mail = data['mail'],
        mot_pass = data['mot_pass'],
        titre_bleu = data['titre_bleu'],

        )
    
    serialser = PropSerializer(prop,many=False)
    return Response(serialser.data)


@api_view(['PUT'])
def updateProp(request,pk):
    prop = Prop.objects.get(id=pk)
    
    serialser = PropSerializer(prop, data=request.POST)
    if serialser.is_valid():
        serialser.save()

    return Response(serialser.data)

@api_view(['DELETE'])
def deleteProp(request,pk):
    prop = Prop.objects.get(id=pk)
    prop.delete()
    return Response('Prop was deleted')

@api_view(['GET'])
def getAnnos(request):
    annos = Anno.objects.all()
    serialser = AnnoSerializer(Anno,many=True)
    return Response(serialser.data)

@api_view(['GET'])
def getAnno(request,pk):
    anno = Anno.objects.get(id=pk)
    serialser = AnnoSerializer(anno,many=False)
    return Response(serialser.data)


@api_view(['POST'])
def createAnno(request):
    data = request.data

    anno = Anno.objects.create(
        description = data['description'],
        photo = data['photo'],
        etat = data['etat'],
        prix = data['prix'],
        add = data['add'],
        numTel = data['numTel'],
    
        )

    serialser = AnnoSerializer(anno,many=False)
    return Response(serialser.data)


@api_view(['PUT'])
def updateAnno(request,pk):
    anno = Anno.objects.get(id=pk)
    
    serialser = AnnoSerializer(anno, data=request.POST)
    if serialser.is_valid():
        serialser.save()

    return Response(serialser.data)

@api_view(['DELETE'])
def deleteAnno(request,pk):
    anno = Anno.objects.get(id=pk)
    anno.delete()
    return Response('Annoce was deleted')

