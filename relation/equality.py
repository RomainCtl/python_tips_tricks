def t_equals(tab1, tab2):
    """
    t_equals function.

    Equality of scalar tables.

    :param tab1 : first list
    :param tab2 : second list

    :return tab1 == tab2
    :rtype: boolean

    Example::
        t_equals([0,1,2,3], [3,2,1,0]) -> False
        t_equals([0,1,2,3], [0,1,2,3]) -> True
        t_equals([1,2,3], [0,1,2,3]) -> False
    """
    if not (type(tab1) is list and type(tab2) is list): raise TypeError('tab1 and tab2 must be list')
    return tab1 == tab2

def e_equals(tab1, tab2):
    """
    e_equals function.

    Set equality.

    :param tab1 : first list
    :param tab2 : second list

    :return tab1 == tab2
    :rtype: boolean

    Example::
        e_equals([0,1,2,2,2,2,2,2,3], [3,2,1,0]) -> True
        e_equals([0,1,2,3,3,2,3], [0,1,2,3]) -> True
        e_equals([1,2,2,2,2,2,3], [0,1,2,3]) -> False
    """
    if not (type(tab1) is list and type(tab2) is list): raise TypeError('tab1 and tab2 must be list')
    return set(tab1) == set(tab2)

def o_equals(obj1, obj2):
    """
    o_equals function.

    Equality of objects.

    :param obj1 : first dict
    :param obj2 : second dict

    :return obj1 == obj2
    :rtype: boolean

    Example::
        o_equals({"nom":"Dupond","prenom":"jean","age":25}, {"age":25,"nom":"Dupond","prenom":"jean"}) -> True
        o_equals({"nom":"Dupond","prenom":"jean","age":25}, {"nom":"Dupond","prenom":"jean"}) -> False
        o_equals({"nom":"Dupond","prenom":"jean","age":25}, {"age":24,"nom":"Dupond","prenom":"jean"}) -> False
    """
    if not (type(obj1) is dict and type(obj2) is dict): raise TypeError('obj1 and obj2 must be dict')
    return e_equals(list(obj1.keys()), list(obj2.keys())) and all(obj1[k] == obj2[k] for k in obj1.keys())

def equals(obj1, obj2):
    """
    equals function.

    Equality of anything.

    :param obj1 :
    :param obj2 :

    :return obj1 is equals to obj2
    :rtype: boolean

    Example::
        equals(1, 1) -> True
        equals("aa", "aa") -> True
        equals([0,1,2,3], [3,2,1,0]) -> False
        equals([0,1,2,2,2,2,2,2,3], [3,2,1,0]) -> False
        equals({"nom":"Dupond","prenom":"jean","age":25}, {"age":25,"nom":"Dupond","prenom":"jean"}) -> True

        to1 = [["un", {"nom" : 'trucMoche', "couleur" : ["Marron","Rouge"]}], ["une","chat"], ["un","chienne"], ["une","chienne"]]
        to2 = [["un", {"couleur" : ["Marron","Rouge"], "nom" : 'trucMoche'}], ["une","chat"], ["un","chienne"], ["une","chienne"]]
        to3 = [["un", {"couleur" : ["Rouge","Marron"], "nom" : 'trucMoche'}], ["une","chat"], ["un","chienne"], ["une","chienne"]]

        equals(to1, to2) -> True
        equals(to2, to3) -> False
    """
    def keys(obj):
        if type(obj) is list: return range(len(obj))
        elif type(obj) is dict: return obj.keys()
        else: raise TypeError("obj must be list or dict")
    if ((type(obj1) is not list and type(obj1) is not dict) or (type(obj2) is not list and type(obj2) is not dict)): return obj1 == obj2
    return e_equals(list(keys(obj1)), list(keys(obj2))) and all(equals(obj1[k], obj2[k]) for k in keys(obj1))
