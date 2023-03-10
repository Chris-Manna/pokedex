from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.cache import cache

class User(AbstractUser):
  following = models.ManyToManyField("User", related_name="followers")


class Post(models.Model):
  content = models.TextField()
  creation_time = models.DateTimeField(auto_now_add=True)
  poster = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")

class Monster(models.Model):
  evolution_instances = []
  monster_id = models.TextField()
  name = models.TextField()
  types = models.TextField()
  weaknesses = models.TextField()
  trainer = models.ForeignKey("User", on_delete=models.CASCADE, related_name="trains")
  evolutions = models.TextField(default="")
  
  def __str__(self):
    return f"{self.monster_id}"
  
  def get_strong_against(self):
    strong_against = []
    for strength in self.types.split(","):
      monsters_strong_against = Monster.objects.filter(weaknesses__icontains=strength)
      strong_against += [obj.name for obj in monsters_strong_against]
    separator = ', '
    strong_against_string = separator.join(strong_against)
    
    # types_spreader = ", ".join(self.types.split(","))
    # return f"{types_spreader} types. Ex: {strong_against_string}"
    
    if len(strong_against_string) > 0:
      types_prettier = ", ".join(self.types.split(","))
      return f"{types_prettier} types. Ex: {strong_against_string}"
    else: 
      return self.types
  
  
  def get_monsters_weak_against(self):
    weak_against = []
    for weakness in self.weaknesses.split(","):
      monsters_weak_against = Monster.objects.filter(types__icontains=weakness)
      weak_against += [obj.name for obj in monsters_weak_against]
    separator = ', '
    weak_against = separator.join(weak_against)
    if len(weak_against) > 0:
      return f"{self.weaknesses} types. Ex: {weak_against}"
    else: 
      return self.weaknesses
  
  
  def get_children(self, lineage = ""):
    children = []
    monster = Monster.objects.get(monster_id=self.monster_id)
    
    def get_children_helper(monster = None, lineage=""):
      evolutions_list = monster.evolutions.split(",")
      if len(lineage) > 0:
        lineage += f" > {monster.name}"
      else:
        lineage = monster.name
      
      if len(evolutions_list) == 0 or evolutions_list == [""]:
        return lineage
      
      for child_id in evolutions_list:
        child = Monster.objects.get(monster_id = child_id)
        future_generations = get_children_helper(child, lineage)
        children.append(future_generations)
    get_children_helper(monster)
    children = list(filter(lambda x: x != None, children))
    if len(children) == 0:
      return ["None"]
    return children