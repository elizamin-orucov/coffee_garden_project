import django_filters
from ..models import Product
from base.models import Category
from services.choices import PRODUCT_STATUS_CHOICES


class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    total_price = django_filters.RangeFilter(field_name="totalprice")
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
        queryset = super().filter_queryset(queryset)

        if category:
            queryset = queryset.filter(category__in=category.get_descendants(include_self=True))
        return queryset
