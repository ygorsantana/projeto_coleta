# Generated by Django 2.2.4 on 2020-05-31 17:47

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=120)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='OrgaoPublico',
            fields=[
                ('endereco_apelido', models.CharField(max_length=120)),
                ('cep', models.CharField(max_length=20, null=True)),
                ('endereco', models.CharField(max_length=100, null=True)),
                ('bairro', models.CharField(max_length=80, null=True)),
                ('numero_casa', models.IntegerField(null=True)),
                ('localizacao_geografica', django.contrib.gis.db.models.fields.PointField(help_text='Pontos de Latitude e Longitude', srid=4326)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=120)),
                ('documento', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PontoColeta',
            fields=[
                ('endereco_apelido', models.CharField(max_length=120)),
                ('cep', models.CharField(max_length=20, null=True)),
                ('endereco', models.CharField(max_length=100, null=True)),
                ('bairro', models.CharField(max_length=80, null=True)),
                ('numero_casa', models.IntegerField(null=True)),
                ('localizacao_geografica', django.contrib.gis.db.models.fields.PointField(help_text='Pontos de Latitude e Longitude', srid=4326)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=2)),
                ('item', models.ManyToManyField(to='core.Item')),
                ('orgao', models.ManyToManyField(to='core.OrgaoPublico')),
                ('uf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.UF')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('endereco_apelido', models.CharField(max_length=120)),
                ('cep', models.CharField(max_length=20, null=True)),
                ('endereco', models.CharField(max_length=100, null=True)),
                ('bairro', models.CharField(max_length=80, null=True)),
                ('numero_casa', models.IntegerField(null=True)),
                ('localizacao_geografica', django.contrib.gis.db.models.fields.PointField(help_text='Pontos de Latitude e Longitude', srid=4326)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=120)),
                ('documento', models.CharField(max_length=15)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=20)),
                ('pontuacao', models.DecimalField(decimal_places=2, max_digits=10)),
                ('uf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.UF')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='orgaopublico',
            name='uf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.UF'),
        ),
    ]
