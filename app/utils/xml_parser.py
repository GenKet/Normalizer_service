import xml.etree.ElementTree as ET

def xml_to_dict(xml_str: str) -> dict:
    """
    Преобразует XML строку в словарь.
    """
    root = ET.fromstring(xml_str)
    return {root.tag: elem_to_dict(root)}

def elem_to_dict(elem):
    """
    Рекурсивное преобразование XML-элемента в словарь.
    Если элемент имеет несколько дочерних элементов с одинаковым тегом,
    они объединяются в список.
    """
    d = {}
    if list(elem):
        for child in elem:
            child_dict = elem_to_dict(child)
            tag = child.tag
            if tag in d:
                if isinstance(d[tag], list):
                    d[tag].append(child_dict)
                else:
                    d[tag] = [d[tag], child_dict]
            else:
                d[tag] = child_dict
    else:
        d = elem.text or ""
    return d
