from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.conf.urls.static import static
from django.conf import settings
# from graphql_jwt.decorators import jwt_cookie
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)