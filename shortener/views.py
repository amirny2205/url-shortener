
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from shortener.serializers import LinkSerializer


class CreateLinkAPIView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.body
        print('flag B ', data)
        serializer = LinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'detail':'incorrect data given'}, status=status.HTTP_400_BAD_REQUEST)