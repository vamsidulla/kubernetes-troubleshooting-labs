# A04: Logs, exec, or metrics fail because API-to-node tunnel is broken

**Level:** Advanced
**Symptom:** Basic API queries may work while `kubectl logs`, `exec`, port-forward, or metrics operations time out.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

Confirm ordinary API reads work; test a logs/exec operation; inspect tunnel components, node readiness, required FQDN/port access, DNS, proxy, and recent egress changes.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Tunnel component is unhealthy
- Firewall/proxy blocks the required control-plane-to-kubelet channel
- Node cannot reach required AKS endpoints
- Network customization breaks tunnel routing

## Resolution path

1. Restore documented AKS outbound requirements
2. Fix the affected tunnel/node component through supported AKS operations
3. Remove unsupported interception of the tunnel path
4. Collect diagnostics before replacing nodes when the fault recurs

## Verify

Logs and exec work on pods across multiple nodes, and tunnel components remain healthy.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Tunnel Connectivity Issues](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/tunnel-connectivity-issues)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
