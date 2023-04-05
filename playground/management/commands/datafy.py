from django.core.management.base import BaseCommand
import uuid
import csv
from django.utils.text import slugify
from playground.models import Event
import os
import datetime 
class Command(BaseCommand):
    help = 'Adding data to Database'
    def handle(self, *args, **options):
        data_file = os.path.join(os.path.dirname(__file__), 'data', 'data.csv')
        file = open("data.csv", encoding="cp437")
        with open("data.csv", 'r',encoding="cp437") as f:
            reader = csv.reader(f)
            for row in reader:
                obj = Event(name=row[0], description=row[1], startTime = datetime.datetime.strptime(row[2], '%H:%M').time()
,date=datetime.datetime.strptime(row[3], '%Y-%m-%d').date(),venue=row[4],state=row[5],image=row[6])
                
                obj.save()
                print(row)
        

        self.stdout.write(self.style.SUCCESS('Data Added'))

