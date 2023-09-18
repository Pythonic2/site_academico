from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.HomePage.as_view(), name='home_page'),
    path('blog/',views.BlogPage.as_view(), name='blog'),
    path('blog/post/<str:titulo>/', views.PostPage.as_view(), name='detalhes_item'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)