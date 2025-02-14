from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import ListingForm

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

@login_required
def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            return redirect('listing_list')
    else:
        form = ListingForm()
    return render(request, 'listings/listing_form.html', {'form': form})

@login_required
def listing_update(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.user != listing.owner:
        return redirect('listing_list')

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'listings/listing_form.html', {'form': form})

@login_required
def listing_delete(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.user == listing.owner:
        listing.delete()
    return redirect('listing_list')
from django.shortcuts import render
from .models import Listing

def home(request):
    listings = Listing.objects.all()  # Получаем все объявления
    return render(request, 'home.html', {'listings': listings})
