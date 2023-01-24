


def left_join(map1, map2):
    result = []
    for key in map1.keys():
        map1_value = map1[key]
        map2_value = map2.get(key, None)
        result.append([key, map1_value, map2_value])
    return result


