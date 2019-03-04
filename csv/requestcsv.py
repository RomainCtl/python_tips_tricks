from requests import RequestException
from requests_ntlm import HttpNtlmAuth
import requests, csv

class RequestCSV:
    def __init__(self, url, encode="utf-8", delimiter=",", lineterminator="\r\n"):
        self.url=url
        self.encode=encode
        self.delimiter=delimiter
        self.lineterminator=lineterminator

    def get(self, login, password):
        try:
            r = requests.Session()
            r.auth = HttpNtlmAuth('AD\\' + login, password, r)

            file = r.get(self.url)

            if file.status_code == requests.codes.ok:
                content = file.content.decode(self.encode).splitlines()
                return list(csv.reader(content, delimiter=self.delimiter, lineterminator=self.lineterminator))
            else:
                file.raise_for_status() # Do an exception
        except RequestException as e:
            print("An Error occured with the request !", str(e))
            return None
        except csv.Error as e:
            print("An error occured while reading csv file !", str(e))
            return None

if __name__ == "__main__":
    r = RequestCSV(url="http://example.com/path/to/file.CSV")
    data = r.get(login="Mylogin", password="Mypassword")
