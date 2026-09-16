# I03: Ingress returns 404, 502, timeout, or TLS errors

**Level:** Intermediate
**Symptom:** Traffic reaches an ingress path but routing or TLS termination is incorrect.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl describe ingress <ing> -n <ns>`; verify ingressClassName, host/path, backend Service/port, endpoints, controller pods/logs, TLS secret, and DNS.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Request host/path does not match a rule
- Wrong ingress class or controller is absent
- Backend has no ready endpoints
- TLS secret is missing, expired, or in another namespace
- Load balancer, NSG, or Application Gateway blocks the outer hop

## Resolution path

1. Test backend Service inside the cluster first
2. Correct class, host, path, service name, and port
3. Place a valid TLS secret in the ingress namespace or fix the certificate controller
4. Trace client → DNS → Azure frontend → controller → Service → pod

## Verify

The correct certificate is served and controller access logs show a successful request to a ready backend.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Connection Issues Application Hosted Aks Cluster](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/connection-issues-application-hosted-aks-cluster)
- [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
