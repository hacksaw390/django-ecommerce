from .models import *


def categories(request):
    all_category = Category.objects.all()
    all_tag = Tag.objects.all()
    context = {'all_category': all_category, 'all_tag': all_tag}
    return context
