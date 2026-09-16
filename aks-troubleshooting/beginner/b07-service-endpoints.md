# B07: Service has no endpoints or reaches the wrong port

**Level:** Beginner
**Symptom:** The pod works directly but the Service fails or shows no ready backends.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl get pods -n <ns> --show-labels`; `kubectl describe svc <svc> -n <ns>`; `kubectl get endpointslice -n <ns> -l kubernetes.io/service-name=<svc> -o yaml`.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Service selector does not match pod labels
- Pods fail readiness and are excluded
- targetPort differs from the application listener
- TCP/UDP protocol differs

## Resolution path

1. Make selectors match stable pod labels
2. Fix readiness before changing the Service
3. Map service port to the correct targetPort and protocol
4. Test pod IP first, then ClusterIP, then ingress/load balancer

## Verify

EndpointSlices contain ready pod addresses and an in-cluster request to the Service succeeds.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Connection Issues Application Hosted Aks Cluster](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/connection-issues-application-hosted-aks-cluster)
- [Debug Service](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
