# Generated by Django 4.2.11 on 2024-04-23 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readdb', '0003_rename_section_id_section_section_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='takes',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='takes',
            name='course',
            field=models.ForeignKey(default='XXXXX', on_delete=django.db.models.deletion.CASCADE, to='readdb.course'),
        ),
        migrations.AlterField(
            model_name='takes',
            name='grade',
            field=models.CharField(default='B', max_length=2),
        ),
        migrations.AlterField(
            model_name='takes',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='readdb.section'),
        ),
        migrations.AlterField(
            model_name='takes',
            name='semester',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='takes',
            name='student',
            field=models.ForeignKey(default=99999, on_delete=django.db.models.deletion.CASCADE, to='readdb.student'),
        ),
        migrations.AlterField(
            model_name='takes',
            name='year',
            field=models.IntegerField(default=2024),
        ),
        migrations.AlterUniqueTogether(
            name='takes',
            unique_together={('student', 'course', 'section', 'semester', 'year')},
        ),
    ]
