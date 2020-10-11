from rest_framework.viewsets import ReadOnlyModelViewSet

from .. import models, serializers


class CharacterListView(ReadOnlyModelViewSet):
    queryset = models.Character.objects.all()
    serializer_class = serializers.CharacterDetailSerializer
    list_serializer_class = serializers.CharacterListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return self.list_serializer_class
        return super().get_serializer_class()

    def get_serializer_context(self):
        ctx = super().get_serializer_context()

        if self.action == 'retrieve':
            ctx.update(
                {
                    'offset': int(self.request.query_params.get('offset', 10)),
                    'columns': self.request.query_params.get('columns'),
                }
            )
        return ctx
