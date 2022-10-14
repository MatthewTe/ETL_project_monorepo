from rest_framework import serializers

# Model imports:
from PROFILE_API.models import Profile, ProfileCategory

# Main Profile Seralizer:
class ProfileSerializer(serializers.ModelSerializer):
    # Specifying foregin key fields:
    category = serializers.SlugRelatedField(queryset=ProfileCategory.objects.all(), slug_field="name")

    class Meta:
        model = Profile
        fields = "__all__"

class ProfileCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCategory
        fields = "__all__"