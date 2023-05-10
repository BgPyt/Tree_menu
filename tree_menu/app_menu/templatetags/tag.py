from django import template
from app_menu.models import Menu, Items
register = template.Library()

@register.inclusion_tag('app_menu/includes/menu.html', takes_context=True)
def draw_menu(context, main_menu):
    menu = Items.objects.all().filter(menu_name__title=main_menu).select_related('parent').order_by('url')
    result = ''
    object_prev = None
    last_obj = None
    object_static = main_menu
    closed_tag = ''
    for item in menu:
        # if item.parent == object_static:
        #     result += f"<li><a href='{item.url}'>{item}</a>"
        #     object_prev = item
        if item.parent == object_prev:
            result += f"<ul><li><a href='{item.title_slug}'>{item}</a>"
            closed_tag += "</ul>"
            object_prev = item
        else:
            # if item.parent == object_static:
            #     result += closed_tag + f"</ul><a href='{item.url}'>{item}</a>"
            #     object_prev = item
            # else:
                if closed_tag:
                    result += (len(object_prev.url.split('/')) - len(
                        item.url.split('/'))) * '</ul>' + f"<li><a href='{item.title_slug}'>{item}</a>"
                else:
                    result += closed_tag + f"<li><a href='{item.title_slug}'>{item}</a>"
                object_prev = item
        last_obj = item

    result += len(last_obj.url.split('/')) * '</ul>'




    return {"html_menu": result,
            "name_menu": main_menu,
            }





