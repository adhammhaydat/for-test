from rest_framework import serializers
from .models import Post,Offer,Comment,Activity


        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ('created_at',)
        model = Post
        fields = "__all__"


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ('created_at',)
        model = Offer
        fields = "__all__"



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ('created_at',)
        model = Comment
        fields = "__all__"        


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ('created_at',)
        model = Activity
        fields = "__all__"    