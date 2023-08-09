from rest_framework import generics, viewsets, response, status
from .models import Educational
from .serializers import EducationalSerializer, EducationalHyperSerializer
class EducationalListAPIView(generics.ListAPIView):
    queryset = Educational.objects.all()
    serializer_class = EducationalSerializer
class EducationalDetailAPIView(generics.RetrieveAPIView):
    queryset = Educational.objects.all()
    serializer_class = EducationalSerializer
class EducationalCreateAPIView(generics.CreateAPIView):
    serializer_class = EducationalSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers= self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
class EducationalUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Educational.objects.all()
    serializer_class = EducationalSerializer
class EducationalViewSet(viewsets.ModelViewSet):
    queryset = Educational.objects.all()
    serializer_class = EducationalHyperSerializer
class EducationalDeleteAPIView(generics.DestroyAPIView):
    queryset = Educational.objects.all()
    serializer_class = EducationalSerializer