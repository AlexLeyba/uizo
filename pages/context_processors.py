from pages.models import Page, CategoryPageModel


def get_pages(request):
    try:
        page = Page.objects.all()
        return {'page': page}
    except:
        pass


def get_category(request):
    try:
        category = CategoryPageModel.objects.all()
        return {'category': category}
    except:
        pass
