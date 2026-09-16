# I05: Pods or nodes cannot reach external endpoints

**Level:** Intermediate
**Symptom:** Package downloads, registries, Azure APIs, or external dependencies time out.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`az aks show -g <rg> -n <cluster> --query networkProfile.outboundType`; test DNS, then destination IP/port from pod and node paths; inspect firewall, UDR, NAT, and required FQDNs.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Firewall or proxy blocks required FQDN/port
- UDR sends traffic to an appliance without a valid return path
- NAT gateway/load balancer configuration is incomplete
- DNS failure is mistaken for general egress failure

## Resolution path

1. Follow the configured outbound type, not a generic diagram
2. Allow documented AKS and workload destinations
3. Fix routes and firewall SNAT/return paths
4. Use packet capture only after hop-by-hop tests identify the unresolved boundary

## Verify

DNS and TCP/TLS checks succeed from both an affected pod and the relevant node path.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Basic Troubleshooting Outbound Connections](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/basic-troubleshooting-outbound-connections)
- [Errors Arfter Restricting Egress Traffic](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/errors-arfter-restricting-egress-traffic)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
