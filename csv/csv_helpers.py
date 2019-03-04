from csv.requestcsv import RequestCSV

class CSVHelpers:
    def __init__(self):
        self.downloaded_data = {} # To save already downloaded files

    def get_file_data(self, file):
        if file not in self.downloaded_data:
            tmp = RequestCSV(url = file)
            self.downloaded_data[file] = tmp.get()
        return self.downloaded_data[file]

    def get_data(self, infos):
        if len(infos['files']) != len(infos['expected_header']): raise IndexError("Error with numbers of expected files !")
        return {
            infos['files'][i] : self.csv_to_dict(self.get_file_data(infos['files'][i]), infos['expected_header'][i], infos['wished_headers'][i])
            for i in range(len(infos['files']))
        }

    def csv_to_dict(self, list, expected_header, wished_headers=None):
        """
        csv_to_dict function

        Transform csv to dict

        This object must contain :
        :param list : list of list
        :param wished_headers : list of wished headers

        :return list of dict
        :rtype: list

        Example::

            csv_liste = [
                ["attr1", "attr2", "attr3"],
                ["val1", "val2", "val3"],
                ["e1", "e2", "e3"]
            ]

            dico = self.csv_to_dict(csv_liste)

            wished_dico = self.csv_to_dict(csv_liste, ["attr1", "attr3"])
        """
        header = list[0]
        if header != expected_header: raise NameError("the headers provided are not those expected")
        if wished_headers is None: wished_headers=header
        if len(wished_headers) > len(header): raise IndexError("wished headers length too long !")
        res = []
        for i in range(1, len(list)):
            line = {}
            for j in range(len(list[i])):
                if header[j] in wished_headers: line[header[j]] = list[i][j]
            res.append(line)
        return res

    def change_key_of_dict(self, dico, new_keys):
        """
        change_key_of_dict function

        Change keys of dict object

        This object must contain :
        :param dico : dict
        :param new_keys : list of new keys

        :return dico with new keys
        :rtype: dict

        Example::

            dico = {"old1": "val1", "old2": "val2", "old3": "val3"}
            new_keys = {"old1": "new1", "old2": "new2", "old3": "new3"}

            new_dico = self.change_key_of_dict(dico, new_keys)
        """
        if len(new_keys) != len(dico): raise IndexError("Error with numbers of new keys !")
        res = {}
        i=0
        for k,v in dico.items():
            res[new_keys[k]] = v
            i+=1
        return res

    def values_of_dict_is_not_empty(self, dico):
        dicov = list(dico.values())
        while "" in dicov: dicov.remove("")
        return not not dicov

    def dict_to_object(self, data, Obj, header):
        return [Obj(**self.change_key_of_dict(e, header)) for e in data if self.values_of_dict_is_not_empty(e)]

    def spe_dict_to_object(self, data, Obj):
        return {k: Obj(**v) for k,v in data.items() if self.values_of_dict_is_not_empty(v)}

    def join_dict_by_dict(self, *args):
        """
        join_dict_by_dict function

        Join two dict with there keys

        This object must contain :
        :param args : *args (dicts)

        :return join of two dict
        :rtype: dict

        Example::

            dico1 = {
                "001": {"siren" : "1", "rce" : "r1"},
                "002": {"siren" : "2", "rce" : "r2"},
                "003": {"siren" : "3", "rce" : "r3"}
            }
            dico2 = {
                "001": {"ico1" : "i1"},
                "003": {"ico1" : "i3"},
                "006": {"ico1" : "i6"}
            }

            dico = self.join_dict_by_dict(dico1, dico2)
        """
        res = {}
        for e in args:
            for k,v in e.items():
                if k in res:
                    res[k] = {**res[k], **v}
                else:
                    res[k] = v
        return res
