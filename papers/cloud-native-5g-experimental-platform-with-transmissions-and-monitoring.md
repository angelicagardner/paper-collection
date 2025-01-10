---
title: "Cloud-native 5G experimental platform with over-the-air transmissions and end-to-end monitoring"
labels: "5g, cloud native, monitoring"
year: 2022
---

# Cloud-native 5G experimental platform with over-the-air transmissions and end-to-end monitoring

**Author(s):** Sergio Barrachina-Muñoz, Miquel Payaró, and Josep Mangues-Bafalluy

**Paper URL:** https://arxiv.org/pdf/2207.11936

**Pages:** 6

**Summary:** This article presents a framework that improves the LCM of 5G networks through cloud-native (CN) deployments and end-to-end (E2E) monitoring. The framework demonstrates containerized network functions, such as Open5GS, deployed within a Kubernetes cluster integrated with multi-access edge computing (MEC). Additionally, it incorporates a Prometheus-based monitoring system visualized through Grafana dashboards, demonstrating practical use cases like user plane function re-selection and user mobility management.

## Sections Summary

### `I. Introduction`
- 5G networks aim to address the needs of a fully connected society with unified infrastructure for diverse services and applications.
- To achieve this an architecture shift is needed: to move from centralized to edge computing with multiple points-of-presence (PoPs)
- Edge computing is beneficial for low-latency, high-bandwidth applications, e.g. VR/AR.
- The MARSAL vision for 5G and beyond-5g (B5G) is focused on advancing telecom networks through:
    - 1) CN deployments that enables dynamic resource sharing, faster time-to-market and automation
    - 2) E2E monitoring that manages complex infrastructures (compute, storage, network, RAN).
- Monitoring is essential in Multi-Tenant Networks for maintaining KPIs across domains, enabling network operators and slice owners to validate SLAs and optimize operations.
- Current research gap:
    - Existing research focuses on CN deployments or monitoring separately
- Paper contribution:
    - Presents a unified experimental platform combining CN 5g core deployment and E2E monitoring.
  
### `II. Related Work`
- Existing studies focus on either:
    - Cloud-native 5G deployments with partial implementations without compresensive monitoring
    - End-to-end system monitoring, typically excluding RAN metrics or lack containerized 5G core deployments.
- This paper proposes a framework that integrates both aspects, using containerized network functions (CNFs) orchestrated by Kubernetes.

### `III. Cloud-Native 5G Experimental Platform`
- This section details the architecture, deployment strategies, and experimental setup.
- Components:
    - NG-RAN (New Radio Access Network): Manages the new radio interface for 5G wireless communication.
    - 5G Core Network (5GC): uses service-based architecture with modular network functions and RESTful APIs.
- Containerized Network Functions (CNFs) offer advantages over physical NFs and virtual NFs, such as greater scalability, energy efficiency, and suitability for edge applications. The containers are managed by orchestrators like k8s.
- Platform is deployed within a k8s cluster, utilizing Helm charts. Calico Container Network Interface (CNI) plugin manages networking within the cluster. The LCM operations (creation, deletion, sclaing) are managed per Network Function Virtualization (NFV) standards.
- For the RAN integration, Amarisoft’s AMARI Callbox Ultimate serves as a physical 5G gNodeB (gNB) for over-the-air transmissions. It connects with the Access and Mobility Management Function (AMF) via k8s-exposed IP.
- MEC-Enabled Testbed configuration and components:
    - Two User Equipment emulators to simulate different service types, including AR and VR.
    - The Amarisoft Callbox acts as the standalone 5G gNB.
    - Edge Node hosts MEC-enabled User Plane Function and an iperf server for network performance testing.
    - Core Node runs Open5GS CNFs to manage core network functions.
    - Monitoring Node provides E2E system monitoring.
    - Ethernet links are utilized within a LAN for testing.
- Monitoring Setup:
    - Deployed using Kubeprometheus for comprehensive monitoring.
    - Collected custom metrics from the Amarisoft Callbox API.
    - Monitoring CNFs are treated as application functions within the 5G service-based architecture framework, allowing for integrated monitoring.

### `IV. End-to-End Monitoring: From Core to RAN`
- The CNFs deployed for monitoring purposes pull metrics from both the core and the RAN domains.
- Kube-prometheus is used for infrastructure monitoring to get the usage of infrastructure resources, such as compute, storage, and network.
- For custom RAN sampling, a Python script using WebSocket connects to the Amarisoft Callbox. This API exposes metrics at gNB/radio level including (per user and cell id) uplink/downlink bitrate, modulation coding scheme, channel quality indicator and signal-to-noise-ratio.
- The data is gathered into a centralized database where metrics are plotted in dashboards in Grafana.

### `V. Use Case Evaluation`
- Experiment #1: User Plane Function (UPF) Re-selection
    - Objective was to assess the monitoring system's ability to track resource usage during dynamic UPF re-selection in a MEC-enabled 5G testbed.
    - Procedure:
        - UE1: Starts a 100 Mbps UDP downlink connection to a core node iperf server.
        - UE2: Initiates a similar connection to the core nod
- Experiment #2: RAN Metrics under User Equipment (UE) mobility.
    - Objective was to validate the custom Amarisoft sampling function by analyzing RAN-specific metrics during UE movement.
    - Procedure:
        - UE1: Starts a 120 Mbps uplink iperf connection to the core node.
        - Receiver gain at the gNB is reduced by 4 dB via the Amarisoft API to simulate UE1 moving away.

## Questions/Discussion Points

- Example to understand the concept of multi-tenant environments (e.g. those enabled by 5g network slicing):
    - Tenant A operates a streaming service and requires low-latency, high-bandwidth connectivity.
    - Tenant B runs IoT applications, requiring high reliability but lower bandwidth.
    - Monitoring tools measure KPIs like latency, jitter, and reliability for each tenant's slice and provide feedback to the network operator. If Tenant A's slice experiences congestion, monitoring systems can trigger an optimization process to allocate more resources or reroute traffic.
