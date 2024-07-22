import datetime
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CurrencyView(APIView):
    def get(self, request, code, date=None):
        bank = cache.get('bank_instance')
        currencies = cache.get('currencies')
        if currencies is None:
            return JsonResponse({'error': 'Currencies not available'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if code in currencies:
            rate = bank.get_rate(code, date)
            data = {
                "code": code,
                "rate": rate,
                "date": datetime.datetime.now().date() if date is None else date
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'No such currency'}, status=status.HTTP_404_NOT_FOUND)
