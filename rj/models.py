# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models
from hyper_resource.models import FeatureModel

class EdificacaoTuristica(FeatureModel):
    gid = models.AutoField(primary_key=True)
    id_objeto = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=254, blank=True, null=True)
    nomeabrev = models.CharField(max_length=254, blank=True, null=True)
    geometriaa = models.CharField(max_length=254, blank=True, null=True)
    tipoediftu = models.CharField(max_length=254, blank=True, null=True)
    ovgd = models.CharField(max_length=254, blank=True, null=True)
    operaciona = models.CharField(max_length=254, blank=True, null=True)
    situacaofi = models.CharField(max_length=254, blank=True, null=True)
    matconstr = models.CharField(max_length=254, blank=True, null=True)
    id_produto = models.IntegerField(blank=True, null=True)
    id_element = models.IntegerField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edificacao_turistica'
