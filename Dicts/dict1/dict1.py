def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    return dict(zip(keys,values))
    pass  # implement me


def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    d1.update(d2)
    return d1

def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    # output_dict = {}
    # for item in lst:
    #     output_dict[item] = d1
    # return output_dict
    output_dict = {item: d1 for item in lst}
    return output_dict


def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    #
    output_dict = {key: datadict[key] for key in keylist}
    return output_dict


def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    for key in keylist:
        datadict.pop(key)
    return datadict


def check_dict_for_key(datadict, key): #thought this was asking for the presence of a key, instead of a value.
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    return key in datadict.values()


def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """
    return min(ddd, key=ddd.get)  #find way to do this w/ lambdas... still need the practice with those.


def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    return (max(ddd, key=ddd.get))