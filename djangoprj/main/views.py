from django.shortcuts import render

# Create your views here.

from .models import WUsers

from mikrotik.models import MTSnapshot, MTUsers

def home_page(request):
    data = []
    #for u in MTUsers.objects.all()[MTUsers.objects.all().count()-50:MTUsers.objects.all().count()]: 
    for u in MTUsers.objects.all()[0:20]: 
    #for u in MTUsers.objects.all(): 
        snapshot = []
        
        for s in MTSnapshot.objects.filter(ip=u.ip).order_by('-id')[0:900]:
            max = 0
            snapshot.append({'time': s.time.strftime("%H:%M"), 'value': s.activity, 'id': s.id})
        if len(snapshot)>0 and u.mac:
            
            for dt in snapshot:
                if dt['value']>max:
                    max = dt['value']
            #print(u.mac)
            data.append( {
                "ip": u.ip,
                'mac': u.mac,
                "id": u.ip.replace('.','-'),
                "host": u.host,
                "data": snapshot,
                "max": max,
                "cnt": len(snapshot)
            }
            )
            
    graph = MTSnapshot.objects.filter(mac='20:C9:D0:C6:9B:B5')
    print(graph)
    return render(request,'main.html',{ "graph": graph, "data": data})