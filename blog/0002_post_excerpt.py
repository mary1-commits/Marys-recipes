from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('blog', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]