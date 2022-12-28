import requests 
import Baseclass


class postOp():
    def __init__(self) :
        pass

postCall=postOp()
className=postCall.__class__
payload=Baseclass.getTestData(className.__name__)

# jsRes=res.json();
# print(jsRes["data"][0]["email"])

def test_postop():
    res=requests.post("https://reqres.in/api/users",payload) 
    rCode=res.status_code
    print(rCode)
    assert rCode==201 ,"response code error";

def test_getOp():
    res=requests.get("https://reqres.in/api/users?page=2")
    rCode=res.status_code
    print(rCode)
    assert rCode==200 ,"response code error"