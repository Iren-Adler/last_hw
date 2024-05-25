from django.shortcuts import render
from django.views.generic import ListView
from core import models, forms, filters


"""class Programmer(ListView):
    template_name = 'core/programmer.html'
    model = models.Programmer

    def get_filters(self):
        return filters.Programmer(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs #qs это метод с отфильтрованным qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['form'] = forms.Programmer
        context['filters'] = self.get_filters()

        return context
"""
"""class Programmer(APIView):
    def get(self, request):
        qs = models.Programmer.object.all()
        names = [p.name for p in qs]
        serializer = serializers.Programmer(qs, many=True)

        return Response(data=serializer.data)
    def post(self, request):
        serializer = serializers.Programmer(data=request.data)
        serializer.is_valid(raise_exceptions=True)
        serializer.save()

        return Response({'massage': 'OK'})
"""
class Programmer(ModelViewSet):
    queryset = models.Programmer.objects.all()
    filterset_class = filters.Programmer
    serializer_class = serializer.Programmer
