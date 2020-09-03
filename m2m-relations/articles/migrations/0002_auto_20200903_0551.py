# Generated by Django 2.2.10 on 2020-09-03 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Тег')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='ArticleHasTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основной')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='Статья')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Tag', verbose_name='Тег')),
            ],
        ),
        migrations.AddConstraint(
            model_name='articlehastag',
            constraint=models.UniqueConstraint(fields=('article', 'tag'), name='article_tag'),
        ),
    ]