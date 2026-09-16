# B02: kubectl returns Forbidden

**Level:** Beginner
**Symptom:** The API is reachable and authentication succeeds, but an operation is denied.

## Think first

Do not begin by restarting everything. Record the failing source, destination, namespace, time window, and exact error. Compare one failing path with one healthy path whenever possible.

## First evidence

`kubectl auth whoami`; `kubectl auth can-i <verb> <resource> -n <namespace>`; inspect the relevant RoleBinding or ClusterRoleBinding.

Save the relevant output before changing the system. Replace placeholders such as `<pod>` and `<ns>`; do not paste angle brackets literally.

## Common root causes

- The Entra identity lacks an Azure AKS access role
- Kubernetes RBAC lacks the verb/resource/namespace permission
- The command targets the wrong namespace
- A group claim or assignment has not propagated

## Resolution path

1. Grant the smallest Azure and Kubernetes roles required for the job
2. Bind permissions at namespace scope when cluster-wide access is unnecessary
3. Reauthenticate after confirmed role propagation
4. Retest with `kubectl auth can-i` before rerunning the change

## Verify

`kubectl auth can-i` returns `yes` only for the intended action and scope.

## Escalate with evidence

If the issue remains, collect the resource IDs, UTC timestamps, correlation/activity IDs, relevant Kubernetes events, affected nodes/pods, and a minimal reproduction. Redact tokens, kubeconfigs, registry credentials, connection strings, and Secret values before sharing evidence.

## Sources

- [User Cannot Get Cluster Resources](https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/connectivity/user-cannot-get-cluster-resources)
- [Authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/)

Source review date: 2026-09-16. Commands are diagnostic examples; verify Azure CLI and Kubernetes version-specific syntax against the linked current documentation.
