# I04: Traffic fails after NetworkPolicy or NSG changes

**Level:** Intermediate
**Symptom:** Connections time out even though pods and Services look healthy.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl get networkpolicy -A`; compare source/destination labels and namespaces; inspect effective NSG rules and route tables; test pod IP, ClusterIP, and external hop separately.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Default-deny policy lacks DNS or application allow rules
- Policy selectors do not match intended workloads
- Subnet NSG blocks node, pod, load-balancer, or storage traffic
- A route sends return traffic through a different path

## Resolution path

1. Create explicit least-privilege ingress and egress rules including DNS
2. Validate policies in a non-production namespace with named probes
3. Allow the required traffic in custom subnet NSGs
4. Correct asymmetric routing rather than broadening every rule

## Verify

The exact source-to-destination flow succeeds while unrelated flows remain denied.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Custom Nsg Blocks Traffic](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/custom-nsg-blocks-traffic)
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
