# datastorage.py
#
# We store our data in three private globals:
#
#    'items'
#
#        The list of current inventory items.  Each item in this list is a
#        (product_code, location_code) tuple.
#
#    'products'
#
#       The list of products we can hold inventory for.  Each item in this list
#       is a (code, description, desired_number) tuple, where 'code is a code
#       identifying the product, 'description' is a string describing that
#       product so the user can identify it, and 'desired_number' is the
#       desired number of items that the user wants to keep in the inventory.
#
#    'locations'
#
#       The list of locations where inventory can be stored.  Each item in this
#       list is a (code, description) tuple, where 'code is the code for an
#       inventory location, and 'description' is a string describing that
#       location so that the user knows where it is.

import json
import os.path

#############################################################################

def init():
    """ Initialize the datastorage module.
    """
    _load_items()

#############################################################################

def items():
    """ Return a list of inventory items.

        We return a list of inventory items.  Each item in the returned list
        will be a (product_code, location_code) tuple.

        Note that the returned list of items are not sorted in any way.
    """
    global _items
    return _items

#############################################################################

def products():
    """ Return a list of the known products.

        We return a list of (code, description, desired_number) tuples
        containing all the known inventory products.
    """
    global _products
    return _products

#############################################################################

def locations():
    """ Return a list of the known locations where inventory can be stored.

        We return a list of (code, description) tuples containing all the known
        inventory locations.
    """
    global _locations
    return _locations

#############################################################################

def add_item(product_code, location_code):
    """ Add an item to the inventory with the given product code and location.
    """
    global _items
    _items.append((product_code, location_code))
    _save_items()

#############################################################################

def remove_item(product_code, location_code):
    """ Remove an inventory item with the given product code from the given location.

        Returns True if and only if the item was successfully removed.
    """
    global _items
    for i in range(len(_items)):
        prod_code,loc_code = _items[i]
        if prod_code == product_code and loc_code == location_code:
            del _items[i]
            _save_items()
            return True
    return False

#############################################################################

def set_products(products):
    """ Set the (currently hardwired) list of inventory products.

        Each item in the 'products' list should be a (code, description,
        desired_number) tuple, where 'code is a code identifying the product,
        'description' is a string describing that product so the user can
        identify it, and 'desired_number' is the desired number of items that
        you want to keep in the inventory.
    """
    global _products
    _products = products

#############################################################################

def set_locations(locations):
    """ Set the (currently hardwired) list of inventory locations.

        Each item in the 'locations' list should be a (code, description)
        tuple, where 'code is the code for an inventory location, and
        'description' is a string describing that location so that the user
        knows where it is.
    """
    global _locations
    _locations = locations

#############################################################################
#
# Private definitions:

def _load_items():
    """ Load the list of inventory items from disk.
    """
    global _items

    if os.path.exists("items.json"):
        f = open("items.json", "r")
        _items = json.loads(f.read())
        f.close()
    else:
        _items = []

#############################################################################

def _save_items():
    """ Save the list of inventory items to disk.
    """
    global _items

    f = open("items.json", "w")
    f.write(json.dumps(_items))
    f.close()

