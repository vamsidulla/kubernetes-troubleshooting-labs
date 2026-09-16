# B08: Pod cannot resolve a service or external name

**Level:** Beginner
**Symptom:** Applications report name resolution failures, timeouts, or intermittent DNS errors.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl exec -n <ns> <pod> -- cat /etc/resolv.conf`; run `nslookup kubernetes.default.svc.cluster.local` and the failing external name from a diagnostic pod; inspect CoreDNS pods and logs.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Wrong service name or namespace search path
- CoreDNS is unhealthy, overloaded, or cannot reach upstream DNS
- Custom VNet DNS cannot resolve Azure/private zones
- NetworkPolicy or firewall blocks UDP/TCP 53

## Resolution path

1. Test cluster-local and external names separately
2. Fix CoreDNS health/capacity before editing application retries
3. Link and configure the correct private DNS zone or forwarding path
4. Allow both UDP and TCP DNS traffic where required

## Verify

Repeated lookups resolve the expected IP from affected and unaffected nodes.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Basic Troubleshooting Dns Resolution Problems](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/dns/basic-troubleshooting-dns-resolution-problems)
- [Dns Debugging Resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
