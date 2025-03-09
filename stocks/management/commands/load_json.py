from django.core.management.base import BaseCommand
from stocks.models import Stock
import json

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('stocks/data.json', 'r') as f:
            data = json.load(f)
            for entry in data:
                Stock.objects.create(
                    date=entry["date"],
                    trade_code=entry["trade_code"],
                    high=entry["high"],
                    low=entry["low"],
                    open=entry["open"],
                    close=entry["close"],
                    volume=int(entry["volume"].replace(",", ""))
                )
