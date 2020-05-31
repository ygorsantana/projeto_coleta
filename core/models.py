# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create,
#   modify, and delete the table
# Feel free to rename the models, but don't rename db_table
# values or field names.
import uuid

from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.gis.db import models as _models


# class Product(PostgresModel):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4
#     )

#     store = models.ForeignKey(
#         'Store',
#         models.CASCADE,
#     )

#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     updated_at = models.DateTimeField(
#         auto_now=True
#     )

#     name = models.CharField(
#         max_length=255,
#     )

#     middleware_name = models.CharField(
#         max_length=255,
#         default=''
#     )

#     code = models.CharField(
#         max_length=255,
#     )

#     stock_control = models.BooleanField(
#         default=False
#     )

#     ean_code = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True
#     )

#     extra_fields = JSONField(
#         blank=True,
#         null=True
#     )

#     category = models.ForeignKey(
#         'Category',
#         models.PROTECT,
#         blank=True,
#         null=True
#     )

#     images = ArrayField(
#         models.CharField(
#             max_length=512,
#         ),
#         null=True,
#         blank=True,
#     )

#     is_active = models.BooleanField(
#         default=False
#     )

#     def __str__(self):
#         return self.name


# class Erp(PostgresModel):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4
#     )

#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


# class Mapping(PostgresModel):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4
#     )

#     field = JSONField(
#         verbose_name='Mapeamento'
#     )

#     erp = models.ForeignKey(
#         'Erp',
#         on_delete=models.CASCADE,
#         verbose_name='ERP'
#     )

#     headers = ArrayField(
#         models.CharField(max_length=50)
#     )

#     def __str__(self):
#         return str(self.field)


# class Category(PostgresModel):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4
#     )

#     store = models.ForeignKey(
#         'Store',
#         on_delete=models.CASCADE
#     )

#     name = models.CharField(
#         max_length=255
#     )

#     code = models.IntegerField()

#     extra = JSONField(
#         null=True,
#         blank=True
#     )

#     def __str__(self):
#         return self.name


# class Shopping(PostgresModel):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4
#     )

#     name = models.CharField(
#         max_length=255
#     )

#     extra = JSONField(
#         null=True,
#         blank=True
#     )

#     class Meta:
#         permissions = (
#             ('has_shopping', 'Has the shopping'),
#         )

#     def __str__(self):
#         return self.name


# class Store(PostgresModel):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4
#     )

#     name = models.CharField(
#         max_length=255
#     )

#     token = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True
#     )

#     reference_code = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True
#     )

#     erps = models.ManyToManyField(
#         Erp,
#         through='StoreErp',
#         through_fields=('store', 'erp'),
#     )

#     min_stock = models.IntegerField(
#         default=5
#     )

#     shopping = models.ForeignKey(
#         Shopping,
#         on_delete=models.CASCADE
#     )

#     extra = JSONField(
#         null=True,
#         blank=True
#     )

#     class Meta:
#         permissions = (
#             ('has_store', 'Has the store'),
#         )

#     def __str__(self):
#         return self.name


# class StoreErp(PostgresModel):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4
#     )

#     store = models.ForeignKey(
#         'Store',
#         on_delete=models.CASCADE
#     )

#     erp = models.ForeignKey(
#         'Erp',
#         on_delete=models.CASCADE
#     )

#     def __str__(self):
#         return self.store


# class Sku(PostgresModel):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4
#     )

#     name = models.CharField(
#         max_length=255,
#     )

#     master = models.IntegerField(
#         default=0,
#     )

#     code = models.CharField(
#         max_length=255,
#         unique=True
#     )

#     color = models.CharField(
#         max_length=255,
#         blank=True
#     )

#     price = models.DecimalField(
#         max_digits=10,
#         decimal_places=2
#     )

#     size = models.CharField(
#         max_length=20,
#         blank=True,
#     )

#     amount = models.IntegerField(
#         blank=True,
#         null=True,
#         default=0
#     )

#     product = models.ForeignKey(
#         Product,
#         models.CASCADE
#     )

#     extra = JSONField(
#         null=True,
#         blank=True
#     )

#     def __str__(self):
#         return self.name


class EnderecoAbstrato(models.Model):
    endereco_apelido = models.CharField(
        max_length=120,
    )
    cep = models.CharField(
        max_length=20,
        null=True,
    )
    uf = models.ForeignKey(
        "UF",
        on_delete=models.SET_NULL,
        null=True,
    )
    endereco = models.CharField(
        max_length=100,
        null=True,
    )
    bairro = models.CharField(
        max_length=80,
        null=True,
    )
    numero_casa = models.IntegerField(
        null=True,
    )
    localizacao_geografica = _models.PointField(
        help_text="Pontos de Latitude e Longitude"
    )

    class Meta:
        abstract = True
    
    def __str__(self):
        return "{} - {}".format(self.endereco_apelido, self.cep)


class Pessoa(EnderecoAbstrato):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )
    nome = models.CharField(
        max_length=120,
    )
    documento = models.CharField(
        max_length=15,
    )
    data_nascimento = models.DateField()
    sexo = models.CharField(
        max_length=10,
    )
    telefone = models.CharField(
        max_length=20,
    )
    usuario = models.ForeignKey(
        "account.User",
        on_delete=models.CASCADE
    )
    pontuacao = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )


class UF(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )
    nome = models.CharField(
        max_length=2,
    )


class OrgaoPublico(EnderecoAbstrato):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )
    nome = models.CharField(
        max_length=120,
    )
    documento = models.CharField(
        max_length=15,
    )
    email = models.EmailField()
    telefone = models.CharField(
        max_length=20,
    )


class PontoColeta(EnderecoAbstrato):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )
    nome = models.CharField(
        max_length=2,
    )
    item = models.ManyToManyField(
        "Item"
    )
    orgao = models.ManyToManyField(
        "OrgaoPublico"
    )


class Item(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )
    nome = models.CharField(
        max_length=120,
    )
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    categoria = models.ForeignKey(
        "Categoria",
        on_delete=models.SET_NULL,
        null=True,
    )


class Categoria(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )
    nome = models.CharField(
        max_length=120,
    )
