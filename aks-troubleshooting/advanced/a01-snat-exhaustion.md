# A01: Intermittent outbound failures from SNAT exhaustion

**Level:** Advanced
**Symptom:** Outbound connections intermittently time out or reset during concurrency spikes.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

Correlate failures with Azure Load Balancer SNAT metrics; inspect connection reuse, destination fan-out, idle connections, outbound IPs, allocated ports, and NAT architecture.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- High new-connection rate with little connection reuse
- Long idle connections retain ports
- Too few outbound IPs/ports for peak concurrency
- Retries amplify exhaustion

## Resolution path

1. Fix clients to reuse connections and use sensible timeouts/backoff
2. Use NAT Gateway or appropriately size outbound IP/port allocation
3. Reduce unnecessary destination fan-out
4. Validate under peak-like load; more ports alone can hide an application leak

## Verify

SNAT failure metrics remain zero under peak load and outbound latency stabilizes.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Snat Port Exhaustion](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/snat-port-exhaustion)
- [Nat Gateway](https://learn.microsoft.com/en-us/azure/aks/nat-gateway)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
