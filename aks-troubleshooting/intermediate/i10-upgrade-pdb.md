# I10: AKS upgrade is blocked by drain or PDB

**Level:** Intermediate
**Symptom:** Node draining fails with eviction errors, or the upgrade stalls waiting for workloads.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl get pdb -A`; `kubectl describe pdb <pdb> -n <ns>`; inspect replica count, allowed disruptions, unhealthy pods, max surge, upgrade events, and maintenance windows.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- PDB allows zero voluntary disruptions
- Single replica cannot remain available during drain
- Unhealthy pods never become evictable
- Surge capacity, subnet IPs, quota, or node pool capacity is insufficient

## Resolution path

1. Restore workload health before upgrading
2. Use enough replicas and a PDB that expresses achievable availability
3. Plan surge nodes, IP capacity, and quota
4. Use forceful disruption only after accepting and documenting workload impact

## Verify

A preflight drain can evict workloads within the stated availability objective and the upgrade completes.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Upgrade Cluster](https://learn.microsoft.com/en-us/azure/aks/upgrade-cluster)
- [Configure Pdb](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
