# Server Fundamentals

## Big Question

How can an entire village share important resources without losing them?

## Story

One hundred cavemen live together in a village.

Every day, they need:

- Food
- Water
- Weapons
- Tools
- Medicine

![The caveman village](../images/SH1.png)

At first, everyone keeps their supplies inside their own cave. Soon, problems begin to appear:

- Food goes missing.
- Weapons get lost.
- Tools are difficult to find.
- Nobody knows who owns each item.
- Some caves have too many supplies while others have none.

The chief needs a better system. He builds one large, protected **storage cave** where the village can keep and manage its shared resources.

![The shared storage cave](../images/SH2.png)

Whenever a hunter needs something, they travel to the storage cave and ask for it. The cave receives the request, finds the requested item, and gives it to the hunter.

In the computer world, this storage cave is called a **server**.

![The storage cave acting as a server](../images/SH3.png)

![A hunter communicating with the storage cave](../diagram/hunter.svg)

## From the Village to Technology

| Caveman World | Computer World |
|---|---|
| Hunter | Client |
| Storage Cave | Server |
| Village Road | Network |
| Asking for a spear | Request |
| Receiving the spear | Response |

## How the Client–Server Model Works

The **client** asks for a resource or service. The **server** receives the request, processes it, and sends back a response. The request and response travel through a **network**.

```text
Client  ── Request ──>  Server
Client  <─ Response ──  Server
```

In the village:

```text
Hunter  ── Asks for a spear ──>  Storage Cave
Hunter  <── Receives a spear ──  Storage Cave
```

## What Is a Server?

A **server** is a computer that provides resources or services to other computers over a network.

A server can provide many kinds of resources:

| Server Type | What It Provides |
|---|---|
| Web server | Websites and web pages |
| File server | Files and folders |
| Email server | Email messages |
| Database server | Organized data |
| Game server | Online game sessions |
| Media server | Videos, music, and images |

## Real-World Example: Watching YouTube

When you open a video on your phone:

1. Your phone acts as the **client**.
2. It sends a **request** through the internet.
3. A YouTube **server** receives the request.
4. The server sends the video back as a **response**.

```text
Phone  ── Video request ──>  Internet  ──>  YouTube Server
Phone  <────── Video ─────  Internet  <──  YouTube Server
```

## Simple Definition

A **client asks**, a **server provides**, and a **network connects them**.
