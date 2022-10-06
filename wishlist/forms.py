from pyexpat import model
from django.forms import ModelForm
from wishlist.models import BarangWishlist

class WishlistFormAjax(ModelForm):
    class Meta:
        model = BarangWishlist
        fields = ['nama_barang','harga_barang','deskripsi']

