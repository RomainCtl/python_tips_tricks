from relation.equality import o_equals
from functools import cmp_to_key

class ArrayManipulator:
    @staticmethod
    def unique(tab):
        arr = []
        for i in range(len(tab)):
            if len(list(filter(lambda item: o_equals(item, tab[i]), arr))) == 0:
                arr.append(tab[i])
        return arr

    @staticmethod
    def union(E, F):
        return ArrayManipulator.unique([*E, *F])

    @staticmethod
    def intersect(E, F):
        arr = []
        for i in range(len(E)):
            if len(list(filter(lambda itemF: o_equals(itemF, E[i]), F))) > 0:
                arr.append(E[i])
        return ArrayManipulator.unique(arr)

    @staticmethod
    def minus(E, F):
        arr = []
        for i in range(len(E)):
            if len(list(filter(lambda itemF: o_equals(itemF, E[i]), F))) == 0:
                arr.append(E[i])
        return ArrayManipulator.unique(arr)

    @staticmethod
    def project(tab, listattr):
        return list(map(lambda item: {attr: item[attr] for attr in listattr}, tab))

    @staticmethod
    def where(tab, cond):
        return list(filter(cond, tab))

    @staticmethod
    def orderby(tab, keys):
        def order(a, b, index=0):
            if index == len(keys): return 0
            elif a[keys[index]] < b[keys[index]]: return -1
            elif a[keys[index]] > b[keys[index]]: return 1
            else: return order(a, b, index+1)

        return sorted(tab, key=cmp_to_key(order))

    @staticmethod
    def groupby(tab, keys, obj):
        res=[]
        for i in range(len(tab)):
            tmp = ArrayManipulator.where(tab, lambda t: all(t[keys[j]] == tab[i][keys[j]] for j in range(len(keys))))

            res.append({
                **{keys[ke]: tab[i][keys[ke]] for ke in range(len(keys))},
                **{ob: obj[ob](tmp) for ob in obj}
            })
        return ArrayManipulator.unique(res)

    @staticmethod
    def sum(tab, key):
        return sum(list(map(lambda a: a[key], ArrayManipulator.project(tab, [key]))))

    @staticmethod
    def count(tab):
        return len(tab)

    @staticmethod
    def avg(tab, key):
        return ArrayManipulator.sum(tab, key) / ArrayManipulator.count(tab)

    @staticmethod
    def full_join(tab1, tab2, ck1, ck2):
        """
        SQL::
            SELECT *
            FROM tab1
            FULL JOIN tab2 ON tab1.ck1 = tab2.ck2
        """
        res = tab1[:]
        for e in tab2:
            ids = [i for i in range(len(tab1)) if tab1[i][ck1] == e[ck2]]
            if len(ids) > 0:
                for id in ids:
                    if tab1[id] in res:
                        res[res.index(tab1[id])] = {**tab1[id], **e}
                    else:
                        res.append({**tab1[id], **e})
            else:
                res.append(e)
        return res

    @staticmethod
    def left_join(tab1, tab2, ck1, ck2):
        """
        SQL::
            SELECT *
            FROM tab1
            LEFT JOIN tab2 ON tab1.ck1 = tab2.ck2
        """
        res = tab1[:]
        for e in tab2:
            ids = [i for i in range(len(tab1)) if tab1[i][ck1] == e[ck2]]
            for id in ids:
                if tab1[id] in res:
                    res[res.index(tab1[id])] = {**tab1[id], **e}
                else:
                    res.append({**tab1[id], **e})
        return res

    @staticmethod
    def right_join(tab1, tab2, ck1, ck2):
        """
        SQL::
            SELECT *
            FROM tab1
            RIGHT JOIN tab2 ON tab1.ck1 = tab2.ck2
        """
        return ArrayManipulator.left_join(tab2, tab1, ck2, ck1)

    @staticmethod
    def inner_join(tab1, tab2, ck1, ck2):
        """
        SQL::
            SELECT *
            FROM tab1
            INNER JOIN tab2 ON tab1.ck1 = tab2.ck2
        """
        res = []
        for e in tab2:
            ids = [i for i in range(len(tab1)) if tab1[i][ck1] == e[ck2]]
            for id in ids:
                res.append({**tab1[id], **e})
        return res

    @staticmethod
    def natural_join(tab1, tab2):
        """
        SQL::
            SELECT *
            FROM tab1
            NATURAL JOIN tab2
        """
        fk = list(set(tab1[0].keys()) & set(tab2[0].keys())) # intersection of the keys of the tow tabs
        if len(fk) != 1: raise Exception("Error on natural join, relation not found !")
        return ArrayManipulator.full_join(tab1, tab2, fk[0], fk[0])

