---
title: "Anycast as a Load Balancing feature"
labels: "loadbalancer, backend, latency"
year: 2010
---

# Anycast as a Load Balancing feature

**Author(s):** Fernanda Weiden and Peter Frost

**Paper URL:** https://dl.acm.org/doi/10.5555/1924976.1925002

**Pages:** 4

**Summary:** This research paper explores the use of Anycast as a feature for load balancing in distributed systems. Anycast enables the delivery of user requests to the nearest or best-performing service instance by leveraging routing protocols. This approach automatically redirects traffic during server or location failures. The paper highlights its advantages over traditional DNS-based load balancing, including faster failover and seamless recovery, making it an efficient solution for modern, globally distributed networks.

## Sections Summary

### `Introduction`
- Traditional load balancing (LB) architectures typically involve deploying multiple replicas of a service and using a LB to distribute user traffic among them.
- The traditional setup improves scalability and availability but can't handle backend service instance failures.
- Enhanced LB design address this by incorporating failover mechanisms that automatically redirect user requests to the nearest secondary location when a primary backend fails. However, if the LBs themselves fail, users lose access to alternate service instances entirely.
- Ensuring uninterrupted user access is a critical design priority.
- One common solution is to update DNS records to redirect traffic to other service locations. While technically feasible, DNS-based failover introduces challenges such as TTL propagation delays, increased downtime, and the operational burden of reverting records once the original location recovers.
- A more seamless and efficient approach is to embed monitoring and failover capabilities directly into the LB infrastructure.
  
### `Basics of Anycast`
- Anycast is a routing technique where multiple hosts share the same IP address and user traffic is routed to the nearest available host based on network topology.
- Useful when all hosts provide identical services, ensuring users connect to the closest service instance.
- Anycast lacks awareness of service health because BGP/Anycast alone doesn’t know whether the service behind the advertised IP is actually healthy, which can result in traffic being routed to unhealthy instances. It only routes traffic based on network topology (i.e., shortest path). If a server becomes unhealthy but still advertises the IP via BGP, users will still be sent there — hence the risk.

### `Our implementation`
- Employs BGP to build a route advertisement hierarchy which eliminates the need for proxy-based failover, preserving client identity and reducing overhead.
- LB is provided as a shared infrastructure usable by multiple services without adding network complexity.
- LBs perform service-specific health checks which enables support for both UDP and TCP services. This refers to the application-level health management added on top of Anycast in their implementation: they use load balancers that run health checks (e.g., using ldirectord). When all local backends fail, the load balancer withdraws the Anycast IP via BGP — i.e., it stops advertising the route. As a result, Anycast automatically reroutes users to the next nearest healthy location.
- A dedicated subnet for Anycast VIPs is configured.
- Routers accept /32 advertisements only from Load Balancers, with ACL protections to prevent route hijacking.
- Anycast VIPs can coexist with traditional VIPs on the same infrastructure.

### `Software used for this implementation`
- Load Balancers are deployed in HA pairs to ensure resilience against single-machine failures.

Heartbeat (from the Linux-HA project) is used as the cluster resource manager, responsible for managing network interfaces and backend software as heartbeat resources.
ldirectord is used for:

Performing health checks on backend servers.
Adding/removing backends from the load balancing pool based on health.
Fallback routing: If all backends fail, it redirects traffic to a secondary location.

Custom Feature:

A fallback command was added to ldirectord to dynamically bring Anycast IPs up or down based on backend health status.
ip_vs (Linux Kernel Load Balancing module) is used to implement Direct Routing (DR) for all VIPs.

ldirectord interfaces with:

    ifconfig to manage IPs.

    ipvsadm to control ip_vs and manage backend pools.

Quagga (a routing software suite) is used to implement BGP on the Load Balancers.

Quagga allows Load Balancers to:

    Advertise BGP routes for services to network routers.

    Automatically withdraw routes when backends fail, ensuring no traffic is sent to unavailable services.

Each service is assigned an IP (VIP).

LVS configuration brings VIPs up.

If all associated backends fail:

    ldirectord brings down the VIP's Anycast IP.

    Quagga withdraws the route, preventing users from being routed to that failed instance.

### `Adding new services to the setup`
- Simple Integration:

    New services can be added by configuring their backends as VIPs on an Anycast-enabled Load Balancer.

    Only requires updates to Heartbeat and ldirectord configurations.

No Additional Network Configuration:

    The Anycast network setup is already in place, reducing complexity and speeding up deployment.

Scaling to New Locations:

    Adding a service in a new location follows the same configuration process.

    Anycast ensures users are automatically routed to the nearest Load Balancer.

### `Failure modes and recovery times`
- Recovery Time Considerations:

    Times are based on this specific Anycast setup; results may vary with different configurations.

Route Propagation Delay:

    Less than 1 second for BGP route updates to propagate.

Router Dead Timer:

    Set to 30 seconds for detecting unresponsive BGP peers.

Service Failures:

    If all backends fail, recovery time = health check interval + <1 second for BGP updates.

Total Failures (e.g., power/network loss):

    Recovery time = 30-second dead timer + <1 second propagation.

## Questions/Discussion Points

- Network topology means that routing decisions are made based on the structure of the network. "Nearest" doesn't necessary mean geographically closets but topologically closets so the host can be reached with the fewest number of network hops, lowest latency or fastest route throuogh the network infrastructure.
- 
