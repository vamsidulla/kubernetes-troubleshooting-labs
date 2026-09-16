# A06: Azure Files mount fails or is slow

**Level:** Advanced
**Symptom:** Mount events show timeout, access denied, missing share, DNS, SMB/NFS, or secret errors.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

Confirm the share exists; resolve the storage endpoint from nodes; test the protocol port (SMB 445 or required NFS path); inspect private endpoint DNS, firewall, secret, CSI logs, and mount options.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Share or secret is wrong
- NSG/firewall blocks storage traffic
- Private endpoint DNS resolves incorrectly
- SMB/NFS protocol or mount options do not match the account
- Identity/key access is invalid

## Resolution path

1. Correct share and credential references
2. Allow the exact storage endpoint and protocol path
3. Fix private DNS zone links/forwarding
4. Use Microsoft-recommended mount options for the chosen protocol
5. Measure before and after performance changes

## Verify

New pods mount reliably from every intended node pool and workload I/O meets its target.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Fail To Mount Azure File Share](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/storage/fail-to-mount-azure-file-share)
- [Mountoptions Settings Azure Files](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/storage/mountoptions-settings-azure-files)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
