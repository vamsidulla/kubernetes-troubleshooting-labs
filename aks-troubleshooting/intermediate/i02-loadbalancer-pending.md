# I02: LoadBalancer external IP remains Pending

**Level:** Intermediate
**Symptom:** A Service of type LoadBalancer never receives an IP or provisioning events show Azure errors.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl describe svc <svc> -n <ns>`; inspect events; check AKS identity permissions, public IP/SKU/region, subnet, quota, and annotations.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- AKS identity cannot manage the required network resource
- A specified public IP is in the wrong resource group, region, or SKU
- Subnet or public IP quota is exhausted
- Unsupported or conflicting service annotations

## Resolution path

1. Fix the exact authorization or resource mismatch in the event
2. Use supported load balancer annotations and IP resources
3. Increase quota or release unused addresses
4. Do not repeatedly recreate the Service before reading Azure Activity Log

## Verify

The Service receives the intended IP and Azure load-balancer health probes succeed.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Load Balancer Standard](https://learn.microsoft.com/en-us/azure/aks/load-balancer-standard)
- [Connection Issues Application Hosted Aks Cluster](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/connection-issues-application-hosted-aks-cluster)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
