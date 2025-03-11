from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView

from .models import Category


class IndexListView(ListView):
    model = Category
    template_name = 'goods/index_list.html'


class CategoryListView(ListView):
    template_name = 'goods/category.html'

    def get_queryset(self):
        self.category = get_object_or_404(
            Category,
            slug=self.kwargs.get('category_slug')
        )
        return self.category.goods.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
