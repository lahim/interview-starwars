from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from .. import factories, serializers


class CharacterListViewTestCase(APITestCase):
    def test_response_status_of_non_empty_list(self):
        resp, _ = self._get_data()
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_response_data_is_not_none(self):
        resp, _ = self._get_data()
        self.assertIsNotNone(resp)

    def test_size_of_non_empty_list(self):
        resp, _ = self._get_data()
        self.assertEqual(len(resp.data), 1)

    def test_keys_of_list_item(self):
        resp, _ = self._get_data()

        for item in resp.data:
            self.assertIsNotNone(item)
            self.assertListEqual(
                list(serializers.CharacterListSerializer.Meta.fields),
                list(item.keys()))

    def test_character_values(self):
        resp, obj = self._get_data()

        for field in serializers.CharacterListSerializer.Meta.fields:
            self.assertEqual(getattr(obj, field), resp.data[0][field])

    def _get_data(self):
        url = reverse('movieassets:character-list')
        character = factories.CharacterFactory()
        return self.client.get(url), character
