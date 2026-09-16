# B03: ImagePullBackOff or ErrImagePull

**Level:** Beginner
**Symptom:** A pod cannot download its image.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl describe pod <pod> -n <ns>` and read the exact pull event; confirm image name, tag, registry, and architecture.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Image or tag does not exist
- Registry authentication or AcrPull permission is missing
- Registry firewall, private endpoint, DNS, or egress blocks access
- The image architecture does not match the node

## Resolution path

1. Correct the immutable image reference
2. Validate AKS-to-ACR integration or the imagePullSecret
3. Test registry DNS and HTTPS connectivity from the node path
4. Publish a compatible multi-architecture image when required

## Verify

A newly created pod reaches Running without repeated pull events.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Cannot Pull Image From Acr To Aks Cluster](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/cannot-pull-image-from-acr-to-aks-cluster)
- [Images](https://kubernetes.io/docs/concepts/containers/images/)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
