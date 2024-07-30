# Generated by Django 4.2.2 on 2024-07-30 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0010_empresa_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='alterado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categoria_atualizada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='cadastrado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categoria_cadastrada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='alterado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='empresa_atualizada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='cadastrado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='empresa_cadastrada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='alterado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='produto_atualizado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='produto',
            name='cadastrado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='produto_cadastrado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='promocao',
            name='alterado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='promocao_atualizada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='promocao',
            name='cadastrado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='promocao_cadastrada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='alterado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subcategoria_atualizada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='cadastrado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subcategoria_cadastrada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='venda',
            name='alterado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='venda_atualizada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='venda',
            name='cadastrado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='venda_cadastrada', to=settings.AUTH_USER_MODEL),
        ),
    ]
