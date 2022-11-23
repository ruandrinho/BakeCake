# Generated by Django 3.2.7 on 2022-11-23 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cakeberry',
            options={'verbose_name': 'Ягода', 'verbose_name_plural': '  Ягоды'},
        ),
        migrations.AlterModelOptions(
            name='cakedecor',
            options={'verbose_name': 'Декор', 'verbose_name_plural': ' Декоры'},
        ),
        migrations.AlterModelOptions(
            name='cakeform',
            options={'verbose_name': 'Форма торта', 'verbose_name_plural': '    Формы тортов'},
        ),
        migrations.AlterModelOptions(
            name='cakesize',
            options={'verbose_name': 'Размер торта', 'verbose_name_plural': '     Размеры тортов'},
        ),
        migrations.AlterModelOptions(
            name='caketopping',
            options={'verbose_name': 'Топпинг', 'verbose_name_plural': '   Топпинги'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': '       Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': '      Заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='cake_caption',
            field=models.CharField(blank=True, max_length=200, verbose_name='Надпись'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_comment',
            field=models.TextField(blank=True, verbose_name='Комментарий для курьера'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_comment',
            field=models.TextField(blank=True, verbose_name='Комментарий к заказу'),
        ),
    ]