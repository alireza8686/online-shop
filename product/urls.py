from django.urls import path

from product.views import ProductListView, ProductMostPopular, ProductNew, SpecialProducts, product_detail

urlpatterns = [
    path("products", ProductListView.as_view(),name='product-list'),
    path('product-detail/<int:pk>/',product_detail,name='product-detail'),
    # path("products/search", Search.as_view()),
    path("products/special", SpecialProducts.as_view(),name='special-products'),
    path("products/new", ProductNew.as_view(),name='new-products'),
    path("products/most_popular", ProductMostPopular.as_view(),name='popular-products'),
    # path("products/<productId>/<title>", product_detail),
]