# Generated by Django 5.0.2 on 2024-02-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_etf_yf_e_score_etf_yf_g_score_etf_yf_s_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='yf_total_esg_score',
            new_name='yf_e_score',
        ),
        migrations.RenameField(
            model_name='etf',
            old_name='yf_total_esg_score',
            new_name='yf_t_score',
        ),
        migrations.AddField(
            model_name='company',
            name='yf_g_score',
            field=models.FloatField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='yf_s_score',
            field=models.FloatField(default=-1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='yf_t_score',
            field=models.FloatField(default=-1),
            preserve_default=False,
        ),
    ]
