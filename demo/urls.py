from django.contrib import admin
from django.urls import path
from apps.core.views import *
from apps.blog.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),
    # STORE
    path('', hjemme, name='hjemme'),
    # BLOG
    path('blogg/', blog, name='blog'),
    # PAGES
        # INFO
        path('info/', info, name='info'),
        path('apningstider/', openhours, name='openhours'),
        path('regler/', rules, name='rules'),
        path('om-oss/', about, name='about'),
        path('sponsorer/', sponsors, name='sponsors'),
        path('foreldre-info/', parent, name='parent'),
        # TJENESTER
        path('lan-og-bd/', lan, name='lan'),
        path('leie-utstyr/', rent_items, name='rent_items'),
        path('leie-lokalet/', rent_place, name='rent_place'),
        path('skoleundervisning/', school, name='school'),
        # ESPORT
        path('e-sport-kurser/', esport_course, name='esport_course'),
        path('e-sport-events/', events, name='events'),
        path('esport-galleri/', esport_galleri, name='esport_galleri'),
        path('spill-og-konsoller/', spill_konsoller, name='spill_konsoller'),
        path('turneringer/', turneringer, name='turneringer'),
        # KUNST
        path('kunst-kurs/', art_course, name='art_course'),
        path('kunst-galleri/', art_galleri, name='art_galleri'),
        path('vår-avdeling/', our_art, name='our_art'),
        # KONTAKT
        path('kontakt-oss/', contact, name='contact'),
        # PRISER
        path('priser/', prices, name='prices'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
