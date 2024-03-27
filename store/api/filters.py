import django_filters
from ..models import Product
from django.db.models import Q
from base.models import Category
from services.choices import PRODUCT_STATUS_CHOICES


class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(label="search")
    total_price = django_filters.RangeFilter(field_name="totalprice", label="total price range")
    category = django_filters.ModelChoiceFilter(field_name="category", queryset=Category.objects.all())
    status = django_filters.ChoiceFilter(field_name="status", choices=PRODUCT_STATUS_CHOICES)

    class Meta:
        model = Product
        fields = (
            "search",
            "category",
            "status",
            "total_price"
        )

    def filter_queryset(self, queryset):
        category = self.form.cleaned_data.pop("category")
        search = self.form.cleaned_data.pop("search")
        queryset = super().filter_queryset(queryset)
        if category:
            queryset = queryset.filter(category__in=category.get_descendants(include_self=True))
        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(category__name__icontains=search))
        return queryset
