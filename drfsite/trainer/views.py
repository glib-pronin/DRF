from django.shortcuts import render
from rest_framework import generics
from .models import Trainer
from .serializers import TrainerSerializer, UserSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.models import User
from rest_framework.permissions import  IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth import login

class TrainerPagination(LimitOffsetPagination):
    default_limit = 2  
    max_limit = 10   


class UserAPICreate(generics.ListCreateAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializers

     def perform_create(self, serializer):
          user = serializer.save()
          login(self.request, user)
     

class TrainerAPIList(generics.ListCreateAPIView):
     queryset= Trainer.objects.all()
     serializer_class=TrainerSerializer
     permission_classes = (IsAuthenticated, ) 
     pagination_class = TrainerPagination
     def get_queryset(self):
          spec_id = self.request.query_params.get('spec_id')
          name = self.request.query_params.get('name')
          if name:
               return Trainer.objects.filter(name=name)
          if spec_id:
                return   Trainer.objects.filter(spec_id=spec_id)
          return  Trainer.objects.all()



class TrainerAPIUpdate(generics.RetrieveUpdateAPIView):
     queryset= Trainer.objects.all()
     serializer_class = TrainerSerializer
     permission_classes = (IsAdminOrReadOnly,)


class TrainerAPIDestroy(generics.RetrieveDestroyAPIView):
     queryset = Trainer.objects.all()
     serializer_class = TrainerSerializer 
     permission_classes = (IsAdminOrReadOnly,)


# class TrainerAPIView (APIView):
#     def get(self, request):
#         w = Trainer.objects.all()
#         return Response({'trainers': TrainerSerializer(w, many=True).data})

#     def post(self, request):
#         serializer = TrainerSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'trainer': serializer.data})
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error":"Method PUT not allowed"})
        
#         try:
#             instance= Trainer.objects.get(pk=pk)
#         except:
#             return Response({"error":"Object does not exist"})
        
#         serializer = TrainerSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"trainer": serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error":"Method DELETE not allowed"})
        
#         try:
#             instance= Trainer.objects.get(pk=pk)
#         except:
#             return Response({"error":"Object does not exist"})
        
#         instance.delete()
#         return Response({"trainer": "was deleted"})


# class TrainerAPIView(generics.ListAPIView):
#     queryset =Trainer.objects.all()
#     serializer_class =TrainerSerializer