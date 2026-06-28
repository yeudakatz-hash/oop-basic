class DictUtils:
    @staticmethod
    def from_lists(keys, values):
        return dict(zip(keys, values))

    @staticmethod
    def from_tuples(tuples_list):
        return dict(tuples_list)

    @staticmethod
    def count_dict(items):
        counter = {}
        for item in items:
            if item in counter:
                counter[item] += 1
            else:
                counter[item] = 1
        return counter

    @staticmethod
    def nested_dict(keys, default_value = None):
        if default_value is None:
            default_value = {}

        result = {}
        for key in keys:
            if isinstance(default_value, dict):
                result[key] = default_value.copy()
            else:
                result[key] = default_value

        return result

    @staticmethod
    def count_info(dictionary):
        num_unique_values = len(set(dictionary.values()))
        return {"keys": len(dictionary) , "unique values" : num_unique_values}

    @staticmethod
    def find_key_by_values(dictionary, value):
        for item in dictionary:
            if item == value:
                return dictionary[item]
        return None

    @staticmethod
    def numeric_stats(dictionary):
        minimum = dictionary[0]
        maximum = dictionary[0]
        total = 0
        counter = 0
        for item in dictionary:
            if isinstance:
                minimum =min(minimum , dictionary[item])
                maximum = max(maximum , dictionary[item])
                total += dictionary[item]
                counter += 1
        return {"המספר המינימלי הוא" : minimum , "המספר המקסימלי הוא" : maximum , "סכום הספרות הוא" : total , "הממוצע הוא" : total / counter}

    @staticmethod
    def common_keys(dict1 , dict2):
        return list(set(dict1.keys()) & set(dict2.keys()))

    @staticmethod
    def print_dict(dictionary , title = "Dictionary"):
        print(f"==={title}===")
        for key, value in dictionary.items():
            print(f"{key} : {value}")
        print("==========")

    @staticmethod
    def safe_update(dictionary , key , value):
        if key in dictionary:
            return dictionary[key] == value
        return "error"






