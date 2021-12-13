from django.contrib import admin
from .models import Post,Comment,Offer,Activity
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Offer)
admin.site.register(Activity)
