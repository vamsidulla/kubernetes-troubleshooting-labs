# AKS Troubleshooting Atlas

This atlas groups recurring Azure Kubernetes Service incidents by **root cause**, from beginner to advanced. It is intentionally not called a list of every AKS incident ever reported: no finite repository can prove worldwide completeness, and the platform changes continuously. Instead, these 30 runbooks cover the most reusable failure families found in current Microsoft AKS guidance, Kubernetes documentation, and operational reports.

Use the existing `labs/` directory for locally reproducible Kubernetes exercises. Use this atlas for AKS-specific diagnosis that requires Azure context.

## Start here: six questions

1. What is the exact symptom and first failing timestamp in UTC?
2. Is the failure in the application, Kubernetes object, node, AKS control plane, or Azure dependency?
3. What is the source, destination, port/protocol, and hop-by-hop path?
4. Is every workload affected or only one namespace, node pool, zone, node, or identity?
5. What changed immediately before the failure?
6. What evidence would disprove the current hypothesis?

## Universal evidence pack

```bash
kubectl cluster-info
kubectl get nodes -o wide
kubectl get pods -A -o wide
kubectl get events -A --sort-by=.metadata.creationTimestamp
kubectl get svc,endpointslice,ingress -A
az aks show -g <resource-group> -n <cluster> -o json
az monitor activity-log list --resource-group <resource-group> --offset 2h
```

Collect only what your role permits. Do not commit command output because it may contain internal IPs, identities, registry names, or other environment details. Never collect Secret values or kubeconfig credentials for a troubleshooting report.

## Beginner
- [B01: kubectl cannot connect to the cluster](beginner/b01-cluster-access.md)
- [B02: kubectl returns Forbidden](beginner/b02-forbidden-rbac.md)
- [B03: ImagePullBackOff or ErrImagePull](beginner/b03-image-pull.md)
- [B04: CrashLoopBackOff](beginner/b04-crash-loop.md)
- [B05: Readiness, liveness, or startup probe failures](beginner/b05-probe-failures.md)
- [B06: Pod remains Pending](beginner/b06-pod-pending.md)
- [B07: Service has no endpoints or reaches the wrong port](beginner/b07-service-endpoints.md)
- [B08: Pod cannot resolve a service or external name](beginner/b08-dns-resolution.md)
- [B09: PVC Pending or pod stuck ContainerCreating](beginner/b09-pvc-pending.md)
- [B10: Logs or exec target the wrong container](beginner/b10-logs-exec.md)

## Intermediate
- [I01: AKS cannot pull from ACR although the image exists](intermediate/i01-acr-auth-network.md)
- [I02: LoadBalancer external IP remains Pending](intermediate/i02-loadbalancer-pending.md)
- [I03: Ingress returns 404, 502, timeout, or TLS errors](intermediate/i03-ingress-routing-tls.md)
- [I04: Traffic fails after NetworkPolicy or NSG changes](intermediate/i04-networkpolicy-nsg.md)
- [I05: Pods or nodes cannot reach external endpoints](intermediate/i05-outbound-egress.md)
- [I06: Scale or upgrade fails because the subnet is full](intermediate/i06-subnet-ip-exhaustion.md)
- [I07: Node becomes NotReady or reports pressure](intermediate/i07-node-notready-pressure.md)
- [I08: OOMKilled, CPU throttling, or eviction](intermediate/i08-resource-saturation.md)
- [I09: Cluster autoscaler does not add or remove nodes](intermediate/i09-autoscaler.md)
- [I10: AKS upgrade is blocked by drain or PDB](intermediate/i10-upgrade-pdb.md)

## Advanced
- [A01: Intermittent outbound failures from SNAT exhaustion](advanced/a01-snat-exhaustion.md)
- [A02: Intermittent timeouts with healthy pods](advanced/a02-intermittent-timeouts.md)
- [A03: Private AKS API is unreachable](advanced/a03-private-api.md)
- [A04: Logs, exec, or metrics fail because API-to-node tunnel is broken](advanced/a04-api-kubelet-tunnel.md)
- [A05: Azure Disk attach or mount fails across zones or nodes](advanced/a05-azure-disk-topology.md)
- [A06: Azure Files mount fails or is slow](advanced/a06-azure-files.md)
- [A07: AKS operation fails with LinkedAuthorizationFailed](advanced/a07-identity-authorization.md)
- [A08: Create, scale, or upgrade fails from quota, capacity, or throttling](advanced/a08-quota-capacity-throttling.md)
- [A09: Large cluster API server or etcd becomes slow](advanced/a09-large-cluster-control-plane.md)
- [A10: AKS managed Istio ingress fails during routing or revision changes](advanced/a10-istio-ingress.md)


## How to use a runbook

Read evidence in this order: **event/error → affected scope → recent change → component state → dependency path**. Make one hypothesis at a time, run a check that can disprove it, apply the smallest justified correction, and verify from the original client path.

Some symptoms have several valid causes. A runbook provides a decision path, not an automatic diagnosis. Commands with Azure resource changes are deliberately described rather than blindly scripted because identity, subnet, route, quota, and disruption choices are environment-specific.

## Coverage and maintenance

- [Coverage matrix](COVERAGE.md) maps symptoms to runbooks.
- [Source register](SOURCES.md) records primary references and review dates.
- [Contribution guide](CONTRIBUTING.md) defines evidence required for new issue families.
- `python3 scripts/validate_aks_atlas.py` checks structure, identifiers, source links, and index coverage.

Last reviewed: 2026-09-16.
