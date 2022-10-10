# from django.shortcuts import render
from datetime import datetime
import secrets
import logging
import string
from rich import print
from url_shortening_app.models import OriginalUrl
from url_shortening_app.serializers import OriginalUrlSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from url_shortening_app.utils import CacheObject


# create a redis instance
redis_cache = CacheObject("")


###############################################################
# Converting a provided long url to it's shortened version
###############################################################
def make_clickable(original_url, shortened_url):
    print(f"[link={original_url}]{shortened_url}[/link]!"),


@api_view(["POST", "GET", "DELETE"])
def encode_url(request):
    print(request.method)
    if request.method == "POST":
        payload = request.data
        original_url = payload["original_url"]
        original_url_object = OriginalUrl.objects.filter(
            original_url=original_url
        ).first()
        if original_url_object is None:

            serializer = OriginalUrlSerializer(data=payload)
            if serializer.is_valid():
                serializer.save()
        try:
            # retrieve shortened_url from cache
            cached_shortened_url = redis_cache.get(
                f"Original_url:{original_url}"
            )
            if cached_shortened_url is not None:
                data = {
                    "original_url": original_url,
                    "shortened_url": cached_shortened_url,
                    "date_created": datetime.now(),
                    "encoded": True,
                }
                return Response(data, status=status.HTTP_200_OK)

            # generate the short url
            base_url = "https://finnly.com/"
            str = string.ascii_lowercase
            random_string = "".join(secrets.choice(str) for i in range(4))
            shortened_url = base_url + random_string
            data = {
                "original_url": original_url,
                "shortened_url": make_clickable(original_url, shortened_url),
                "date_created": datetime.now(),
                "encoded": True,
            }
            # save data to cache
            cache_key = f"Original_url:{original_url}"
            redis_cache.set_(cache_key, shortened_url)

            return Response(data, status=status.HTTP_200_OK)
        except Exception as exc:
            logging.info("Error posting request")
            logging.exception(exc)

    return Response(
        {"error_message": "Request method should be 'POST'"},
        status=status.HTTP_400_BAD_REQUEST,
    )


###############################################################
# Converting a shortened url back to it's original long version
###############################################################


@api_view(["POST"])
def decode_url(request):
    print(request.data)
    if request.method == "POST":
        payload = request.data
        shortened_url = payload["shortened_url"]

        # retrieve original_url from cache
        cache_keys = redis_cache.keys()
        print(f"-----------------------{cache_keys}")
        for cache_key in cache_keys:
            print(redis_cache.get(cache_key) == shortened_url, cache_key)
            if redis_cache.get(cache_key) == shortened_url:
                data = {
                    "shortened_url": shortened_url,
                    "original_url": cache_key[13:],
                    "date_created": datetime.now(),
                    "decoded": True,
                }
                print(data)
                return Response(data, status=status.HTTP_200_OK)
    return Response(
        {"error_message": "Request method should be 'POST'"},
        status=status.HTTP_400_BAD_REQUEST,
    )
