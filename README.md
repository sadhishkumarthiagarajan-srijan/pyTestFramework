# pyTestFramework


command to run test scripts with report generation pytest filename.py --html=testoutput/report.html

command to run specific test method inside .py file pytest filename.py::test_method --html=testoutput/report.html



@pytest.mark.get 
with the above annotation we can restrict a test run to only run tests marked with get:
command to run with marker is 
pytest  GetAndPost.py -m get. "get is the marker name"
