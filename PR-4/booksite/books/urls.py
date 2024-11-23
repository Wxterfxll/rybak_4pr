from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BookList, BookDetail, BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]

urlpatterns += router.urls