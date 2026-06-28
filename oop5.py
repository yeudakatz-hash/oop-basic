# class DictUtils:
#     @staticmethod
#     def from_lists(keys, values):
#         return dict(zip(keys, values))
#
#     @staticmethod
#     def from_tuples(tuples_list):
#         return dict(tuples_list)
#
#     @staticmethod
#     def count_dict(items):
#         counter = {}
#         for item in items:
#             if item in counter:
#                 counter[item] += 1
#             else:
#                 counter[item] = 1
#         return counter
#
#     @staticmethod
#     def nested_dict(keys, default_value = None):
#         if default_value is None:
#             default_value = {}
#
#         result = {}
#         for key in keys:
#             if isinstance(default_value, dict):
#                 result[key] = default_value.copy()
#             else:
#                 result[key] = default_value
#
#         return result
#
#     @staticmethod
#     def count_info(dictionary):
#         num_unique_values = len(set(dictionary.values()))
#         return {"keys": len(dictionary) , "unique values" : num_unique_values}
#
#     @staticmethod
#     def find_key_by_values(dictionary, value):
#         for item in dictionary:
#             if item == value:
#                 return dictionary[item]
#         return None
#
#     @staticmethod
#     def numeric_stats(dictionary):
#         minimum = dictionary[0]
#         maximum = dictionary[0]
#         total = 0
#         counter = 0
#         for item in dictionary:
#             if isinstance:
#                 minimum =min(minimum , dictionary[item])
#                 maximum = max(maximum , dictionary[item])
#                 total += dictionary[item]
#                 counter += 1
#         return {"המספר המינימלי הוא" : minimum , "המספר המקסימלי הוא" : maximum , "סכום הספרות הוא" : total , "הממוצע הוא" : total / counter}
#
#     @staticmethod
#     def common_keys(dict1 , dict2):
#         return list(set(dict1.keys()) & set(dict2.keys()))
#
#     @staticmethod
#     def print_dict(dictionary , title = "Dictionary"):
#         print(f"==={title}===")
#         for key, value in dictionary.items():
#             print(f"{key} : {value}")
#         print("==========")
#
#     @staticmethod
#     def safe_update(dictionary , key , value):
#         if key in dictionary:
#             return dictionary[key] == value
#         return "error"
#
#     @staticmethod
#     def merge_dicts(dict1, dict2, conflict_strategy="keep_first"):
#         result = dict1.copy()
#
#         for key, value in dict2.items():
#             if key in result:
#                 if conflict_strategy == "keep_first":
#                     pass
#                 elif conflict_strategy == "keep_second":
#                     result[key] = value
#                 elif conflict_strategy == "sum_values":
#                     result[key] += value
#             else:
#                 result[key] = value
#         return result
#
#     @staticmethod
#     def filter_dict(dictionary, filter_func):
#         result = {}
#         for key, value in dictionary.items():
#             if filter_func(key, value):
#                 result[key] = value
#         return result
#
#     @staticmethod
#     def invert_dict(dictionary):
#         all_values = list(dictionary.values())
#         unique_values = set(all_values)
#
#         if len(all_values) != len(unique_values):
#             print("Error: Cannot invert dictionary, values are not unique!")
#             return None
#
#         result = {}
#         for key, value in dictionary.items():
#             result[value] = key
#
#         return result
#
#
# # יצירת מילונים
# dict1 = DictUtils.from_lists(['a', 'b', 'c'], [1, 2, 3])
# dict2 = DictUtils.count_dict(['x', 'y', 'x', 'z', 'x'])
#
# # מידע על מילונים
# print(DictUtils.count_info(dict1))
# print(DictUtils.find_key_by_value(dict1, 2))
# print(DictUtils.dict_status(dict2))
#
# # שינויים והדפסה
# DictUtils.print_dict(dict1, "My Dictionary")
# merged = DictUtils.merge_dicts(dict1, dict2, "keep_first")
# DictUtils.print_dict(merged, "Merged Dictionary")
#
# # סינון מתקדם
# def is_big_value(key, value):
#     return value > 1
#
# filtered = DictUtils.filter_dict(dict2, is_big_value)
# DictUtils.print_dict(filtered, "Filtered Dictionary")


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
    def nested_dict(keys, default_value=None):
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
        return {"keys": len(dictionary), "unique_values": num_unique_values}

    @staticmethod
    def find_key_by_value(dictionary, value):
        for k, v in dictionary.items():
            if v == value:
                return k
        return None

    @staticmethod
    def dict_status(dictionary):
        numeric_values = [v for v in dictionary.values() if isinstance(v, (int, float))]
        if not numeric_values:
            return {"min_value": None, "max_value": None, "sum_values": 0, "avg_values": 0}

        minimum = min(numeric_values)
        maximum = max(numeric_values)
        total = sum(numeric_values)
        average = total / len(numeric_values)

        return {
            "min_value": minimum,
            "max_value": maximum,
            "sum_values": total,
            "avg_values": average
        }

    @staticmethod
    def common_keys(dict1, dict2):
        return list(set(dict1.keys()) & set(dict2.keys()))

    @staticmethod
    def print_dict(dictionary, title="Dictionary"):
        print(f"==={title}===")
        for key, value in dictionary.items():
            print(f"{key} : {value}")
        print("==========")

    @staticmethod
    def safe_update(dictionary, key, value):
        if key in dictionary:
            dictionary[key] = value
            return True
        return "error"

    @staticmethod
    def merge_dicts(dict1, dict2, conflict_strategy="keep_first"):
        result = dict1.copy()
        for key, value in dict2.items():
            if key in result:
                if conflict_strategy == "keep_first":
                    pass
                elif conflict_strategy == "keep_second":
                    result[key] = value
                elif conflict_strategy == "sum_values":
                    result[key] += value
            else:
                result[key] = value
        return result

    @staticmethod
    def filter_dict(dictionary, filter_func):
        result = {}
        for key, value in dictionary.items():
            if filter_func(key, value):
                result[key] = value
        return result

    @staticmethod
    def invert_dict(dictionary):
        all_values = list(dictionary.values())
        unique_values = set(all_values)
        if len(all_values) != len(unique_values):
            print("Error: Cannot invert dictionary, values are not unique!")
            return None
        result = {}
        for key, value in dictionary.items():
            result[value] = key
        return result


dict1 = DictUtils.from_lists(['a', 'b', 'c'], [1, 2, 3])
dict2 = DictUtils.count_dict(['x', 'y', 'x', 'z', 'x'])

print(DictUtils.count_info(dict1))
print(DictUtils.find_key_by_value(dict1, 2))
print(DictUtils.dict_status(dict2))

DictUtils.print_dict(dict1, "My Dictionary")
merged = DictUtils.merge_dicts(dict1, dict2, "keep_first")
DictUtils.print_dict(merged, "Merged Dictionary")


def is_big_value(key, value):
    return value > 1


filtered = DictUtils.filter_dict(dict2, is_big_value)
DictUtils.print_dict(filtered, "Filtered Dictionary")

