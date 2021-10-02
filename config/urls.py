"""The URLconf of the config app."""

from importlib.util import find_spec

from django.contrib.flatpages.views import flatpage
from django.urls import path

info_page = flatpage
if find_spec('csp'):  # pragma: no cover
    from csp.decorators import csp_update
    info_page = csp_update(
        style_src="'unsafe-inline'",
        img_src="https:"
    )(flatpage)

info_page.__doc__ = """
| Alias for :func:`django.contrib.flatpages.views.flatpage`.
| If ``django-csp`` is installed, this is configured
  to allow custom styles & images in the page.
"""

#: The URL patterns of the config app.
urlpatterns = [
    path('info/', info_page, {'url': '/info/'}, name='info'),
    path('privacy/', info_page, {'url': '/privacy/'}, name='privacy'),
]

__all__ = ['info_page', 'urlpatterns']
