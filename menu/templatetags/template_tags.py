from django import template
from django.utils.safestring import mark_safe
from ..models import Menu

# Register this function as a template tag so it can be used in templates
register = template.Library()

# Define a custom template tag using Django's simple_tag decorator
@register.simple_tag(takes_context=True)
def draw_menu(context, table_name, level=1, parent=None):
    """
    This function takes a list of menu_items, a current url, a level (default=1), and a parent item (default=None)
    and returns a recursive HTML unordered list representing a tree menu.
    """
    # Get table from models using name of table
    menu_items = Menu.get_table(table_name)
    # menu_items = Menu.objects.using('default')
    # Get the current URL from the context object
    url = context['request'].path
    # If this is the first level of the menu, get the root menu items
    if level == 1:
        parent = menu_items.filter(parent='/')
    # Start building the HTML output
    output = '<ul class="nav nav-pills flex-column mb-auto">'
    # Loop through each menu item
    for item in parent:
        # Check if the current item is active (i.e., its full URL is in the current URL)
        is_active = item.full_url in url
        # Set the icon based on whether the item is active or not
        icon = "bi-dash-circle" if is_active else "bi-plus-circle"
        # Set the link based on whether the item is active or not
        link_href = item.parent if is_active else item.full_url
        # Set the 'active' class if the item is active
        active = 'active' if is_active else ''
        # Add the HTML for this menu item to the output string
        output += f'<li class="nav-item">' \
                    f'<a href="{link_href}" class="nav-link text-white {active}">' \
                    f'{"&nbsp;"*level*4}' \
                    f'<i class="bi {icon}"></i>' \
                    f' {item.title}</a>'

        # If this item is active, get its children (i.e., menu items that have this item as their parent)
        if item.full_url in url:
            # If the current URL has the same number of characters as the current level times 3, get the immediate children
            if len(url) == level*3: 
                children = menu_items.filter(parent=url)
            # Otherwise, get the children of the parent menu item
            else:
                children = menu_items.filter(parent=url[:level*3])
            # If there are children, recursively call this function to generate their HTML
            if children:
                output += draw_menu(context, table_name, level+1, children)

        # Close the HTML tag for this menu item
        output += '</li>'
    # Close the HTML tag for this level of the menu
    output += '</ul>'
    # If this is the first level of the menu, mark the output as safe for rendering in a template
    return mark_safe(output) if level == 1 else output