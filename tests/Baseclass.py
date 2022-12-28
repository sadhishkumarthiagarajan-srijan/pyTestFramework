
import json


def getTestData(par):
    print(par)
    with open("/Users/sadhishkumar.thiagarajan/pyLearning/ApiTesting/testData/data.json",'r') as string:
        my_dict=json.load(string)
        string.close()

        for k,v in my_dict.items():
            if(k==par):
                val=json.dumps(v)
                return val


