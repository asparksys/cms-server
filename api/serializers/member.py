from rest_framework import serializers
from member.models import MemberRole, Member


class MemberRoleSerializer(serializers.ModelSerializer):
    # member = serializers.RelatedField(read_only=True)

    class Meta:
        model = MemberRole
        fields = "__all__"
        read_only_fields = ("added_by",)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            "full_name",
            "gender",
            "dob",
            "education",
            "address",
            "role",
            "join_date",
            "full_name",
            "blood_group",
            "email",
            "address",
            "phone_number",
            "immediate_contact_number",
            "image",
        )
