from django import template

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 

@register.filter(name='has_not_group') 
def has_group(user, group_name):
    has = user.groups.filter(name=group_name).exists()
    return (not has)