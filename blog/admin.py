from django.contrib import admin


from .models import touch
from .models import Blog
from .models import data
from .models import reg




admin.site.register(touch)
admin.site.register(Blog)
admin.site.register(data)
admin.site.register(reg)

