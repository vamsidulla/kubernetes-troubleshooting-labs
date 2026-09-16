# B06: Pod remains Pending

**Level:** Beginner
**Symptom:** The scheduler cannot place a pod on any node.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl describe pod <pod> -n <ns>`; `kubectl get events -n <ns> --sort-by=.metadata.creationTimestamp`; `kubectl get nodes --show-labels`.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Insufficient requested CPU or memory
- Taint without a toleration
- Node selector, affinity, topology, or zone constraint has no match
- PVC is unbound
- Maximum pods or IP capacity is reached

## Resolution path

1. Fix impossible constraints or provision the required node pool
2. Set realistic requests using observed usage
3. Add only intentional tolerations
4. Resolve PVC or IP capacity before forcing scheduling

## Verify

Scheduler events clear and the pod receives a node without violating workload requirements.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Kube Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/)
- [Node Not Ready Basic Troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/availability-performance/node-not-ready-basic-troubleshooting)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
