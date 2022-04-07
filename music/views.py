from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from.models import Song
from .serializers import SongSerializer



@api_view(['GET','POST'])
def song_list(request):
    if request.method =='GET':
        music=Song.objects.all()
        serializer=SongSerializer(music, many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer=SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def song_detail(request, pk):

    print(pk)
    return Response(pk)
