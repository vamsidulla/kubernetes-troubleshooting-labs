# Lab 03: Intermittent events caused by competing consumers

## Scenario

An event-driven service appeared to receive messages intermittently. Event publication succeeded, the queue existed, and platform metrics showed no delivery errors. Repeated tests produced inconsistent results.

## Investigation

The investigation separated the path into stages:

1. Confirm the producer published each event.
2. Confirm the event-routing layer reported successful delivery.
3. Observe queue depth and message completion.
4. Correlate consumer logs using message identifiers.
5. Inventory every running instance using the same queue and credentials.

Example Kubernetes checks:

```bash
kubectl get deploy,statefulset,pod -A -o wide
kubectl get pods -A -l app=<consumer-label>
kubectl logs -n <namespace> -l app=<consumer-label> --prefix --since=15m
kubectl get deploy -n <namespace> <deployment> -o jsonpath='{.spec.replicas}{"\n"}'
```

The missing messages were not lost. A second copy of the service was running outside the local Kubernetes environment and reading from the same queue. The broker distributed messages between both active consumers.

## Root cause

The system used competing-consumer semantics: a message is processed by one eligible receiver, not broadcast to every receiver. Two independently running service instances shared the same queue, so test messages were split between them.

## Corrective actions

- Stop the unintended consumer or assign an isolated development queue.
- Give each environment distinct queue names or subscriptions.
- Add environment and instance identity to structured logs.
- Track active receivers and message completion counts.
- Include external processes and VMs in the consumer inventory, not only Kubernetes replicas.

## Interview takeaway

When an event is published successfully but appears missing at one consumer, verify whether another eligible consumer completed it. Healthy broker metrics do not prove that a particular instance received the message.
