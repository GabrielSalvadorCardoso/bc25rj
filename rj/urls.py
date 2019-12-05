from django.urls import path, re_path
from .views import *

app_name = "rj"
urlpatterns = [
    path('', APIRoot.as_view(), name="root"),
    re_path('^edificacao-turistica/(?P<pk>[0-9]+)/(?P<operation_or_attributes>.+)/?$', EdificacaoTuristicaDetail.as_view(), name='EdificacaoTuristica_detail_operation_or_attributes'),
    re_path('^edificacao-turistica/(?P<sigla>[A-Za-z]{2})/(?P<operation_or_attributes>.+)/?$', EdificacaoTuristicaDetail.as_view(), name='EdificacaoTuristica_bysigla_operation_or_attributes'),
    path('edificacao-turistica/<int:pk>.<str:extension>', EdificacaoTuristicaDetail.as_view(), name='EdificacaoTuristica_detail_extension'),
    re_path('^edificacao-turistica/(?P<sigla>[A-Za-z]{2})(?P<extension>\..+)/?$', EdificacaoTuristicaDetail.as_view(), name='EdificacaoTuristica_bysigla_extension'),
    path('edificacao-turistica/<int:pk>', EdificacaoTuristicaDetail.as_view(), name='EdificacaoTuristica_detail'),
    re_path('^edificacao-turistica/(?P<sigla>[A-Za-z]{2})/?$', EdificacaoTuristicaDetail.as_view(), name='EdificacaoTuristica_bysigla_detail'),
    path('edificacao-turistica/<path:operation_or_attributes>/', EdificacaoTuristicaList.as_view(), name='EdificacaoTuristica_list_operation_or_attributes'),
    path('edificacao-turistica.<str:extension>', EdificacaoTuristicaList.as_view(), name='EdificacaoTuristica_list_extension'),
    path('edificacao-turistica', EdificacaoTuristicaList.as_view(), name='EdificacaoTuristica_list'),
]