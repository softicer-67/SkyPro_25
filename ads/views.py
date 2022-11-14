# -*- coding: utf8 -*-
import json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DetailView

from .models import Ads, Cat


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        ads_view = request.GET.get('ads_view')
        if ads_view:
            object_list = self.object_list(ads_view)

        response = []
        for ads in self.object_list:
            response.append({
                'id': ads.id,
                'name': ads.name,
                'author': ads.author,
                'price': ads.price,
                'description': ads.description,
                'address': ads.address,
                'is_published': ads.is_published
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)
        ad = Ads.objects.create(
                name=ads_data['name'],
                author=ads_data['author'],
                price=ads_data['price'],
                description=ads_data['description'],
                address=ads_data['address'],
                is_published=ads_data['is_published']
               )
        ad.save()

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published
        })


@method_decorator(csrf_exempt, name='dispatch')
class CatView(ListView):
    model = Cat

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        cat_view = request.GET.get('cat_view')
        if cat_view:
            object_list = self.object_list(cat_view)

        response = []
        for c in self.object_list:
            response.append({
                'id': c.id,
                'name': c.name,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        cat_data = json.loads(request.body)
        try:
            cat = Cat.objects.create(
                name=cat_data['name']
               )
        except Exception:
            return JsonResponse({'error': 'Такая категория уже используется'}, status=500)

        cat.save()
        return JsonResponse({
            'id': cat.id,
            'name': cat.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            ads = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)

        return JsonResponse({
            'id': ads.id,
            'name': ads.name,
            'author': ads.author,
            'price': ads.price,
            'description': ads.description,
            'address': ads.address,
            'is_published': ads.is_published
        })


@method_decorator(csrf_exempt, name="dispatch")
class CatDetailView(DetailView):
    model = Cat

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Not found'}, status=404)

        return JsonResponse({
            'id': ad.id,
            'name': ad.name
        })
