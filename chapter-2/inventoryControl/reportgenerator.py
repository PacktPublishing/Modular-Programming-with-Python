# reportgenerator.py
#
# This module implements the report-generation logic for the InventoryControl
# system.

import datastorage

#############################################################################

def generate_inventory_report():
    """ Generate a report of the current inventory levels.

        We return a list of strings containing the report's contents.
    """
    # Get the list of known products and locations.

    product_names = {} # Maps product code to product name.
    for product_code,name,desired_number in datastorage.products():
        product_names[product_code] = name

    location_names = {} # Maps location code to location name.
    for location_code,name in datastorage.locations():
        location_names[location_code] = name

    # Calculate the report's contents.

    grouped_items = {} # Maps product code to dictionary mapping location code
                       # to number of items with that product at that location.

    for product_code,location_code in datastorage.items():
        if product_code not in grouped_items:
            grouped_items[product_code] = {}

        if location_code not in grouped_items[product_code]:
            grouped_items[product_code][location_code] = 1
        else:
            grouped_items[product_code][location_code] += 1

    # Generate the report.

    report = []
    report.append("INVENTORY REPORT")
    report.append("")

    for product_code in sorted(grouped_items.keys()):
        product_name  = product_names[product_code]
        report.append("Inventory for product: {} - {}".format(product_code,
                                                              product_name))
        report.append("")

        for location_code in sorted(grouped_items[product_code].keys()):
            location_name = location_names[location_code]
            num_items     = grouped_items[product_code][location_code]
            report.append("  {} at {} - {}".format(num_items,
                                                   location_code,
                                                   location_name))
        report.append("")

    return report

#############################################################################

def generate_reorder_report():
    """ Generate a report of the inventory items to re-order.

        We return a list of strings containing the report's contents.
    """
    # Get the list of known products and locations.

    product_names   = {} # Maps product code to product name.
    desired_numbers = {} # maps product code to desired number of items.

    for product_code,name,desired_number in datastorage.products():
        product_names[product_code] = name
        desired_numbers[product_code] = desired_number

    # Calculate our current inventory levels.

    num_in_inventory = {} # Maps product code to number of items in inventory.

    for product_code,location_code in datastorage.items():
        if product_code in num_in_inventory:
            num_in_inventory[product_code] += 1
        else:
            num_in_inventory[product_code] = 1

    # Generate the report.

    report = []
    report.append("RE-ORDER REPORT")
    report.append("")

    for product_code in sorted(product_names.keys()):
        desired_number = desired_numbers[product_code]
        current_number = num_in_inventory.get(product_code, 0)
        if current_number < desired_number:
            product_name = product_names[product_code]
            num_to_reorder = desired_number - current_number
            report.append("  Re-order {} of {} - {}".format(num_to_reorder,
                                                            product_code,
                                                            product_name))
    report.append("")

    return report

