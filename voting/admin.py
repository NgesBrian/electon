from django.contrib import admin

# Register your models here.

#from .models import User

#from .models import Login

from django.contrib.auth.models import User

from .models import Elections

from .models import Candidate

#admin.site.register(User)
#admin.site.register(Login)
admin.site.register(Elections)
admin.site.register(Candidate)