# The Client–Server Model

## Big Question

How does a client ask a server for something and receive it?

## Story

A hunter needs a spear, but the spears are stored in the village's central storage cave.

The hunter sends a message along the village road to the chief. The chief understands the request and asks the storage worker to find a spear. The spear is then sent back to the hunter.

```text
Hunter
   ↓
Village Road
   ↓
Chief
   ↓
Storage Worker
   ↓
Hunter receives the spear
```

The hunter asks for something, the village handles the request, and the hunter receives an answer.

This is similar to how a client communicates with a server.

## From the Village to the Internet

| Caveman World | Computer World |
|---|---|
| Hunter | Client |
| Asking for a spear | Request |
| Village road | Network or internet |
| Chief and storage workers | Server and its software |
| Receiving the spear | Response |

The same journey in the computer world looks like this:

```text
Client
   ↓
Internet
   ↓
Server
   ↓
Response returns to the client
```

## The Two Main Messages

Client–server communication begins with two simple ideas: a **request** and a **response**.

### Request — Asking for Something

A **request** is a message sent by a client to ask a server for a resource or action.

Examples:

- “Send me this web page.”
- “Play this video.”
- “Save my new password.”
- “Show me my messages.”

The hunter asking for a spear is making a request.

### Response — Receiving an Answer

A **response** is the server's reply to a request.

The response might contain:

- A web page
- An image or video
- Requested data
- Confirmation that an action succeeded
- An error explaining what went wrong

The hunter receiving the spear is receiving a response.

```text
Client  ── Request ──>  Server
Client  <─ Response ──  Server
```

## A Browser Example

When you visit a website:

1. Your browser acts as the **client**.
2. It sends a **request** through the internet.
3. The website's **server** receives and processes the request.
4. The server sends a **response** containing the page.
5. Your browser displays the page.

You use this model every time you open a website, stream a video, or use an online application.

## Three Helpful Protocols

A **protocol** is a set of rules that computers follow when they communicate—like agreed rules for writing and delivering village messages.

For now, we only need a simple understanding of three protocols.

### HTTP — Rules for Web Messages

**HTTP (Hypertext Transfer Protocol)** defines how a web client and web server format and exchange requests and responses.

In simple terms, HTTP gives the browser and server a shared language for web communication.

```text
Browser  ── HTTP request ──>  Web server
Browser  <─ HTTP response ──  Web server
```

### HTTPS — Protected HTTP

**HTTPS (Hypertext Transfer Protocol Secure)** is HTTP communication protected by encryption.

Encryption helps prevent other people from reading or changing the messages while they travel across the network. HTTPS also helps the client verify that it is communicating with the intended website.

You will usually see `https://` and a padlock icon when a website uses HTTPS.

```text
HTTP   = Web communication
HTTPS  = Protected web communication
```

### TCP — Reliable Delivery

**TCP (Transmission Control Protocol)** helps deliver data reliably and in the correct order.

Imagine that a large response must be divided into several numbered packages. TCP checks that the packages arrive, puts them back in order, and retransmits missing packages when necessary.

Traditional HTTP and HTTPS communication commonly uses TCP underneath. You do not need to control TCP yourself—the operating system and networking software handle it for you.

## How the Pieces Fit Together

Think of sending a protected village message:

| Networking Term | Simple Role | Village Analogy |
|---|---|---|
| Request | Asks for something | Hunter asks for a spear |
| Response | Returns an answer | Hunter receives the spear |
| HTTP | Rules for the message | Agreed message format |
| HTTPS | Protects the message | Message inside a locked box |
| TCP | Delivers all parts reliably | Messenger checks every package arrives |

For a typical HTTPS website, the simplified journey is:

```text
Browser creates an HTTP request
              ↓
HTTPS protects the request
              ↓
TCP helps deliver it reliably
              ↓
Server processes it and sends a response
```

The important idea is not to memorize every protocol yet. Remember the journey:

```text
Client asks  →  Server processes  →  Server responds
```

## Simple Definition

The **client–server model** is a way for computers to communicate in which a client sends a request and a server returns a response across a network.

**The client asks. The server answers. Protocols help the messages travel correctly and safely.**
