from hyper_resource.resources.AbstractResource import AbstractResource, JSON_CONTENT_TYPE, CONTENT_TYPE_JSONLD
from hyper_resource.resources.FeatureCollectionResource import FeatureCollectionResource
from hyper_resource.resources.FeatureResource import FeatureResource
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import *

class APIRoot(AbstractResource):

    def add_entry_point_link_header(self, request, response):
        entry_point_uri = request.build_absolute_uri()[:-1]
        link_content = '<' + entry_point_uri + '>; rel="https://schema.org/EntryPoint", '
        link_content += '<' + entry_point_uri + '.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
        response["Link"] = link_content

    def get_entry_point_data(self, request, *args, **kwargs):
        return {
            "edificacao-turistica": reverse("rj:EdificacaoTuristica_list", args=args, kwargs=kwargs, request=request),
        }

    def get(self, request, *args, **kwargs):
        data = self.get_entry_point_data(request, *args, **kwargs)
        response = Response(data, status=status.HTTP_200_OK, content_type=JSON_CONTENT_TYPE)
        self.add_entry_point_link_header(request, response)
        return response

    # todo: maybe this content make more sanse in contexts.py
    def options(self, request, *args, **kwargs):
        entry_point_keys = self.get_entry_point_data(request, *args, **kwargs).keys()
        context = {"@context": {"hydra": "https://www.w3.org/ns/hydra/core#"}}
        for key in entry_point_keys:
            context["@context"].update({
                key: {
                    "@id": "https://purl.org/geojson/vocab#FeatureCollection",
                    "@type": "@id"
                }
            })

        context["hydra:supportedProperty"] = []

        for key in entry_point_keys:
            context["hydra:supportedProperty"].append({
                "hydra:property": key,
                "hydra:writable": False,
                "hydra:readable": True,
                "hydra:required": False
            })

        response = Response(context, status=status.HTTP_200_OK, content_type=CONTENT_TYPE_JSONLD)
        self.add_entry_point_link_header(request, response)
        return response

class EdificacaoTuristicaList(FeatureCollectionResource):
    serializer_class = EdificacaoTuristicaSerializer

class EdificacaoTuristicaDetail(FeatureResource):
    serializer_class = EdificacaoTuristicaSerializer