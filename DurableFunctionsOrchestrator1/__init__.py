# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    logging.info(f"Payload from HTTP Trigger: " + context.get_input() )    
    result1 = yield context.call_activity('GenerateID', "Step 0: Genrate Order ID")
    data = {}
    data['orderid'] = result1
    data['activity'] = "Step 1: Placed order for all the items in your cart"
    data['order'] = context.get_input()
    json_data = json.dumps(data)
    result2 = yield context.call_activity('PlaceOrder', str(json_data))
    data = {}
    data['orderid'] = result1
    data['activity'] = "Step 2: Check if inventory is available"
    data['order'] = context.get_input()
    json_data = json.dumps(data)
    result3 = yield context.call_activity('CheckInventory', str(json_data))
    data = {}
    data['orderid'] = result1
    data['activity'] = "Step 3: Payment Process"
    data['order'] = context.get_input()
    json_data = json.dumps(data)
    result3 = yield context.call_activity('PaymentProcess', str(json_data))
    data = {}
    data['orderid'] = result1
    data['activity'] = "Step 4: Initiate Order fulfillment"
    data['order'] = context.get_input()
    json_data = json.dumps(data)
    result4 = yield context.call_activity('OrderFulfillment', str(json_data))

    return [result1,result2,result3,result4]

main = df.Orchestrator.create(orchestrator_function)