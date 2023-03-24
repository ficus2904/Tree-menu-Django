# Custom Django Template Tag for Generating a Tree Menu
This is a custom Django template tag that generates a tree menu using the Menu model from your Django app.

## Usage
1. Add the `draw_menu` function to your app's `templatetags` directory, in a file called `menu_tags.py`.

2. In any Django template where you want to use the tree menu, include the following at the top of the file:

```django
{% load menu_tags %}
```

3. To generate the tree menu in the template, use the `draw_menu` template tag as follows:

```django
{% draw_menu table_name %}
```

Where `table_name` is the name of the table in the Menu model that you want to use to generate the tree menu.

By default, the `draw_menu` template tag will generate a menu with a depth of 1 (i.e., only the top-level menu items). You can also specify a different depth by passing the `level` parameter:

```django
{% draw_menu table_name level=2 %}
```

This will generate a menu with a depth of 2 (i.e., top-level and second-level menu items).

## Logic
The `draw_menu` function takes a list of menu items, a current URL, a level (default=1), and a parent item (default=None), and returns a recursive HTML unordered list representing a tree menu.

The function first gets the Menu model using the name of the table. If this is the first level of the menu, it gets the root menu items (i.e., items with a parent of '/'). It then loops through each menu item and generates the HTML for that item.

For each menu item, the function checks if it is active (i.e., its full URL is in the current URL), sets the icon and link based on whether the item is active or not, and adds the HTML for the menu item to the output string.

If the menu item is active, the function gets its children (i.e., menu items that have this item as their parent) and recursively calls itself to generate their HTML.

Finally, the function returns the HTML output string as a safe string, marked as safe for rendering in a Django template.