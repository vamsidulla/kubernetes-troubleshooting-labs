# Lab 04: ImagePullBackOff from an invalid tag

Run commands from the repository root in a disposable learning cluster. These examples do not require cloud resources.

## Set up

```bash
kubectl config current-context
kubectl create namespace troubleshooting-labs --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -n troubleshooting-labs -f labs/04-imagepullbackoff/broken.yaml
```

Observe the failure before applying the fix. Image downloads and restart backoff can take time.

## Investigate

```bash
kubectl get pods -n troubleshooting-labs -l app=image-pull-lab
kubectl describe pods -n troubleshooting-labs -l app=image-pull-lab
kubectl get deployment image-pull-lab -n troubleshooting-labs -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

## Expected evidence

Expect `ErrImagePull` followed by `ImagePullBackOff`. Events should identify a missing image/tag. Registry rate limits, authentication failures, and network timeouts are different causes; follow the event text rather than assuming all pull errors have this cause.

## Explain your diagnosis

Why would restarting the Pod fail to solve this? Would container logs help?

<details>
<summary>Reveal root cause, fix, and interview answer</summary>

The specified tag does not exist. Select a valid image reference. The corrected deployment creates a new Pod; no application configuration change is needed. Prevention: validate image references in CI and promote immutable digests.

```bash
kubectl apply -n troubleshooting-labs -f labs/04-imagepullbackoff/fixed.yaml
kubectl rollout status -n troubleshooting-labs deployment/image-pull-lab --timeout=120s
```

The replacement Pod requests the same invalid tag. The application has not started, so there are no application logs to inspect. Events are the useful evidence.

</details>

## Cleanup and repeat

```bash
kubectl delete -n troubleshooting-labs -f labs/04-imagepullbackoff/fixed.yaml --ignore-not-found
```

Delete these lab resources before repeating the broken setup. Do not apply the entire labs directory recursively: broken and fixed files deliberately define the same objects.

## Validation status

Manifests were parsed and checked for consistent references. Expected runtime evidence is instructional; no cluster execution results are claimed.
