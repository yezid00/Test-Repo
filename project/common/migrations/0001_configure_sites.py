
from django.conf import settings
from django.db import migrations

def configure_sites(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    default_site, _ = Site.objects.get_or_create(id=1)
    default_site.name = settings.APP_NAME
    default_site.domain = settings.SITE_URL
    default_site.save()

def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(
            configure_sites,
            noop
        )
    ]

