# B04: CrashLoopBackOff

**Level:** Beginner
**Symptom:** The image starts, exits, and Kubernetes restarts it with increasing delay.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl get pod <pod> -n <ns> -o wide`; `kubectl describe pod <pod> -n <ns>`; `kubectl logs <pod> -n <ns> --previous`; inspect `.status.containerStatuses`.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Application startup error
- Missing configuration or secret
- Wrong command, arguments, or working directory
- Liveness probe kills a slow but healthy startup
- OOM termination

## Resolution path

1. Use the previous-container logs and exit code to fix the application cause
2. Verify referenced ConfigMaps and Secrets exist with expected keys
3. Use startupProbe for slow initialization
4. For OOMKilled, measure usage and correct requests, limits, or the memory leak

## Verify

Restart count stops increasing and readiness becomes true.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Connection Issues Application Hosted Aks Cluster](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/connection-issues-application-hosted-aks-cluster)
- [Debug Running Pod](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
