from rest_framework import serializers
from . import models, services


class CharacterListSerializer(serializers.ModelSerializer):
    created_date = serializers.SerializerMethodField()

    def get_created_date(self, obj: models.Character):
        return obj.created_date

    class Meta:
        model = models.Character
        fields = ('id', 'name', 'created_date')


class CharacterDetailSerializer(serializers.ModelSerializer):
    table = serializers.SerializerMethodField()

    def get_offset(self):
        return self.context.get('offset', None)

    def get_columns(self):
        columns = self.context.get('columns')
        return columns.split(',') if columns else None

    def get_table(self, obj: models.Character):
        columns, headers, rows = services.load_characters_from_csv(
            obj, offset=self.get_offset(), count_by_columns=self.get_columns())

        data = []
        for row in rows:
            r = {header: cel for cel, header in zip(row, headers)}
            data.append(r)

        return {
            'items': data,
            'columns': columns,
        }

    class Meta:
        model = models.Character
        fields = ('name', 'source_file', 'table', 'created_date')
