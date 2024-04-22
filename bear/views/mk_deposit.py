from decimal import Decimal
from pydantic import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from ..schemas import CreateDeposit
from ..models import Player, Deposit


@api_view(['POST'])
def mk_deposit(request):
    try:
        payload = CreateDeposit(**request.data)   
        deposit_value = Decimal(request.data['value'])

        if deposit_value <= 10:
            return Response({'details': 'Depósito mínimo de 10,00'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            player = Player.objects.get(id=payload.player_id)
        except Player.DoesNotExist:
            return Response({"details": "Jogador não existe"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            with transaction.atomic():
                player = Player.objects.select_for_update().get(id=payload.player_id)
                new_balance = player.balance + deposit_value
                player.balance = new_balance

                player.save()
                new_deposit = Deposit.objects.create(
                    **payload.model_dump(),
                    balance_after=new_balance
                )

                new_deposit.save()
        except Player.DoesNotExist:
            return Response({'details': "Conta não existe"}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message':'Depósito realizado com sucesso'}, status=status.HTTP_201_CREATED)
    except ValidationError as validation_error:
        return Response({"detail": str(validation_error)}, status=status.HTTP_400_BAD_REQUEST)