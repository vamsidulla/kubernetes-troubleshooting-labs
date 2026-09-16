# Coverage matrix

| Level | ID | Runbook | Primary domain |
|---|---|---|---|
| Beginner | B01 | [kubectl cannot connect to the cluster](beginner/b01-cluster-access.md) | Access/control plane |
| Beginner | B02 | [kubectl returns Forbidden](beginner/b02-forbidden-rbac.md) | Identity/RBAC |
| Beginner | B03 | [ImagePullBackOff or ErrImagePull](beginner/b03-image-pull.md) | Images |
| Beginner | B04 | [CrashLoopBackOff](beginner/b04-crash-loop.md) | Application |
| Beginner | B05 | [Readiness, liveness, or startup probe failures](beginner/b05-probe-failures.md) | Health probes |
| Beginner | B06 | [Pod remains Pending](beginner/b06-pod-pending.md) | Scheduling |
| Beginner | B07 | [Service has no endpoints or reaches the wrong port](beginner/b07-service-endpoints.md) | Services |
| Beginner | B08 | [Pod cannot resolve a service or external name](beginner/b08-dns-resolution.md) | DNS |
| Beginner | B09 | [PVC Pending or pod stuck ContainerCreating](beginner/b09-pvc-pending.md) | Storage |
| Beginner | B10 | [Logs or exec target the wrong container](beginner/b10-logs-exec.md) | Debugging |
| Intermediate | I01 | [AKS cannot pull from ACR although the image exists](intermediate/i01-acr-auth-network.md) | ACR |
| Intermediate | I02 | [LoadBalancer external IP remains Pending](intermediate/i02-loadbalancer-pending.md) | Load balancer |
| Intermediate | I03 | [Ingress returns 404, 502, timeout, or TLS errors](intermediate/i03-ingress-routing-tls.md) | Ingress/TLS |
| Intermediate | I04 | [Traffic fails after NetworkPolicy or NSG changes](intermediate/i04-networkpolicy-nsg.md) | Network policy/NSG |
| Intermediate | I05 | [Pods or nodes cannot reach external endpoints](intermediate/i05-outbound-egress.md) | Egress |
| Intermediate | I06 | [Scale or upgrade fails because the subnet is full](intermediate/i06-subnet-ip-exhaustion.md) | IP capacity |
| Intermediate | I07 | [Node becomes NotReady or reports pressure](intermediate/i07-node-notready-pressure.md) | Nodes |
| Intermediate | I08 | [OOMKilled, CPU throttling, or eviction](intermediate/i08-resource-saturation.md) | Resources |
| Intermediate | I09 | [Cluster autoscaler does not add or remove nodes](intermediate/i09-autoscaler.md) | Autoscaling |
| Intermediate | I10 | [AKS upgrade is blocked by drain or PDB](intermediate/i10-upgrade-pdb.md) | Upgrades/PDB |
| Advanced | A01 | [Intermittent outbound failures from SNAT exhaustion](advanced/a01-snat-exhaustion.md) | SNAT |
| Advanced | A02 | [Intermittent timeouts with healthy pods](advanced/a02-intermittent-timeouts.md) | Intermittent network |
| Advanced | A03 | [Private AKS API is unreachable](advanced/a03-private-api.md) | Private API |
| Advanced | A04 | [Logs, exec, or metrics fail because API-to-node tunnel is broken](advanced/a04-api-kubelet-tunnel.md) | API-node tunnel |
| Advanced | A05 | [Azure Disk attach or mount fails across zones or nodes](advanced/a05-azure-disk-topology.md) | Azure Disk |
| Advanced | A06 | [Azure Files mount fails or is slow](advanced/a06-azure-files.md) | Azure Files |
| Advanced | A07 | [AKS operation fails with LinkedAuthorizationFailed](advanced/a07-identity-authorization.md) | Azure identity |
| Advanced | A08 | [Create, scale, or upgrade fails from quota, capacity, or throttling](advanced/a08-quota-capacity-throttling.md) | Quota/capacity |
| Advanced | A09 | [Large cluster API server or etcd becomes slow](advanced/a09-large-cluster-control-plane.md) | Control plane scale |
| Advanced | A10 | [AKS managed Istio ingress fails during routing or revision changes](advanced/a10-istio-ingress.md) | Istio |

The matrix is a discovery index, not a completeness claim. Add a new runbook when evidence shows a distinct root-cause family; link an existing runbook when a report is another symptom of the same family.
