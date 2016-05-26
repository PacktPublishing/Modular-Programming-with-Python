# This module defines the public interface for our "configpackage" package.

def init(config):
    global settings

    settings = {}
    settings['log_errors'] = config.get("log_errors", False)
    settings['db_password'] = config.get("db_password", "")


def test():
    global settings

    if settings['log_errors']:
        print("Error logging enabled")
    else:
        print("Error logging disabled")

