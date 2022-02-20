<b>How to run the Application</b>	

- Install all the dependencies in requirment.txt file - pip install -r "requirements.txt"
- run the command "python manage.py runserver"

<b>Approach to the solution</b>
 
- Created a model Called Operation(name, formula, parameter) to save all the mathematical operations
- User can  create function by giving name and formula 
(user can either give the direct formula(ex: "a+b") or user can add python functions, for example if user want to add factorial user must add "math.factorial(n)")
- Wrote a signal to save all the parameter from the formula to parameter field
- This parameter field used for the validation by the time of execution of the function
- User can execute the mathematical operations by passing operation id and parameters as JSON object
- While executing the operation Serializer validation method will ensure whether the given parameters contains all the saved parameters and will return the result



<b>API Documentation</b>

1) Add Operation
    URL :POST /api/operations/add-operation/

    payload :  {"name":"addition", "formula": "a+b"}

    Result : 

    Status :HTTP 201 Created

    {
        "id": 1,
        "name": "addition",
        "formula": "a+b"
    }

2) List Operations
    URL: GET /api/operations/get-all-operations/

    Result :
    Status :HTTP 200 OK
    [
    {
        "id": 1,
        "name": "addition",
        "formula": "a+b"
    }
    ]

3) Get Operation

    URL : GET /api/operations/{operation_id}/retrieve-update-delete/
    Result:
    Status :HTTP 200 OK
    {
        "id": 1,
        "name": "addition",
        "formula": "a+b"
    }

4) Edit Operation
    URL : PUT /api/operations/{operation_id}/retrieve-update-delete/

    payload :  {"name":"addition", "formula": "x+y"}
    Result:
    Status :HTTP 200 OK
    {
        "id": 1,
        "name": "addition",
        "fórmula": "x+y"
    }

5) Delete Operation

    URL : DELETE /api/operations/{operation_id}/retrieve-update-delete/

    Result :
    Status : 204 No Content
6) Execute Operation
    URL : PUT /api/operations/perform-operations/
    payload : {"operation_id": 1, "parameters": {"x":5, "y":4}}

    Result: 
    Status :HTTP 200 OK
    {"result": 9}

