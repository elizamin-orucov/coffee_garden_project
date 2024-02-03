from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.api.urls")),
]

# urlpatterns += i18n_patterns(
#     # path('settings/', include('settings.urls')),
#     path('', include('products.api.urls')),
# )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
