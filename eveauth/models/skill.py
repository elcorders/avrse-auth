from django.db import models

from eveauth.models.character import Character
from sde.models import Type


class Skill(models.Model):
    character = models.ForeignKey(Character, related_name="skills")
    type = models.ForeignKey(Type)
    trained_skill_level = models.IntegerField()
    active_skill_level = models.IntegerField()
    skillpoints_in_skill = models.IntegerField()

    @property
    def rank(self):
        return int(self.type.attributes.get(attribute_id=275).value)
