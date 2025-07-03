from django.contrib import admin
from .models import JobRole, Question, Answer, Rating, Bookmark


admin.site.register(JobRole)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Rating)
admin.site.register(Bookmark)
