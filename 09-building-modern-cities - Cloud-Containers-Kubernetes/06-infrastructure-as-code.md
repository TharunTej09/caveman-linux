# 06 — Infrastructure as Code

> “If the city exists only in one builder's memory, the city cannot be rebuilt.” — Chief Grog

## 🎯 Learning Objectives

- Explain infrastructure as code, desired state, providers, resources, modules, and state.
- Describe a safe format, validate, plan, review, apply, and verify workflow.
- Understand why state is sensitive and must be protected.
- Recognise drift, idempotence, dependencies, and lifecycle risks.
- Review a Terraform plan before making infrastructure changes.

## 🏕️ Caveman Story

Chief Grog once built roads from spoken instructions. Every district ended up different, and no one could reproduce a damaged bridge.

He creates versioned stone blueprints. Builders review each proposed change, compare it with the existing city, and produce a plan before moving a single rock.

The city ledger records which real bridge belongs to each blueprint symbol. Losing the ledger would make future work dangerous, so Grog locks, backs up, and protects it.

## 🖼️ Big Concept Illustration

![Chief Grog reviewing a versioned infrastructure blueprint before builders change the modern city](../images/09-building-modern-cities/infrastructure-as-code-hero.png)

```text
Write code → format → validate → plan → human/policy review
                                      ↓
                                approved apply
                                      ↓
                         verify reality + monitor drift

Configuration + State + Provider APIs = Managed infrastructure
```

| Caveman system | Infrastructure as Code |
| --- | --- |
| City blueprint | Configuration |
| Builder guild | Provider |
| Bridge or workshop | Resource |
| Reusable district plan | Module |
| City ownership ledger | State |
| Proposed construction list | Plan |

## 📖 Concept Explained Simply

Infrastructure as Code (IaC) represents infrastructure in version-controlled configuration instead of relying on undocumented manual actions.

- A **provider** communicates with a platform API.
- A **resource** describes an infrastructure object.
- A **module** packages reusable configuration.
- **State** maps configuration addresses to real objects and stores known attributes.
- A **plan** compares configuration, state, and refreshed remote reality to propose actions.
- **Drift** occurs when real infrastructure changes outside the managed workflow.

Declarative tools describe the desired result. **Idempotence** means repeating an operation with the same desired state should converge without unnecessary change, though provider behaviour and external side effects still require care.

Terraform and OpenTofu use similar workflows and configuration language, but they are separate projects with different licensing, releases, and ecosystems. Choose deliberately and pin tool and provider versions.

### Why Should I Care?

IaC makes changes reviewable, repeatable, testable, and auditable. It can also reproduce mistakes at enormous speed. Safe automation requires protected state, least-privilege credentials, policy checks, approvals, and recovery planning.

## 🌍 Real Linux Example

A pull request changes a cloud load balancer and Kubernetes cluster. CI formats and validates the code, security policy checks the proposal, and a speculative plan is reviewed. After approval, automation creates a fresh saved plan, applies that exact artifact with a locked remote state, validates service health, and records the result.

For AI infrastructure, IaC can define GPU node pools, networks, storage, identities, registries, and observability. Capacity availability and high cost make an accurate plan and cleanup policy especially important.

## 🛠️ Commands Introduced

The examples use Terraform. Run them only in a disposable lab configuration with non-production credentials. Review provider-specific behaviour and every proposed action.

### Prepare and Check Configuration

```bash
terraform init
terraform fmt -check -recursive
terraform validate
```

- `init` prepares the working directory, downloads declared providers/modules, and configures the backend.
- `fmt -check -recursive` checks canonical formatting without rewriting files.
- `validate` checks syntax and internal consistency; it does not prove that remote infrastructure will work.

### Create and Review a Saved Plan

```bash
terraform plan -out=tfplan
terraform show tfplan
```

The saved plan is an opaque execution artifact. It can contain sensitive configuration and values, so protect it and never commit it. Review creates, updates, replacements, deletions, and unexpected provider changes.

For machine-readable review in controlled automation:

```bash
terraform show -json tfplan
```

JSON output may contain sensitive information. Store and process it securely.

### Apply the Reviewed Artifact

```bash
terraform apply tfplan
terraform output
terraform state list
```

- `apply tfplan` executes the previously saved plan.
- `output` reads declared outputs; sensitive outputs require careful handling.
- `state list` lists managed addresses without changing infrastructure.

An old plan can become unsafe as remote reality changes. Production pipelines should generate and approve plans within a controlled workflow, use remote state locking, and prevent concurrent applies.

## 💡 Caveman Tip

Treat the plan as a change request, not colourful terminal output. Ask what will be created, changed in place, replaced, or deleted—and what user impact each action can cause.

## ⚠️ Common Mistakes

- Committing state files, saved plans, secrets, or credentials.
- Applying without reviewing replacement and deletion actions.
- Sharing one local state file across a team.
- Making manual console changes and ignoring drift.
- Running concurrent applies without state locking.
- Using broad administrator credentials in automation.
- Changing provider versions without testing and reviewing the new plan.
- Assuming `terraform validate` checks permissions, quotas, cost, or runtime health.

## 🧪 Hands-on Lab

### Final Mission: Review the City Blueprint

Use a disposable IaC project and a low-risk local or sandbox provider:

1. Pin the required Terraform and provider versions.
2. Define one harmless lab resource and one useful output.
3. Initialise, check formatting, and validate the configuration.
4. Create a saved plan and classify every proposed action.
5. Inspect the human-readable plan and protect the plan artifact.
6. Apply only the reviewed saved plan.
7. Verify the real result independently and list managed state addresses.
8. Change one attribute, review the new plan, and explain drift versus intended change.
9. Remove lab resources through a separately reviewed plan when authorised.

## 📝 Quick Recap

```text
Versioned intent + protected state + provider API
        ↓
Format → validate → plan → review → apply → verify
        ↓
Repeatable, auditable infrastructure change
```

## 🧠 Interview Questions

1. What problem does infrastructure as code solve?
2. Why does Terraform need state, and why is state sensitive?
3. What is the difference between validation and planning?
4. What is infrastructure drift?
5. Why apply a saved plan in automation?
6. How would you protect an IaC production workflow?
7. When can a declarative change still cause an outage?

## 📚 What's Next

You can now trace the modern platform from physical hardware to VMs, cloud resources, containers, Kubernetes, and versioned infrastructure. Return to the [module map](README.md), complete the final mission, and use these layers as the foundation for AI infrastructure.
