# A09: Large cluster API server or etcd becomes slow

**Level:** Advanced
**Symptom:** Controllers lag, list/watch requests time out, or API latency/throttling rises at scale.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

Measure API latency and request rates; identify high-cardinality/list clients, object counts, noisy controllers, large Secrets/ConfigMaps, event volume, and webhook latency.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Clients repeatedly list all objects instead of using efficient watches
- Excess object/event churn loads etcd
- Slow or unavailable admission webhooks block writes
- Controller concurrency and retries create request storms

## Resolution path

1. Fix the noisiest client/controller based on metrics and audit evidence
2. Scope watches and use pagination/caching
3. Reduce object churn and oversized resources
4. Set webhook timeouts/failure policy deliberately and keep endpoints highly available
5. Engage Microsoft support for control-plane limits after workload causes are quantified

## Verify

API latency and throttling remain stable during representative controller and deployment activity.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Troubleshoot Apiserver Etcd](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/create-upgrade-delete/troubleshoot-apiserver-etcd)
- [Aks At Scale Troubleshoot Guide](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/create-upgrade-delete/aks-at-scale-troubleshoot-guide)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
