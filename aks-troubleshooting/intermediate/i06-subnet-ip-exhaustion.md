# I06: Scale or upgrade fails because the subnet is full

**Level:** Intermediate
**Symptom:** AKS reports `InsufficientSubnetSize` or `SubnetIsFull`; new nodes or pods cannot obtain addresses.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`az network vnet subnet show --ids <subnet-id>`; review network plugin, pod subnet, maxPods, current nodes, surge nodes, and reserved addresses.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Subnet CIDR was sized only for steady state
- Upgrade surge needs temporary node/IP capacity
- Azure CNI pod IP demand exceeds available addresses
- Unused interfaces or resources still hold IPs

## Resolution path

1. Calculate peak demand including max surge and growth
2. Expand or migrate to an adequately sized subnet following supported AKS procedures
3. Consider Azure CNI Overlay when it fits requirements
4. Remove genuinely unused consumers after verifying ownership

## Verify

Capacity calculations cover the next scale/upgrade and the operation succeeds without exhausting free addresses.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Insufficientsubnetsize Error Advanced Networking](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/insufficientsubnetsize-error-advanced-networking)
- [Error Code Subnetisfull Upgrade](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/create-upgrade-delete/error-code-subnetisfull-upgrade)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
