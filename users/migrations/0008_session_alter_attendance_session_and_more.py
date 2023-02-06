# Generated by Django 4.0.3 on 2023-02-04 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_attendance_session_alter_student_session_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='attendance',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.session'),
        ),
        migrations.AlterField(
            model_name='student',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.session'),
        ),
        migrations.DeleteModel(
            name='Sessions',
        ),
    ]
