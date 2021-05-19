from django.db import models


class HeadClub(models.Model):
    name = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class BranchClub(models.Model):
    # general details
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    head = models.ForeignKey(HeadClub, on_delete=models.CASCADE)
    parent_club = models.CharField(max_length=255, blank=False, default=None)
    club_id = models.CharField(
        max_length=255, blank=True, default=None, null=True
    )
    motto = models.CharField(
        max_length=255, null=False, blank=False, default=None
    )
    chartered_date = models.DateField()

    # contact info
    email = models.EmailField(blank=False, default=None)

    # social media
    website = models.URLField(
        max_length=2048, default="https://asparksys.com", blank=True
    )
    instagram = models.URLField(
        max_length=2048,
        default="hittps://instagram.com/asparksystems",
        blank=True,
    )
    facebook = models.URLField(
        max_length=2048, default="https://facebook.com/aspaksys", blank=True
    )
    twitter = models.URLField(
        max_length=2048, default="https://twitter.com/asparksys", blank=True
    )

    # appearance
    color_code = models.CharField(max_length=50, default="black", blank=False)
    logo = models.URLField(
        max_length=2048,
        default="https://4m4you.com/wp-content/uploads/2020/06/logo-placeholder.png",
    )

    def __str__(self):
        return self.name
