from enum import Enum
from typing import List

from fastapi import FastAPI, HTTPException

app = FastAPI()

class OperationName(str, Enum):
    add = "add"
    sub = "sub"
    mul = "mul"
    div = "div"

#Convert list of numbers to list of strings to concatenate the operator and then perform eval to calculate the result
def operate_list(numbers, operator):
    str_numbers = [str(i) for i in numbers]
    result = str_numbers[0]
    for i in range(1, len(numbers)):
        if str_numbers[i] == "0" and operator == "/":
            #if the dividend is 0 an exception is rised
            raise HTTPException(status_code=400, detail="Division by zero not allowed")
        result = result + operator + str_numbers[i]
    return eval(result)

@app.post("/add")
def operate_add(numbers: List[int]):
    if len(numbers) > 0:
        return {"result": operate_list(numbers, "+")}
    else:
        raise HTTPException(status_code=400, detail="The list of numbers can't be empty")

@app.post("/sub")
def operate_sub(numbers: List[int]):
    if len(numbers) > 0:
        return {"result": operate_list(numbers, "-")}
    else:
        raise HTTPException(status_code=400, detail="The list of numbers can't be empty")

@app.post("/mul")
def operate_mul(numbers: List[int]):
    if len(numbers) > 0:
        return {"result": operate_list(numbers, "*")}
    else:
        raise HTTPException(status_code=400, detail="The list of numbers can't be empty")

@app.post("/div")
def operate_div(numbers: List[int]):
    if len(numbers) > 0:
        return {"result": operate_list(numbers, "/")}
    else:
        raise HTTPException(status_code=400, detail="The list of numbers can't be empty")

@app.post("/arithmetic_operations/{operation}")
def operate(operation: OperationName, numbers: List[int]):
    if len(numbers) > 0:
        operator = None
        if operation == "add":
            operator = "+"
        if operation == "sub":
            operator = "-"
        if operation == "mul":
            operator = "*"
        if operation == "div":
            operator = "/"

        return {"result": operate_list(numbers, operator)}
    else:
        raise HTTPException(status_code=400, detail="The list of numbers can't be empty")