from django.http import JsonResponse
from .models import Match
from .serializers import MatchSerializer

def match_list(request):
    
    #get all matches
    #serialize them
    #return json
    matches = Match.objects.all()
    serializer = MatchSerializer(matches, many=True)
    return JsonResponse({'matches': serializer.data}, safe=False)