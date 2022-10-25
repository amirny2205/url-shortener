from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from shortener.models import LinkModel
from shortener.serializers import LinkSerializer


class CreateLinkAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectAPIView(APIView):


    def get(self, request, shortened, *args, **kwargs):
        link = LinkModel.objects.get(shortened=shortened)
        return redirect(link.redirect_to)