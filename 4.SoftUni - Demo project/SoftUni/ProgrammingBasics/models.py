from django.db import models


class Lecture(models.Model):
    Index = models.IntegerField(null=False)
    Title = models.CharField(max_length=50, null=False, help_text="Lecture title")
    Description = models.TextField(null=False, help_text=
                                   "Short description about the lecture.<br> \
                                   - for new line use &lt;br&gt;<br> \
                                   - supports html"
                                   )
    Resources = models.TextField(null=True, blank=True, help_text="Links. Html only...")

