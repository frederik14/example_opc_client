from opcua import Client, ua

# json_data = request.stream.read()
# data = json.loads(json_data)
client = Client("opc.tcp://10.10.121.64:50000/") # Change IP adress!
# client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
try:
    client.connect()

    # get a specific node knowing its node id
    #var = client.get_node(ua.NodeId(1002, 2))
    var = client.get_node("ns=2;s=MCP.Services.Supervisor Service.Status") # Path defined by folder sturture in OPC-toolbox.
    print(var)
    var.get_data_value() # get value of node as a DataValue object
    print(var.get_value()) # get value of node as a python builtin
    #var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
    #var.set_value(3.9) # set node value using implicit data type

finally:
    client.disconnect()