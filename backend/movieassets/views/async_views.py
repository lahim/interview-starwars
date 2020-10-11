import asyncio

from django.http import JsonResponse
from django.utils.translation import gettext as _

from .. import services


async def fetch_data_view(request):
    loop = asyncio.get_event_loop()

    loop.create_task(services.fetch_people())
    data = {
        'message': _('Fetching data...'),
    }
    return JsonResponse(data=data, status=200)
