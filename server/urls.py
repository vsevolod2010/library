from .api import router
from django.urls import path, include
from .views import BookListView, SearchBookListView, statistic, authors_count, books_count


urlpatterns = [
    path('api/v0/', include(router.urls)),
    path('library/', BookListView.as_view()),
    path('statistic/', statistic),
    path('statistic/authors/', authors_count),
    path('statistic/books/', books_count),
    path('library/search/', SearchBookListView.as_view())
]
