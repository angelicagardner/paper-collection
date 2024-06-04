---
title: "Towards a Framework for Monitoring and Analyzing High Performance Computing Environments Using Kubernetes and Prometheus"
labels: "observability, prometheus, kubernetes, monitoring"
year: 2019
---

# Towards a Framework for Monitoring and Analyzing High Performance Computing Environments Using Kubernetes and Prometheus

**Author(s):** Nitin Sukhija; Elizabeth Bautista

**Paper URL:** https://ieeexplore.ieee.org/document/9060302

**Summary:** Computing environments for complex calculations and large data processing at high speeds are challenging to manage and monitor, leading to traditional alert methods being inefficient. This paper proposes a framework that integrates with modern platforms where the different components (OMNI, Kubernetes, Prometheus, Grafana) serves different purposes to create unified, dynamic and real-time capacities. This scalable infrastructure will be used for management, monitoring and alerting of heterogeneous computing systems at NERSC.

**Pages:** 6

## Sections Summary

- `1. Introduction`
  - An HPC (High-Performance Computing) environment is a computing system designed to perform complex calculations and process large amounts of data at high speeds.
  - Extreme-scale HPC environments require sophisticated automation and orchestration to manage diverse components like compute cores, memory, interconnects, power, and cooling systems.
  - Monitoring computational centers becomes increasingly challenging as they grow, leading to alert fatigue where true issues are obscured by numerous false alarms.
  - Traditional alert methods become less effective due to the high volume of alerts.
    
- `2. Background and Related Work`
  - For a monitoring solution to be efficient it needs to take into consideration scalability and HA, automation, dashboards, actionable insight analytics and capacity planning, distribution and customization.
  - Previous work (project examples) include Trinity Monitoring infrastructure and OpenLorenz.
  - The proposed monitoring framework in this paper integrates with modern platforms to provide a unified solution and aims to provide dynamic and real-time capacity, and it's specifically designed to handle the monitoring and management needs of extreme-scale systems. 
    
- `3. Design of HPC Monitoring and Analysis Framework`
  - *Figure 1. Overview design of the proposed framework.*
  - Data comes from heterogenenous and distributed sources in and out of the data center.
  - Examples of operational data include:
    - Time series data from the environment (e.g., temperature, power, humidity levels);
    - Monitoring data (e.g., network speeds, latency, packet loss, utilization or those that monitor the filesystem for disk write speeds, I/O); and
    - Event data (e.g., system logs, console logs, hardware failure events).
  - This diverse data should be kept on a single location and in the same format.
  - The Operations Monitoring and Notification Infrastructure (OMNI) is a big data collection infrastructure solution created for above purpose and backed by Elasticsearch. Data is getting into Elasticsearch via RabbitMQ (messaging broker). OMNI is able to ingest > 25,000 messages per second.
  - The time series data gathered and aggregated by Prometheus will be stored in OMNI and will be used to display dashboards.
    
- `4. Conclusion and Future Work`
  - In the proposed framework, each component has specific roles within the architecture, such as Prometheus pulling data, OMNI collecting data, Kubernetes managing the system via deployments of clusters and services, and Grafana real-time visualizing the data.
  - Future enhancements may include adding various data analysis methods like:
    - Clustering for grouping similar data;
    - Prescriptive analytics for decision-making; and
    - Statistical analysis to detect significant system changes and alert.
  - Different alert mechanisms could also be integrated to notify administrators of system problems in alternative ways.
