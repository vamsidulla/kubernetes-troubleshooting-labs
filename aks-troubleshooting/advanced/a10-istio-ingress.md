# A10: AKS managed Istio ingress fails during routing or revision changes

**Level:** Advanced
**Symptom:** Gateway pods run but traffic returns timeout, 404, 503, or TLS errors, especially during canary upgrades.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

Inspect `aks-istio-ingress` deployments, Services, pods, logs, revisions, Gateway/VirtualService or Gateway API resources, backend endpoints, TLS secrets, and external/internal load balancer paths.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Gateway resource selects the wrong revision or labels
- TLS secret is absent from the ingress namespace
- Host/route/backend does not match
- Canary revisions create mixed configuration
- Azure frontend or NSG prevents traffic reaching Envoy

## Resolution path

1. Test backend and gateway separately
2. Align gateway revision labels and routing resources
3. Place and rotate the correct credential secret
4. During canary upgrades, inspect both control-plane/gateway revisions
5. Trace Envoy response flags and Azure network hops before changing mesh policy

## Verify

Requests consistently reach the intended revision and backend with the expected certificate and no Envoy upstream errors.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Istio Add On Ingress Gateway](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/extensions/istio-add-on-ingress-gateway)
- [Istio About](https://learn.microsoft.com/en-us/azure/aks/istio-about)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
