from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item


def bag_contents(request):

    bag_products = []
    total = 0
    item_count = 0
    bag = request.session.get('bag', {})

    for product_id, quantity in bag.items():
        if isinstance(quantity, int):
            item = get_object_or_404(Item, pk=product_id)
            total += quantity * item.price
            item_count += quantity
            bag_products.append({
                'product_id': product_id,
                'quantity': quantity,
                'item': item,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_products': bag_products,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
