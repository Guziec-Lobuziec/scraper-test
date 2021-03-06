# Generated by Django 2.1.7 on 2019-04-09 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('url', models.TextField(primary_key=True, serialize=False)),
                ('full_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AuthorStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occurance_count', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.Author')),
            ],
            options={
                'ordering': ['author', '-occurance_count'],
            },
        ),
        migrations.CreateModel(
            name='GloballStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occurance_count', models.IntegerField()),
            ],
            options={
                'ordering': ['-occurance_count'],
            },
        ),
        migrations.CreateModel(
            name='StatsVersion',
            fields=[
                ('version_number', models.AutoField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('ready', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('word_of_interest', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='globallstatistic',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.StatsVersion'),
        ),
        migrations.AddField(
            model_name='globallstatistic',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.Word'),
        ),
        migrations.AddField(
            model_name='authorstatistic',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.StatsVersion'),
        ),
        migrations.AddField(
            model_name='authorstatistic',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.Word'),
        ),
    ]
