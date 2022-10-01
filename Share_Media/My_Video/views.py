from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from .models import Collection
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


class CollectionListView(ListView):
    model = Collection
    context_object_name = 'collections'
    template_name = 'collection_list.html'


class CollectionDetailView(HitCountDetailView):
    model = Collection
    template_name = 'collection_detail.html'
    context_object_name = 'collection'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        likes_connected = get_object_or_404(Collection, id=self.kwargs['pk'])
        dislikes_connected = get_object_or_404(Collection, id=self.kwargs['pk'])
        liked = False
        disliked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        if dislikes_connected.dislikes.filter(id=self.request.user.id).exists():
            disliked = True
        context['number_of_likes'] = likes_connected.number_of_likes()
        context['number_of_dislikes'] = dislikes_connected.number_of_dislikes()
        context['collection_is_liked'] = liked
        context['collection_is_disliked'] = disliked
        context['user_likes'] = likes_connected.user_likes()
        context['user_dislikes'] = dislikes_connected.user_dislikes()
        context.update({'popular_videos': Collection.objects.order_by('-hit_count_generic__hits')[:3], })
        return context


def CollectionLike(request, pk):
    user = User.objects.get(username=request.user.username)
    collection = get_object_or_404(Collection, id=request.POST.get('collection_id'))
    if collection.likes.filter(id=request.user.id).exists():
        collection.likes.remove(request.user)
    else:
        collection.likes.add(request.user)

    return HttpResponseRedirect(reverse('collection_detail', args=[str(pk)]))


def CollectionDisLike(request, pk):
    collection = get_object_or_404(Collection, id=request.POST.get('collection_id'))
    if collection.dislikes.filter(id=request.user.id).exists():
        collection.dislikes.remove(request.user)
    else:
        collection.dislikes.add(request.user)

    return HttpResponseRedirect(reverse('collection_detail', args=[str(pk)]))

