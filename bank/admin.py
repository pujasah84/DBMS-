from django.contrib import admin
# from .models import Branch

# admin.site.register(Branch)

from django.apps import apps


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except:
        pass
