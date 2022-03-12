from django.urls import path

from product.views import ProductListView, product_detail

urlpatterns = [
    path("products", ProductListView.as_view(),name='product-list'),
    path('product-detail/<int:pk>/',product_detail,name='product-detail'),
    # path("products/search", Search.as_view()),
    # path("products/special", ProductSpecial.as_view()),
    # path("products/new", ProductNew.as_view()),
    # path("products/most_popular", ProductMostPopular.as_view()),
    # path("products/<productId>/<title>", product_detail),
]