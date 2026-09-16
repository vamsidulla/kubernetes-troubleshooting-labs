# A05: Azure Disk attach or mount fails across zones or nodes

**Level:** Advanced
**Symptom:** Stateful pods remain ContainerCreating with attach, multi-attach, topology, authorization, or disk-limit events.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

Map PVC → PV → disk → zone → pod → node; inspect access mode, StorageClass binding mode, cluster identity permissions, CSI events, and per-VM disk limits.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Zonal disk and node zones differ
- ReadWriteOnce disk is attached to a different node
- Identity lacks access to an external disk
- Node reached its disk attachment limit
- Large fsGroup ownership changes delay mount

## Resolution path

1. Use topology-aware provisioning and WaitForFirstConsumer
2. Use ZRS when supported and appropriate
3. Respect RWO/RWOP semantics or choose storage designed for multi-node access
4. Grant least privilege at the disk/resource-group scope
5. Scale/rebalance nodes or choose a suitable VM size

## Verify

The pod mounts on an allowed node; failover behavior matches the storage availability design.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Fail To Mount Azure Disk Volume](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/storage/fail-to-mount-azure-disk-volume)
- [Azure Csi Disk Storage Provision](https://learn.microsoft.com/en-us/azure/aks/azure-csi-disk-storage-provision)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
