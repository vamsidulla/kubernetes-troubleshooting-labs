# B05: Readiness, liveness, or startup probe failures

**Level:** Beginner
**Symptom:** A container runs but stays unready or is repeatedly restarted by a probe.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl describe pod <pod> -n <ns>`; compare probe path, port, scheme, headers, delay, timeout, and failure threshold with the actual listener.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Wrong path, named port, protocol, or host
- Application listens only on localhost or another port
- Startup is slower than the liveness delay
- Dependency checks make readiness flap

## Resolution path

1. Test the endpoint inside the pod or with an ephemeral debug container
2. Correct the probe to represent the intended health signal
3. Add startupProbe for long startup instead of weakening liveness indefinitely
4. Keep readiness focused on whether this instance should receive traffic

## Verify

The pod becomes Ready; a controlled application failure changes only the intended probe state.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Configure Liveness Readiness Startup Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
