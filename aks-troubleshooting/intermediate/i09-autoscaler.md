# I09: Cluster autoscaler does not add or remove nodes

**Level:** Intermediate
**Symptom:** Pods remain Pending or empty nodes never scale down even though autoscaling is enabled.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl describe pod <pending-pod> -n <ns>`; inspect autoscaler profile/logs and node-pool min/max; look for unhelpable scheduling constraints, quota, PDBs, local storage, and safe-to-evict annotations.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Pod cannot fit any available node-pool shape
- Node pool reached maximum or subscription quota
- Affinity, taints, zones, or PVC topology make the pod unhelpable
- PDB or non-evictable workload prevents scale-down

## Resolution path

1. Ensure at least one autoscaled pool can satisfy the complete pod constraints
2. Raise pool maximum/quota or add the appropriate pool
3. Correct impossible scheduling rules
4. Adjust disruption and eviction settings based on availability requirements

## Verify

A controlled pending workload triggers scale-up and an eligible empty node later scales down.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Cluster Autoscaler Overview](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler-overview)
- [Assign Pod Node](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
