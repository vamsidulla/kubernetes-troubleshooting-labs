# A08: Create, scale, or upgrade fails from quota, capacity, or throttling

**Level:** Advanced
**Symptom:** Azure returns allocation failure, quota exceeded, SKU unavailable, or HTTP 429.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

Inspect the exact Azure error and region/SKU; check regional vCPU and family quotas, availability-zone capacity, API request rate, surge demand, and Activity Log.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- Subscription quota is lower than peak operation needs
- Chosen VM SKU/zone has no available capacity
- Rapid automation retries cause request throttling
- Upgrade surge temporarily exceeds quota

## Resolution path

1. Request quota before the maintenance window
2. Offer approved alternative VM sizes/zones or a separate node pool
3. Honor Retry-After and use exponential backoff with jitter
4. Serialize noisy infrastructure operations and make automation idempotent

## Verify

The operation succeeds without repeated retries and monitoring shows no sustained throttling.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [Error Code Aksrequeststhrottled](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/create-upgrade-delete/error-code-aksrequeststhrottled)
- [View Quotas](https://learn.microsoft.com/en-us/azure/quotas/view-quotas)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
