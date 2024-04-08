from django.urls import path, include

urlpatterns = [
    path('depot/', include("depot.urls")),
    path('accounts/', include("accounts.urls")),
]
