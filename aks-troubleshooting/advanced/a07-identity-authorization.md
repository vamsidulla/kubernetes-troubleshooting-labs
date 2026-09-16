# A07: AKS operation fails with LinkedAuthorizationFailed

**Level:** Advanced
**Symptom:** Cluster creation or an update fails because the AKS identity cannot join or manage a linked Azure resource.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

Read the complete error: capture the caller identity, resource ID, and denied action; verify role assignments at the linked resource scope and check Activity Log.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Role is assigned to the wrong identity
- Permission is granted at the AKS resource but not the linked VNet, route table, DDoS plan, disk, or private DNS zone
- Role propagation is incomplete
- A custom role omits the exact join/action permission

## Resolution path

1. Grant the minimum built-in/custom role containing the denied action at the correct scope
2. Confirm whether control-plane, cluster, or kubelet identity performs the operation
3. Wait for propagation and retest once
4. Remove stale identity assumptions after migration from service principals

## Verify

The exact previously denied operation succeeds, and the identity has no unrelated broad permissions.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Linkedauthorizationfailed Error](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/error-codes/linkedauthorizationfailed-error)
- [Use Managed Identity](https://learn.microsoft.com/en-us/azure/aks/use-managed-identity)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
