from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status  # For status codes
from django.shortcuts import get_object_or_404
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    """
    Returns a list of available API routes.
    """
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    """
    Retrieve and return a list of all room objects.
    """
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)  # Use 'serializer' instead of 'serializers'
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    """
    Retrieve and return a specific room by its primary key (pk).
    """
    try:
        room = Room.objects.get(id=pk)
        serializer = RoomSerializer(room, many=False)
        return Response(serializer.data)
    except Room.DoesNotExist:
        return Response({'error': 'Room not found'}, status=status.HTTP_404_NOT_FOUND)
