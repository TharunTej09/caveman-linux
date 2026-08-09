# Lab 02 — Host a Web Server

## 🎯 Mission

Turn the VM into a server that accepts an HTTP request and returns your own page.

## Prerequisites

- Lab 01 VM with network access
- A user with `sudo` permission

## ⚠️ Safety

Use NAT or a trusted private lab network. Do not expose this learning server to the public internet.

## Starting State

Log in to the VM. Record its address with `ip -brief address`.

## Tasks

1. Install Nginx:

   ```bash
   sudo apt update
   sudo apt install nginx
   ```

2. Confirm that the service is running and listening:

   ```bash
   systemctl status nginx
   ss -ltnp
   ```

3. Create a course page without replacing the packaged default file:

   ```bash
   echo '<h1>Chief Grog Web Server</h1><p>The village is online.</p>' | sudo tee /var/www/html/caveman.html
   ```

4. Request it locally:

   ```bash
   curl -i http://localhost/caveman.html
   ```

5. From the host, open `http://VM_IP/caveman.html`. If NAT prevents host-to-guest access, configure a hypervisor port-forward from host port `8080` to guest port `80`, then open `http://localhost:8080/caveman.html`.
6. Inspect recent service records:

   ```bash
   sudo journalctl -u nginx --since "10 minutes ago"
   sudo tail /var/log/nginx/access.log
   ```

## ✅ Verification

- `systemctl is-active nginx` prints `active`.
- `ss -ltnp` shows a listener on TCP port 80.
- `curl` returns an HTTP success status and your page content.
- The access log contains the request.

## Troubleshooting Clues

- **Connection refused:** verify service state and port 80 listener first.
- **Local request works but host request fails:** check VM network mode, port forwarding, and guest firewall.
- **404 response:** confirm the requested filename and `/var/www/html/caveman.html` match.
- **Configuration error:** run `sudo nginx -t` before restarting.

## Cleanup

```bash
sudo rm /var/www/html/caveman.html
sudo apt remove nginx
```

Keep Nginx installed if you want to reuse it in later server-operations lessons.

## 🧠 Think Like an Engineer

Trace one browser request through client, IP address, TCP port, Nginx process, file, response, and access log. At which points could it fail?
