# main.py
#
# This is the main program for the InventoryControl system.

import datastorage
import userinterface
import reportgenerator

#############################################################################

def main():
    datastorage.init()

    datastorage.set_products([
        ("SKU123", "4 mm flat-head wood screw",        50),
        ("SKU145", "6 mm flat-head wood screw",        50),
        ("SKU167", "4 mm countersunk head wood screw", 10),
        ("SKU169", "6 mm countersunk head wood screw", 10),
        ("SKU172", "4 mm metal self-tapping screw",    20),
        ("SKU185", "8 mm metal self-tapping screw",    20),
    ])

    datastorage.set_locations([
        ("S1A1", "Shelf 1, Aisle 1"),
        ("S2A1", "Shelf 2, Aisle 1"),
        ("S3A1", "Shelf 3, Aisle 1"),
        ("S1A2", "Shelf 1, Aisle 2"),
        ("S2A2", "Shelf 2, Aisle 2"),
        ("S3A2", "Shelf 3, Aisle 2"),
        ("BIN1", "Storage Bin 1"),
        ("BIN2", "Storage Bin 2"),
    ])

    while True:
        action = userinterface.prompt_for_action()
        if action == "QUIT":
            break
        elif action == "ADD":
            product = userinterface.prompt_for_product()
            if product != None:
                location = userinterface.prompt_for_location()
                if location != None:
                    datastorage.add_item(product, location)
        elif action == "REMOVE":
            product = userinterface.prompt_for_product()
            if product != None:
                location = userinterface.prompt_for_location()
                if location != None:
                    if not datastorage.remove_item(product, location):
                        userinterface.show_error("There is no product with " +
                                                 "that code at that location!")
        elif action == "INVENTORY_REPORT":
            report = reportgenerator.generate_inventory_report()
            userinterface.show_report(report)
        elif action == "REORDER_REPORT":
            report = reportgenerator.generate_reorder_report()
            userinterface.show_report(report)

#############################################################################

if __name__ == "__main__":
    main()

