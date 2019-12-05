from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import *

class EdificacaoTuristicaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdificacaoTuristica
        geo_field = 'geom'
        auto_bbox = True
        id_field = 'gid'
        fields = ["gid", "id_objeto", "nome", "nomeabrev", "geometriaa", "tipoediftu", "ovgd", "operaciona", "situacaofi", "matconstr"]