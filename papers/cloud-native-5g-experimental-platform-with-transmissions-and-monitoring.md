---
title: "Cloud-native 5G experimental platform with over-the-air transmissions and end-to-end monitoring"
labels: "5g, cloud native, monitoring"
year: 2022
---

# Cloud-native 5G experimental platform with over-the-air transmissions and end-to-end monitoring

**Author(s):** Sergio Barrachina-Muñoz, Miquel Payaró, and Josep Mangues-Bafalluy

**Paper URL:** https://arxiv.org/pdf/2207.11936

**Pages:** 6

**Summary:** This article introduces a framework that enhances LCM of 5G networks through CN deployments and E2E monitoring. The framework demonstrates containerized network functions, like Open5GS, in a Kubernetes cluster with multi-access edge computing (MEC). It also implements a Prometheus-based monitoring system visualized via Grafana dashboards, showcasing use cases in user plane function re-selection and user mobility management.

## Sections Summary

### `I. Introduction`
- 5G networks aim to address the needs of a fully connected society by enabling services and applications on a unified infrastructure.
- 5G transitions from centralized architectures to edge computing with multiple points-of-presence (PoPs)
- Low-latency, high-bandwidth applications benefit from edge computing, e.g. VR/AR.
- The MARSAL vision for 5G and B5G is focused on advancing capabilities of telecommunications networks. Its key enablers are (1) CN deployments that allow dynamic resource sharing, faster time-to-market and automation, and (2) end-to-end monitoring to manage the complex infrastructures (compute, storage, network, RAN).
- Monitoring in essential in Multi-Tenant Networks for maintaining KPIs across domains, enabling network operators and slice owners to validate SLAs and optimize operations.
- Existing research focuses on CN deployments or monitoring separately.
- This paper contribution is to present a unified experimental platform combining CN 5g core deployment and end-to-end monitoring.
  
### `II. Related Work`
- Studies focus either on cloud-native 5G deployments or end-to-end monitoring systems, but not both together.
- As for CN deployment studies, the studies often rely on partial implementation and lack comprehensive monitoring.
- As for system monitoring studies, they often exclude RAN metrics or lack containerized 5g core deployment.
- This paper proposes a framework that integrates both aspects, using containerized network functions (CNFs) orchestrated by Kubernetes. The paper also demonstrates the system through practical scenarios like UPF re-selection and user mobility.

### `III. Cloud-Native 5G Experimental Platform`
- Overview:
    - This section details the architecture, deployment strategies, and experimental setups of the 5G platform and its testing environment.
- Components:
    - NG-RAN (New Radio Access Network): Manages the new radio (NR) interface essential for 5G wireless communication.
    - 5G Core Network (5GC): Employs a Service-Based Architecture (SBA) featuring modular Network Functions (NFs) and Service-Based Interfaces (SBIs) that utilize RESTful APIs for communication.
- Containerized Network Functions (CNFs) offer advantages over PNFs (Physical NFs) and VNFs (Virtual NFs), such as greater scalability, energy efficiency, and suitability for edge applications. Containers, managed by orchestrators like Kubernetes, ensure lightweight and consistent deployments.
- Deployment Details for 5GC NFs and Monitoring systems:
    - Deployed within a Kubernetes cluster.
    - Utilized Helm charts for streamlined installation.
    - Employed Calico as the Container Network Interface (CNI) plugin to manage networking.
    - Managed container lifecycle tasks (creation, deletion, scaling) in line with Network Function Virtualization (NFV) standards.
- Experimental RAN Integration:
    - Amarisoft’s AMARI Callbox Ultimate serves as a physical 5G gNodeB (gNB) facilitating real over-the-air transmissions. Configured to connect with the Access and Mobility Management Function (AMF) via its IP address exposed through Kubernetes services, ensuring stable connectivity.
- MEC-Enabled Testbed configuration and components:
    - User Equipment (UE) Emulators: Two emulators targeting different service types, including best-effort and time-critical services like Augmented Reality (AR) and Virtual Reality (VR).
    - Amarisoft Callbox: Acts as the standalone 5G gNB.
    - Edge Node: Hosts MEC-enabled User Plane Function (UPF) and an iperf server for network performance testing.
    - Core Node: Runs Open5GS CNFs, managing core network functions.
    - Monitoring Node: Provides end-to-end system monitoring capabilities.
    - Networking: Simplified to Ethernet links within a Local Area Network (LAN) for testing purposes.
- Monitoring Setup:
    - Deployed using Kubeprometheus for comprehensive monitoring.
    - Collected custom metrics by sampling the Amarisoft Callbox API.
    - Monitoring CNFs are treated as Application Functions (AFs) within the 5G SBA framework, allowing for integrated monitoring and management.

### `IV. End-to-End Monitoring: From Core to RAN`
- Specific CNFs were deployed for monitoring purposes, and the deployed CNFs pull metrics both from the core and the RAN domains. The data is gathered into a centralized database where metrics are then plotted in dashboards.
- Kube-prometheus is used for infrastructure monitoring, to monitor the usage of infrastructure resources, such as compute, storage, and network.
- Custom sampling function for RAN: For our monitoring purposes, the Amarisoft Callbox can be accessed through a remote API using the WebSocket protocol, which establishes a persistent connection between the client (Amarisoft sampling CNF in monitoring node) and the server (Amarisoft Callbox itself). This API exposes different metrics at gNB/radio level, including (per user and cell id) uplink and downlink bitrate, modulation coding scheme (MCS), channel quality indicator (CQI), or signal-to-noise-ratio (SNR). The custom sampling function we developed, available at the referred repository, is a containerized Python script that opens a WebSocket against the Callbox API and exposes some metrics of interest to the Prometheus scraper.
- Visualizing metrics with Grafana.

### `V. Use Case Evaluation`
- Experiment #1 conducted: Focuses on User Plane Function (UPF) re-selection in MEC-enabled 5G networks.
    - The objective was to assess the monitoring framework's ability to track resource usage during dynamic UPF re-selection in a MEC-enabled 5G testbed.
    - UE1 starts a 100 Mbps UDP downlink connection to a core node iperf server.
    - UE2 initiates a similar connection to the core node.
- Experiment #2 conducted: Concentrates on RAN (gNB) metrics under UE mobility.
    - The objective was to validate the custom Amarisoft sampling function by analyzing RAN-specific metrics during UE movement.
    - UE1 initiates a 120 Mbps uplink iperf connection to the core node. The receiver gain at the gNB is sequentially reduced by 4 dB via the Amarisoft API to simulate UE1 moving away.

### `VI. Conclusions`
- This paper demonstrated a cloud-native 5G framework with containerized, end-to-end monitoring.
- They demonstrated the framework’s capabilities using Grafana dashboards by collecting and visualizing metrics from both infrastructure and RAN domains.

## Questions/Discussion Points

- Example to understand the concept of multi-tenant environments (e.g. those enabled by 5g network slicing):
    - Tenant A operates a streaming service and requires low-latency, high-bandwidth connectivity.
    - Tenant B runs IoT applications, requiring high reliability but lower bandwidth.
    - Monitoring tools measure KPIs like latency, jitter, and reliability for each tenant's slice and provide feedback to the network operator. If Tenant A's slice experiences congestion, monitoring systems can trigger an optimization process to allocate more resources or reroute traffic.
