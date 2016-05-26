import importlib

module_name = input("Load module: ")
if module_name != "":
    module = importlib.import_module(module_name)
    module.say_hello()

