import json
import requests

def load_filenames():
    r = requests.get('https://raw.githubusercontent.com/outbreak-info/covid19_LST_report_data/main/reportlist.txt')
    reportlist=r.text.split('\n')
    formattedlist = [x.replace(" ","%20") for x in reportlist]
    return(formattedlist)

def load_annotations():
    basejsonurl = 'https://raw.githubusercontent.com/outbreak-info/covid19_LST_report_data/main/json/'
    formattedlist = load_filenames()
    for eachjson in formattedlist:
        fileurl = basejsonurl+eachjson
        rawdoc = requests.get(fileurl)
        if rawdoc.status_code == 200:
            doc = json.loads(rawdoc.text)
        else:
            continue
        yield doc

if __name__ == '__main__':
    with open('output.json', 'w') as output:
        json.dump([i for i in load_annotations()], output)
