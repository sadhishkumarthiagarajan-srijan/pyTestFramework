import requests 
import json
import utils.Baseclass as base
import pytest

class testDemo2():
    def __init__(self) :
        pass

clsName=testDemo2()
className=clsName.__class__



                        
@pytest.mark.smoke
def test_getCall():
    res=requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities") 
    rCode=res.status_code
    print(rCode)
    dataJson=res.json()
    for d in dataJson:
        if(d['id']==30):
            assert d['title']=="Activity 30"
            print(d['title'])

@pytest.mark.smoke
def test_PostCall():
    payload=base.getTestData("test_PostCall")
    res=requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",json.loads(payload))
    rCode=res.status_code
    print(rCode)
    print(res.text)
    
    