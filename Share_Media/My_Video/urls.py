from  django.urls  import  path
from My_Video import views
from .views import CollectionDetailView, CollectionListView, CollectionLike, CollectionDisLike 


urlpatterns =[
path('', CollectionListView.as_view(), name= 'CollectionListView'),
path('<int:pk>/', CollectionDetailView.as_view(), name='CollectionDetailView'),
path('collection-like/<int:pk>', views.CollectionLike, name="collection_like"),
path('collection-dislike/<int:pk>', views.CollectionDisLike, name="collection_dislike")
]
