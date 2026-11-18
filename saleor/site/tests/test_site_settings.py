import pytest
from django.contrib.sites.models import Site
from django.core.exceptions import ImproperlyConfigured

from ..models import MAX_LINE_QUANTITY_HINT, SiteSettings


def test_new_get_current():
    result = Site.objects.get_current()
    assert result.name == "example.com"
    assert result.domain == "example.com"
    assert type(result.settings) is SiteSettings


def test_site_settings_default_from_email(settings):
    site = Site.objects.get_current()
    site.settings.default_mail_sender_address = None
    assert site.settings.default_from_email == settings.DEFAULT_FROM_EMAIL
    settings.DEFAULT_FROM_EMAIL = None
    with pytest.raises(ImproperlyConfigured):
        _x = site.settings.default_from_email


def test_max_line_quantity_hint_value():
    """Dashboard mirrors MAX_LINE_QUANTITY_HINT; changing it requires updating both repos."""
    assert MAX_LINE_QUANTITY_HINT == 50
