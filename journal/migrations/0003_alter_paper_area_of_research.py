# Generated by Django 5.0.2 on 2025-05-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_rename_author_paper_author_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='area_of_research',
            field=models.CharField(choices=[('engineering', 'Engineering'), ('sci_tech', 'Science & Technology'), ('pharmacy', 'Pharmacy'), ('science', 'Science (Physics/Chemistry/Maths/Biology)'), ('commerce', 'Commerce'), ('economics', 'Economics'), ('management', 'Management'), ('hospitality', 'Hospitality and Tourism'), ('arts', 'Arts'), ('medical', 'Medical Science'), ('life_science', 'Life Sciences'), ('health_medical', 'Health & Medical Science'), ('social_science', 'Social Science and Humanities'), ('law', 'LAW & Education'), ('biotech', 'Biotechnology')], default='engineering', max_length=50),
        ),
    ]
