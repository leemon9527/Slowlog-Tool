# Generated by Django 2.0.6 on 2020-03-23 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysql_tools', '0003_mysqluploadfile_filesize'),
    ]

    operations = [
        migrations.CreateModel(
            name='MysqlProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='项目名称')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
        migrations.AddField(
            model_name='mysqluploadfile',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='uploadfile_project', to='mysql_tools.MysqlProject', verbose_name='项目'),
        ),
    ]
