# 02 — Cloud Computing

> “The city grows faster when it can rent what it needs without quarrying a new mountain.” — Chief Grog

## 🎯 Learning Objectives

- Define cloud computing beyond “someone else's computer.”
- Explain regions, availability zones, elasticity, and service models.
- Compare IaaS, PaaS, and SaaS responsibilities.
- Recognise cost, resilience, identity, and automation considerations.
- Inspect first-boot cloud configuration with `cloud-init`.

## 🏕️ Caveman Story

The village receives a sudden order for ten thousand spears. Chief Grog cannot build workshops, roads, and storage caves quickly enough.

A distant city offers ready-made land and workshops. Grog can request them when needed, pay for what he uses, and release them afterward.

The city maintains the mountain and shared roads. Grog still controls his workers, tools, access rules, and stored treasure. Renting removes some work—but not responsibility.

## 🖼️ Big Concept Illustration

![Chief Grog requesting expandable compute storage and network resources from a cloud city](../images/09-building-modern-cities/cloud-computing-hero.png)

```text
Request through API
        ↓
Compute + storage + network + managed services
        ↓
Deploy → measure → scale → recover → release
```

| City service | Cloud concept |
| --- | --- |
| Distant territory | Region |
| Separate protected district | Availability zone |
| Rented workshop | Compute instance |
| Expandable warehouse | Object/block storage |
| Identity seal | IAM identity and policy |
| Usage ledger | Metering and billing |

## 📖 Concept Explained Simply

Cloud computing provides technology resources on demand through self-service interfaces and APIs. Important characteristics include rapid provisioning, measured usage, pooled capacity, broad network access, and the ability to scale.

- **IaaS:** the provider operates physical facilities and virtualisation; you manage the guest OS, applications, data, and much of the configuration.
- **PaaS:** the provider also manages more of the runtime and platform; you focus on application code and data.
- **SaaS:** the provider operates the complete application; you manage users, configuration, and how organisational data is used.

A **region** is a geographic deployment area. An **availability zone** is an isolated location within a region. Exact designs differ by provider, so resilience must be intentionally designed and tested.

**Scalability** is the ability to handle growth. **Elasticity** is the ability to add and remove capacity as demand changes. Neither guarantees availability, security, performance, or controlled cost.

### Why Should I Care?

Linux engineers increasingly operate systems whose disks, networks, identities, and failure boundaries are controlled by cloud APIs. Understanding the shared-responsibility boundary prevents dangerous assumptions.

## 🌍 Real Linux Example

A launch template creates an Ubuntu VM in a private subnet. At first boot, `cloud-init` sets the hostname, creates users, installs approved packages, and starts configuration automation. A load balancer sends traffic only after health checks pass.

Production systems spread critical workloads across failure domains, restrict access with identity and network policy, encrypt data, monitor cost and quotas, and test recovery. AI platforms add specialised GPU instances, high-throughput storage, model registries, and expensive idle capacity that must be managed deliberately.

## 🛠️ Commands Introduced

This lesson owns `cloud-init`, a common first-boot configuration system for cloud images. Run these commands inside a disposable cloud VM or a compatible local image.

### Check Provisioning Status

```bash
cloud-init status
cloud-init status --long
cloud-init status --wait
```

- `status` reports whether initialisation is running, done, disabled, or in error.
- `--long` includes detailed stage information.
- `--wait` blocks until completion and is useful in automation; its exit status must still be checked.

### Query Instance Metadata Safely

```bash
cloud-init query instance_id
cloud-init query v1.cloud_name
cloud-init query --all
```

`query` reads cloud-init's cached instance data. Treat `--all` output as potentially sensitive and do not paste it into public tickets.

### Analyse Boot Configuration

```bash
sudo cloud-init analyze show
sudo cloud-init analyze blame
sudo cloud-init schema --system
```

- `analyze show` displays boot-stage timing.
- `analyze blame` ranks slow cloud-init events; a slow item is evidence, not automatically the root cause.
- `schema --system` validates the system's cloud configuration where supported.

Collect a diagnostic bundle only when authorised:

```bash
sudo cloud-init collect-logs
```

The archive may contain logs, configuration, and metadata. Protect it as operational evidence.

## 💡 Caveman Tip

Before deploying, write down the shared-responsibility boundary: what the provider secures, what your team secures, and which managed service changes that boundary.

## ⚠️ Common Mistakes

- Assuming a single VM in the cloud is highly available.
- Leaving resources running and discovering the cost later.
- Giving workloads broad identity permissions.
- Embedding secrets in user data or machine images.
- Depending on one region or zone without a recovery decision.
- Rerunning cloud-init modules blindly; not every module is idempotent.
- Treating provider service limits and quotas as unlimited capacity.

## 🧪 Hands-on Lab

### Mission: Inspect a Rented Workshop

On a disposable cloud VM or cloud-compatible image:

1. Identify its region or cloud name using cached cloud-init data.
2. Check whether first-boot provisioning completed successfully.
3. Review the stages and identify the slowest event.
4. Validate the active cloud configuration.
5. Draw the shared-responsibility boundary for OS patches, firewall rules, data, and physical hardware.
6. Record the resources that continue to cost money while idle.
7. Terminate chargeable lab resources through the approved provider workflow when finished.

## 📝 Quick Recap

```text
Cloud = on-demand resources + APIs + measured usage + shared responsibility
```

Cloud changes how infrastructure is requested and operated; it does not remove the need for architecture, security, monitoring, or recovery.

## 🧠 Interview Questions

1. How does cloud computing differ from virtualisation alone?
2. What are IaaS, PaaS, and SaaS?
3. How do scalability and elasticity differ?
4. Why does one availability zone not remove every failure risk?
5. What does `cloud-init` commonly do during first boot?
6. What remains the customer's responsibility on a cloud VM?

## 📚 What's Next

VMs package an operating system. [03 — Containers](03-containers.md) shows how Linux can isolate applications while sharing one kernel.
