# 03 — AI Model Serving

> “A wise stone hidden in a vault helps nobody. Build a safe counter where the city can ask, wait, and receive an answer.” — Chief Grog

## 🎯 Learning Objectives

- Explain model serving and online inference.
- Follow a request through queueing, batching, generation, and response.
- Compare latency, throughput, concurrency, and time to first token.
- Inspect a vLLM-compatible service through health and API endpoints.
- Recognise production needs such as authentication, scaling, versioning, and rollback.

## 🏕️ Caveman Story

Chief Grog opens the thinking workshop to the public. At first, every visitor walks straight to the thinking stone. Soon, requests collide and nobody knows whose answer belongs where.

Grog builds a guarded counter, an orderly queue, a clerk who combines compatible jobs, and several identical workshops. A lookout checks whether each workshop is ready before sending it visitors.

The model has become a **served application**.

## 🖼️ Big Concept Illustration

![Chief Grog operating a reliable model-serving workshop with queues and replicas](../images/10-teaching-the-city-to-think/ai-model-serving-hero.png)

```text
Client
  ↓
Authentication → Rate limit → Load balancer
                                ↓
                         Request queue
                                ↓
                     Batching / Scheduler
                                ↓
                    Model replicas on GPUs
                                ↓
                     Tokens stream to client
```

| Caveman workshop | Model serving |
| --- | --- |
| Public counter | API endpoint |
| Guard | Authentication and policy |
| Waiting line | Request queue |
| Grouped scrolls | Dynamic batching |
| Thinking workshop | Model server |
| Several workshops | Replicas |
| First answer stone | Time to first token |
| Complete answer scroll | End-to-end latency |

## 📖 Concept Explained Simply

**Model serving** loads a trained model and exposes it through an interface so applications can request inference.

- A **serving engine** manages model loading, request scheduling, batching, memory, and output generation.
- **Latency** is how long a request takes. For streaming LLMs, separate time to first token from time per output token.
- **Throughput** measures work completed over time, such as requests or tokens per second.
- **Concurrency** is the number of requests active at once.
- **Batching** combines work to improve accelerator efficiency, but waiting too long for a batch can hurt latency.
- **Autoscaling** adds or removes capacity from signals such as queue depth or concurrency; GPU replicas may start slowly because model weights are large.

### Why Should I Care?

A model that works in a notebook is not automatically a reliable service. Production serving must handle competing requests, bad inputs, overload, deployments, failures, access controls, and measurable service objectives.

## 🌍 Real Linux Example

A vLLM server loads an instruction model onto one or more GPUs and exposes an HTTP API. A gateway authenticates callers and applies limits. A load balancer routes traffic only to ready replicas. During a release, the old version remains available until the new version passes health, capacity, and quality checks.

For sensitive services, bind the raw model server to a private interface and place authentication, TLS, request limits, and audit controls in front of it. OpenAI-compatible describes an API shape; it does not make every backend behaviour identical.

## 🛠️ Commands Introduced

Run these only in a disposable lab with a small model that fits the available hardware. Model downloads can be large and gated models may require authorisation.

### Start a Lab Server

```bash
vllm serve MODEL_ID --host 127.0.0.1 --port 8000
```

- Replace `MODEL_ID` with an approved small instruction model.
- Binding to `127.0.0.1` keeps the unprotected lab endpoint local.
- A chat request requires a compatible model and chat template.

### Check Readiness and Available Models

```bash
curl --fail --silent --show-error http://127.0.0.1:8000/health
curl --fail --silent --show-error http://127.0.0.1:8000/v1/models
```

- `--fail` returns an error for unsuccessful HTTP status codes.
- `--silent --show-error` removes progress noise but preserves errors.
- `/health` checks whether the server can accept work; `/v1/models` shows the served model identity.

### Send One Chat Request

```bash
curl --fail --silent --show-error \
  http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "MODEL_ID",
    "messages": [{"role": "user", "content": "Explain Linux in one sentence."}],
    "max_tokens": 40,
    "temperature": 0
  }'
```

`curl` is introduced here as the client for a serving API. The small output limit controls lab cost and time; deterministic settings do not guarantee factual accuracy.

### Observe Streaming

```bash
curl --no-buffer --fail --silent --show-error \
  http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"MODEL_ID","messages":[{"role":"user","content":"Count to five."}],"stream":true,"max_tokens":20}'
```

`--no-buffer` displays streamed chunks as they arrive, making time to first token visible to the learner.

## 💡 Caveman Tip

Measure at the boundary users experience. Fast token generation cannot compensate for a long queue, slow retrieval, or overloaded gateway.

## ⚠️ Common Mistakes

- Exposing an unauthenticated model endpoint publicly.
- Using average latency without percentiles or time-to-first-token.
- Increasing batch size until interactive requests feel slow.
- Scaling only on CPU while GPU memory or queue depth is saturated.
- Treating a healthy process as proof the model is ready and correct.
- Deploying a new model or prompt without versioning and rollback.
- Logging complete prompts and responses without privacy controls.

## 🧪 Hands-on Lab

### Mission: Open the Answer Counter

1. Start a small approved model on localhost.
2. Verify the health endpoint before sending inference.
3. Confirm the exact served model ID.
4. Send one bounded non-streaming request.
5. Send one bounded streaming request and observe the first chunk.
6. Increase concurrent lab requests gradually and watch queueing behaviour.
7. Propose readiness, rate-limit, timeout, and rollback rules.
8. Stop the lab server with `Ctrl+C` after requests finish.

## 📝 Quick Recap

```text
Request → Guard → Queue → Batch → Model → Streamed response
              latency ↔ throughput ↔ cost
```

## 🧠 Interview Questions

1. What does a model server do?
2. How do latency, throughput, and concurrency differ?
3. What is time to first token?
4. Why can batching improve throughput but hurt latency?
5. Which signals would you use to scale an LLM service?
6. What must be tested before shifting traffic to a new model version?

## 📚 What's Next

The model may need trusted knowledge beyond its weights. [04 — Vector Databases](04-vector-databases.md) explains how the city retrieves information by meaning.
