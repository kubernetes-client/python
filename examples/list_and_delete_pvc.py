from kubernetes import client, config, watch
from datetime import datetime, timezone, timedelta
import os, subprocess

#----------------------------------------------------
now = datetime.utcnow()
only_date = now.date()
print (" ")
print ("Today's date is:", (only_date))
print (" ")
retention_days = 0
#------------------------------------------------------

ns = os.getenv("K8S_NAMESPACE")
if ns is None:
    ns = "foo" # Namespace foo is aleady existing, or enter namespace

config.load_kube_config()

v1 = client.CoreV1Api()

pvcs = v1.list_namespaced_persistent_volume_claim(namespace=ns, watch=False)
print("---- PVCs ---")
print("%-16s\t%-40s\t%-6s\t%-6s" % ("Name", "Volume", "Size", "Date_Created"))
for pvc in pvcs.items:
    print("%-16s\t%-40s\t%-6s\t%-6s" %
            (pvc.metadata.name, pvc.spec.volume_name,    
            pvc.spec.resources.requests['storage'], pvc.metadata.creation_timestamp.date()))
print("")
filtered_pvcs_date = pvc.metadata.creation_timestamp.date() 


if (only_date - filtered_pvcs_date) > timedelta(retention_days):
    print ("PVC is older than configured retention of %d days" % (retention_days))
    
    cmd = ('kubectl delete pvc' + " " + pvc.metadata.name + " " + '-n' + " " + ns)
    os.system(cmd) 
    
    
else:
    print ("PVC is younger than configured retention of %d days" % (retention_days)
