# I07: Node becomes NotReady or reports pressure

**Level:** Intermediate
**Symptom:** Pods are evicted or stop scheduling; node conditions show MemoryPressure, DiskPressure, PIDPressure, or NetworkUnavailable.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl describe node <node>`; `kubectl get events --all-namespaces --sort-by=.metadata.creationTimestamp`; `kubectl top node`; inspect kubelet/container runtime and AKS diagnostics.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Memory, disk, PID, CPU, or IOPS saturation
- Network/DNS/firewall change breaks control-plane connectivity
- Container runtime or kubelet is unhealthy
- Underlying VM or platform fault

## Resolution path

1. Cordon and drain only when disruption budgets and capacity allow
2. Remove the resource pressure and fix the responsible workloads
3. Restore required control-plane network paths
4. Use node image upgrade/reimage or Microsoft support for persistent platform faults

## Verify

The node remains Ready under normal load and the triggering pressure metric stays below its threshold.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Node Not Ready Basic Troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/availability-performance/node-not-ready-basic-troubleshooting)
- [Node Not Ready After Being Healthy](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/availability-performance/node-not-ready-after-being-healthy)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
