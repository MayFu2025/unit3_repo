def mystery(list1:list, list2:list) -> list:
    output = []
    for it in list1:
        for el in list2:
            if it == el:
                output.append(it)
    return output

