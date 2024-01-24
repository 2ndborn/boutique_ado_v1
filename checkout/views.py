from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Oc83ICQB35zR1MG3qlioVb61chdUlOJ9KxA47cFmYlu6ofvG1CgkKrIdWxLmuZVe1skHNMkJvStuOCpViOvX83Z00I7UtecwD',
        'client_secret': 'test client secret',
    }

    return render(request, 'checkout/checkout.html', context)