# B01: kubectl cannot connect to the cluster

**Level:** Beginner
**Symptom:** `kubectl` reports timeout, certificate, context, or server connection errors.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

Separate local kubeconfig problems from API reachability: `kubectl config current-context`; `kubectl cluster-info`; `az aks show -g <rg> -n <cluster> -o table`; `az aks get-credentials -g <rg> -n <cluster> --overwrite-existing`.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Wrong context or stale kubeconfig
- The cluster is stopped or failed
- Private API DNS or network path is unavailable
- Authorized IP ranges or a firewall block the client

## Resolution path

1. Confirm subscription, resource group, cluster name, and current context
2. Refresh credentials only for the intended personal or approved cluster
3. For a private cluster, test DNS resolution and routing from an allowed network
4. Use AKS diagnostics and Azure Activity Log when the control plane state is unhealthy

## Verify

`kubectl get nodes` succeeds and the API endpoint resolves from the intended client network.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Connection Issues Application Hosted Aks Cluster](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/connection-issues-application-hosted-aks-cluster)
- [Access Private Cluster](https://learn.microsoft.com/en-us/azure/aks/access-private-cluster)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
