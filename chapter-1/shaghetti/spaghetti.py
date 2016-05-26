# spaghetti.py -- an example of bad coding.

import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config['config']

def get_data_from_user():
    config = load_config()
    data = []
    for n in range(config.getint('num_data_points')):
        value = input("Data point {}: ".format(n+1))
        data.append(value)
    return data

def print_results(results):
    for value,num_times in results:
        print("{} = {}".format(value, num_times))

def analyze_data():
    data = get_data_from_user()
    results = {}
    for value in data:
        try:
            results[value] = results[value] + 1
        except KeyError:
            results[value] = 1
    return results

def sort_results(results):
    sorted_results = []
    for value in results.keys():
        sorted_results.append((value, results[value]))
    sorted_results.sort()
    return sorted_results

if __name__ == "__main__":
    results = analyze_data()
    sorted_results = sort_results(results)
    print_results(sorted_results)

