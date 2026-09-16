# I01: AKS cannot pull from ACR although the image exists

**Level:** Intermediate
**Symptom:** Pull events show 401, 403, timeout, or DNS failures against ACR.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`az aks check-acr -g <rg> -n <cluster> --acr <registry>.azurecr.io`; inspect the pod event and determine whether the failure is identity, DNS, network, or content.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Kubelet identity lacks AcrPull
- ACR firewall/private endpoint denies the node path
- Private DNS resolves incorrectly
- Repository scope token or imagePullSecret is invalid

## Resolution path

1. Grant AcrPull to the kubelet identity at the minimum ACR scope
2. Allow the AKS subnet or configure private endpoint connectivity and DNS
3. Rotate only the failed secret/token and update the workload
4. Retest from a new pod; cached images can hide a continuing failure

## Verify

A node without the cached image can pull it successfully.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Cannot Pull Image From Acr To Aks Cluster](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/cannot-pull-image-from-acr-to-aks-cluster)
- [Cluster Container Registry Integration](https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
