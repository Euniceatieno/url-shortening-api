# from django.shortcuts import render
from datetime import datetime
import logging

from django.shortcuts import redirect
from url_shortening_app.models import OriginalUrl
from url_shortening_app.serializers import OriginalUrlSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from url_shortening_app.utils import (
    RedisCache,
    generate_random_string,
    validate_url,
)
from django.views.decorators.csrf import csrf_exempt


# create a redis instance
redis_cache = RedisCache()


###############################################################
# Converting a provided long url to it's shortened version
###############################################################


@api_view(["POST"])
def encode_url(request):
    if request.method == "POST":

        payload = request.data
        payload["original_url_id"] = generate_random_string()
        original_url = payload["original_url"]
        valid_url = validate_url(original_url)
        if valid_url is not True:
            return Response(
                {
                    "invalid_url_error": f"{original_url} does not "
                    f"exist on Internet"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

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

            base_url = request.build_absolute_uri()[
                : -len(request.get_full_path())
            ]
            shortened_url = base_url + "/" + payload["original_url_id"]
            data = {
                "original_url": original_url,
                "shortened_url": shortened_url,
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
            return

    return Response(
        {"error_message": "Request method should be 'POST'"},
        status=status.HTTP_400_BAD_REQUEST,
    )


###############################################################
# Redirecting the short_url
###############################################################


@csrf_exempt
def redirect_short_url(request, url_id):
    original_url_object = OriginalUrl.objects.filter(
        original_url_id=str(url_id)
    ).first()
    return redirect(original_url_object.original_url)


###############################################################
# Converting a shortened url back to it's original long version
###############################################################


@api_view(["POST"])
def decode_url(request):
    if request.method == "POST":
        try:
            payload = request.data
            shortened_url = payload["shortened_url"]
            url_id = shortened_url[-6:]
            # query  the original_url object where
            # url_id is the original_url_id
            original_url_object = OriginalUrl.objects.filter(
                original_url_id=str(url_id)
            ).first()

            if original_url_object is not None:
                data = {
                    "shortened_url": shortened_url,
                    "original_url": original_url_object.original_url,
                    "date_created": datetime.now(),
                    "decoded": True,
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {
                        "error_message": (
                            f"Short url:{shortened_url} isn't "
                            f"mapped to any url"
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as exc:
            logging.info("Error posting request")
            logging.exception(exc)

    return Response(
        {"error_message": "Request method should be 'POST'"},
        status=status.HTTP_400_BAD_REQUEST,
    )
