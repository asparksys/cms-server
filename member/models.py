from django.db import models
from ums.models import User
from club.models import BranchClub


class BaseModel:
    date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    club_id = models.ForeignKey(BranchClub, on_delete=models.CASCADE)


class MemberRole(BaseModel, models.Model):
    name = models.CharField(max_length=255, blank=False, default=None)


class Member(BaseModel, models.Model):
    BLOOD_GROUPS = [("unknown", "Unknown"), ("A+","A+"), ("A-", "A-"), ("B+", "B+"), ("B-","B-"), ("O+","O+"), ("O-", "O-"), ("AB+", "AB+"), ("AB-", "AB-")]
    GENDERS = [('unknown',"Unknown"), ('male',"Male"), ('female',"Female")]
    EDUCATION_LEVELS = [
        ('see/slc',"SEE/SLC"),
        ('+2',"+2"),
        ('bachelors',"Bachelors"),
        ('masters',"Masters"),
        ('mphil',"MPhil"),
        ('phd',"PhD"),
        ('others',"Others"),
    ]

    full_name = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDERS, max_length=30)
    dob = models.DateField()
    education = models.CharField(max_length=255, choices=EDUCATION_LEVELS)
    address = models.CharField(max_length=255, null=True)
    role = models.ForeignKey(MemberRole, on_delete=models.CASCADE)
    join_date = models.DateField()
    full_name = models.CharField(max_length=255, default=None)
    blood_group = models.CharField(max_length=50,choices=BLOOD_GROUPS)
    email = models.EmailField(max_length=255, default="info@asparksys.com")
    address = models.CharField(max_length=255, default=None)
    phone_number = models.CharField(max_length=255, default=None)
    immediate_contact_number = models.CharField(max_length=255, default=None)
    image = models.URLField(max_length=2048, default="https://picsum.photos/200")
