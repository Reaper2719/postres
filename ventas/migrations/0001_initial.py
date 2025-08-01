# Generated by Django 5.2.4 on 2025-07-29 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(choices=[('diego', 'Diego'), ('sahara', 'Sahara')], max_length=10)),
                ('sabor', models.CharField(choices=[('milo', 'Milo'), ('maracuya', 'Maracuyá'), ('limon', 'Limón'), ('mora', 'Mora'), ('lulo', 'Lulo')], max_length=10)),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
