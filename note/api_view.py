from .serializers import NoteSerializer , RegisterSerializer
from rest_framework import viewsets , generics
from .models import Note, Customer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter



class NoteViewset(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']


    def get_queryset(self):
        customer = Customer.objects.get(user=self.request.user)
        return Note.objects.filter(user=customer)
    
    def perform_create(self, serializer):
        customer = Customer.objects.get(user=self.request.user)
        serializer.save(user=customer)

class RegisterView(generics.CreateAPIView):
    queryset = RegisterSerializer
