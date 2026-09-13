# Lab 07: Pending Pod from unmatched node selection

Run commands from the repository root in a disposable learning cluster. These examples do not require cloud resources.

## Set up

```bash
kubectl config current-context
kubectl create namespace troubleshooting-labs --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -n troubleshooting-labs -f labs/07-node-selector/broken.yaml
```

Observe the failure before applying the fix. Image downloads and restart backoff can take time.

## Investigate

```bash
kubectl get nodes -l troubleshooting.example.com/placement=missing
kubectl get pods -n troubleshooting-labs -l app=node-selector-lab -o wide
kubectl describe pods -n troubleshooting-labs -l app=node-selector-lab
kubectl get nodes --show-labels
```

## Expected evidence

Prerequisite: the first command must return no matching nodes. If it finds one, skip this lab rather than relabeling shared nodes. Expect `Pending`, no assigned node, and `FailedScheduling` events referring to node affinity/selector mismatch.

## Explain your diagnosis

Will adding CPU or raising replica count solve a strict label mismatch?

<details>
<summary>Reveal root cause, fix, and interview answer</summary>

The deployment requires a label absent from every node. The fix removes the unnecessary constraint. No node changes are needed. Prevention: validate placement requirements against available node pools and monitor unschedulable Pods.

```bash
kubectl apply -n troubleshooting-labs -f labs/07-node-selector/fixed.yaml
kubectl rollout status -n troubleshooting-labs deployment/node-selector-lab --timeout=120s
```

No. Node eligibility is a hard condition independent of available CPU. After the fix, verify that a node is assigned and the Pod becomes Ready. If it remains Pending, inspect events for a separate constraint such as taints or insufficient resources.

</details>

## Cleanup and repeat

```bash
kubectl delete -n troubleshooting-labs -f labs/07-node-selector/fixed.yaml --ignore-not-found
```

Delete these lab resources before repeating the broken setup. Do not apply the entire labs directory recursively: broken and fixed files deliberately define the same objects.

## Validation status

Manifests were parsed and checked for consistent references. Expected runtime evidence is instructional; no cluster execution results are claimed.
