from datetime import datetime
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Player
from ..serializer import PlayerSerializer
from ..schemas import CreatePlayer
from ..validators.utils import valid_age, document_exist


@api_view(['POST'])
def create_player(request):
    try:
        data = request.data
        date_birth = datetime.strptime(data['date_birth'], '%Y-%m-%d').date()

        if not valid_age(date_birth, 18):
            return Response({'details': f'Jogador deve ser maior de idade'}, status=status.HTTP_400_BAD_REQUEST)

        if document_exist(Player, 'document', data['document']):
            return Response({'detail': f'Cpf ja cadastrado.'}, status=status.HTTP_400_BAD_REQUEST)
        
        payload = CreatePlayer(**request.data)
        new_player = Player.objects.create(**payload.model_dump())
        new_player.save()
        return Response(payload.model_dump(mode='json'), status=status.HTTP_201_CREATED)

    
    except Exception as exception:
        return Response({"detail": str(exception)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_player(request):
    try:
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as exception:
        return Response({"detail": str(exception)}, status=status.HTTP_400_BAD_REQUEST)