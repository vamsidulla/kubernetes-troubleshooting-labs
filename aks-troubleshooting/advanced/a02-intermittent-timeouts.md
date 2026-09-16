# A02: Intermittent timeouts with healthy pods

**Level:** Advanced
**Symptom:** Only some requests fail; restarts or retries appear to recover temporarily.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

Correlate client, ingress, service, pod, and dependency timestamps; compare failing nodes; inspect endpoints, health probes, conntrack, SNAT, DNS, packet loss, and application connection pools.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- One unhealthy backend remains intermittently eligible
- SNAT or conntrack exhaustion
- Asymmetric routing or firewall idle timeout
- DNS returns stale/mixed answers
- Application pool exhausts sockets or threads

## Resolution path

1. Remove unhealthy endpoints by fixing readiness
2. Correct connection lifecycle and Azure outbound capacity
3. Align idle timeouts and preserve symmetric paths
4. Capture packets at both ends only for the narrowed failure window

## Verify

The measured error rate stays within the service objective during sustained traffic without retry masking.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Intermittent Timeouts Or Server Issue](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/intermittent-timeouts-or-server-issue)
- [Snat Port Exhaustion](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/snat-port-exhaustion)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
