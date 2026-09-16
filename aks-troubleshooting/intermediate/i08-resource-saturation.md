# I08: OOMKilled, CPU throttling, or eviction

**Level:** Intermediate
**Symptom:** Containers terminate with OOMKilled, latency rises under CPU pressure, or pods are evicted.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl describe pod <pod> -n <ns>`; inspect last termination reason; `kubectl top pod -A --containers`; compare observed usage with requests, limits, QoS, and node allocatable.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Memory leak or workload spike crosses the limit
- Requests are too low for scheduling and autoscaling signals
- CPU limit throttles latency-sensitive work
- Node memory or disk pressure evicts lower-priority pods

## Resolution path

1. Measure before changing requests or limits
2. Fix leaks and bound untrusted concurrency
3. Set requests from realistic percentiles and use autoscaling where appropriate
4. Protect system capacity and distribute replicas across nodes

## Verify

Load testing shows stable latency, no OOM/eviction, and expected autoscaling behavior.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Identify Memory Saturation Aks](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/availability-performance/identify-memory-saturation-aks)
- [Identify High Cpu Consuming Containers Aks](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/availability-performance/identify-high-cpu-consuming-containers-aks)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
