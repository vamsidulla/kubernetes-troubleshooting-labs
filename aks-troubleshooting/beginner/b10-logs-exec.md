# B10: Logs or exec target the wrong container

**Level:** Beginner
**Symptom:** Troubleshooting commands fail or display incomplete evidence in a multi-container pod.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl get pod <pod> -n <ns> -o 'jsonpath={.spec.containers[*].name}{"\n"}'`; use `-c <container>`; include `--previous` after restarts.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- A sidecar was selected by default
- The failed container already restarted
- The image lacks a shell or diagnostic tools
- Logs were never written to stdout/stderr

## Resolution path

1. Name the container explicitly
2. Use previous logs and termination state
3. Use `kubectl debug` with an approved diagnostic image instead of modifying the app image
4. Send application logs to stdout/stderr and centralize retention

## Verify

Evidence comes from the failing container instance and includes the relevant time window.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Debug Running Pod](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)
- [Primary documentation](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/#ephemeral-container)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
