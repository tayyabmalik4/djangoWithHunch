import json
from django.shortcuts import render, HttpResponse
from data.models import dht111
from datetime import datetime

# Create your views here.
def fetch(request):
    # -----this is fetching from the database and also get the latest id from database and show the template page.

    temperature = []
    humidity = []
    time = []
    task = dht111.objects.latest('id')
    all_data = dht111.objects.all().order_by('-id')[:6]
    for i in all_data:
        temperature.append(i.temperature)
        humidity.append(i.humidity)
        time.append(i.date)
    print(all_data[0].date)
    context = {'task':task,'temperature': json.dumps(temperature),'humidity':json.dumps(humidity),'time1': time[0] , 'time2': time[1] ,'time3': time[2] ,'time4': time[3] ,'time5': time[4] , 'time6': time[5]}
    
    return render(request,'fetch.html',context)

