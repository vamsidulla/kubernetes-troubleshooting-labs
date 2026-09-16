# B09: PVC Pending or pod stuck ContainerCreating

**Level:** Beginner
**Symptom:** Storage is not provisioned, attached, or mounted.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl describe pvc <pvc> -n <ns>`; `kubectl describe pod <pod> -n <ns>`; inspect StorageClass, PV, CSI pods, zone, access mode, and events.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- StorageClass is missing or incorrect
- Disk and scheduled node are in different zones
- ReadWriteOnce disk is attached to another node
- Identity lacks disk permissions
- Node disk attachment limit is reached

## Resolution path

1. Use a supported CSI StorageClass with correct topology
2. Use WaitForFirstConsumer or suitable ZRS storage when appropriate
3. Respect access modes; avoid mounting one RWO disk across different nodes
4. Grant the cluster identity access to the disk scope
5. Scale or use a VM size with sufficient disk slots

## Verify

PVC is Bound, mount events stop, and the pod reaches Running.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Fail To Mount Azure Disk Volume](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/storage/fail-to-mount-azure-disk-volume)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
