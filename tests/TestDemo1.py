import requests 
import json
import utils.Baseclass as base
import pytest



class postOp():
    def __init__(self) :
        pass

postCall=postOp()
className=postCall.__class__
payload=base.getTestData(className.__name__)

# jsRes=res.json();
# print(jsRes["data"][0]["email"])
@pytest.mark.smoke
def test_postop():
    res=requests.post("https://reqres.in/api/users",payload) 
    rCode=res.status_code
    print(rCode)
    assert rCode==201 ,"response code error";
    response=res.json();
    print(response)
    print(response["id"])

@pytest.mark.smoke  #marker
def test_getOp():
    res=requests.get("https://reqres.in/api/users?page=2")
    rCode=res.status_code
    print(rCode)
    assert rCode==200 ,"response code error"
    response=json.loads(res.text)
    for k,v in response.items():
       if(k=='data'):
           dataToAssert=json.dumps(v)
           jsonstr=json.loads(dataToAssert)
           for d in jsonstr:
               if(d['email']=='tobias.funke@reqres.in'):
                        print(d['id'])
                        assert d['id']==9 ,"id value mismatch"
                   


   
