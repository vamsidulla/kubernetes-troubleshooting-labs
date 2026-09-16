# Contributing an AKS issue family

Add a new runbook only when it represents a distinct root cause or decision path. Another error string for an existing cause belongs in that runbook.

A contribution must include:

1. A sanitized symptom and exact error text.
2. Affected scope and AKS/Kubernetes versions.
3. Evidence that separates the cause from similar causes.
4. Read-only diagnostic steps before changes.
5. The smallest supported correction and a rollback consideration.
6. A verification from the original client path.
7. At least one current Microsoft or Kubernetes primary source.

Never contribute customer names, subscriptions, tenant IDs, internal hostnames/IPs, kubeconfigs, tokens, Secret values, or proprietary manifests. Do not claim a procedure was tested unless the environment and result are stated.
