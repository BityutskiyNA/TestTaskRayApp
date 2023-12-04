import httpx
import asyncio

from asgiref.sync import sync_to_async

from config import app_settings
from products.models import Product, Images


@sync_to_async
def add_image_to_product_async(product_id, new_link):
    try:
        product_instance = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return

    new_image_instance, created = Images.objects.get_or_create(link=new_link)
    product_instance.images.add(new_image_instance)
    product_instance.save()


async def search_photos(query):
    url = 'https://api.unsplash.com/search/photos/'
    headers = {'Authorization': f'Client-ID {app_settings.access_key}'}
    params = {'query': query['name'], 'per_page': 1}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, params=params,
                                        timeout=5)
            if response.status_code == 200:
                data = response.json()
                data['query'] = query
                return data
            else:
                return None
        except httpx.TimeoutException:
            return None


async def save_photos(search_queries):
    tasks = [search_photos(query) for query in search_queries]
    results = await asyncio.gather(*tasks)

    for result in results:
        if result and result['results'] != []:
            photo = result['results'][0]
            print(photo['urls']['regular'])
            await add_image_to_product_async(result['query']['id'], photo['urls']['regular'])
