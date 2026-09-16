# A03: Private AKS API is unreachable

**Level:** Advanced
**Symptom:** The cluster exists but clients outside the approved network cannot resolve or connect to the private API FQDN.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

Resolve the API FQDN from the failing client; compare private IP, private DNS zone links, custom DNS forwarding, peering, VPN/ExpressRoute routing, NSGs, and TCP 443.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Private DNS zone is not linked to the client VNet
- Custom DNS does not forward the private zone
- Peering or on-prem routes do not reach the private endpoint
- Firewall/NSG blocks the resolved private IP

## Resolution path

1. Link the correct private DNS zone or configure conditional forwarding
2. Provide an approved network path such as peering, VPN, ExpressRoute, or jump host
3. Allow the precise API destination and port
4. Avoid exposing the API publicly as a shortcut unless the security design changes

## Verify

The approved client resolves the private IP and completes an authenticated API request.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Private Clusters](https://learn.microsoft.com/en-us/azure/aks/private-clusters)
- [Access Private Cluster](https://learn.microsoft.com/en-us/azure/aks/access-private-cluster)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
