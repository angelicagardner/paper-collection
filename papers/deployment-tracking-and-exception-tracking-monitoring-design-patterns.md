---
title: "Deployment Tracking and Exception Tracking: monitoring design patterns for cloud-native applications"
labels: "monitoring, design patterns, devops, observability, cloud native"
year: 2024
---

# Deployment Tracking and Exception Tracking: monitoring design patterns for cloud-native applications

**Author(s):** Carlos Albuquerque and Filipe F. Correia

**Paper URL:** https://dl.acm.org/doi/10.1145/3628034.3628038

**Pages:** 10

**Summary:** This paper introduces **Deployment Tracking** and **Exception Tracking** as two design patterns to improve the observability of cloud-native architectures. It is following a previously published paper about design patterns for CN, distributed systems. These patterns help development teams quickly isolate the root causes of anomalies and reduce the mean time to resolution (MTTR).

## Sections Summary

### `1. Introduction`

- The paper distinguishes between Observability and Monitoring using Newman’s definitions:
    - Observability: A system characteristic, the ability to understand internal states via external outputs.
    - Monitoring: A human activity, the act of keeping track of the system's health and performance.

- Observability is cited as the 4th most common DevOps practice.

- Transitioning from on-premises monoliths to cloud-native systems has changed how monitoring must be handled. There is a need for better ways to communicate and reuse modern monitoring practices across teams.

- The authors propose documenting monitoring practices as design patterns to facilitate easier communication and more thoughtful implementation.

- The paper refines previous work on monitoring patterns and introduces two new descriptions specifically focused on tracking system events.
  
### `2. Related Work`

- Existing documentation (like Richardson’s microservices patterns) often lacks formal structure or sufficient detail, making it difficult for practitioners to distinguish between context, forces, and consequences.

- Log deployment is the 4th most common monitoring practice, particularly among experienced developers. The authors aim to formalize related "grey literature" examples, such as Etsy’s release tracking, into a rigorous design pattern.

- Exception tracking is the 2nd most common monitoring practice, and it requires a specialized approach which is distinct from standard logging, to handle de-duplication and alerting. The paper formalizes this idea to make it accessible for less experienced engineers.

### `3. About the Patterns`

- The authors identify 11 practices categorized by their functional purpose:
    1. Audit Logging: Recording user actions and system changes for compliance and security.
    2. Structured Logging: Using a consistent format across all services to ensure logs are machine-readable and universally understood.
    3. Log Sampling: Prioritizing and filtering logs to manage storage costs while retaining essential troubleshooting data.
    4. Distributed Tracing: Assigning unique IDs to external requests to visualize their flow across micrcoservices.
    5. Deployment Tracking (Featured in this paper): Logging every production change to correlate system anomalies with specific deployments.
    6. Exception Tracking (Featured in this paper): Using a dedicated service to aggregate, alert, and manage the resolution of code exceptions.
    7. Liveness Probes: Implementing endpoints to check if a service is running.
    8. Readiness Probes: Implementing endpoints to check if a service is ready to accept traffic.
    9. Synthetic Testing: Running a subset of tests against the production environment to catch issues before users do.
    10. Application Metrics: Gathering business-level performance data into centralized dashboards for real-time insights.
    11. Infrastructure Metrics: Gathering hardware-level performance data into centralized dashboards for real-time insights.

- The paper focuses on Deployment Tracking and Exception Tracking for two reasons:
    - They provide the event data needed to troubleshoot and find the root cause of system failures.
    - The data captured by these patterns often serves as the foundation for broader application and infrastructure metrics.

### `4. Deployment Tracking`

- This section details the Deployment Tracking design pattern, which addresses the gap between identifying a system failure and finding its root cause.

- The Problem: Metrics show what is failing (effects), but not why (causes). When anomalies occur, teams often struggle to determine if a recent change triggered the issue.

- The Solution: Every production change, code releases, environment variable updates, or infrastructure scaling must be recorded as a Deployment Record and overlaid directly onto system metric dashboards.

- Benefits of this pattern:
    - Faster troubleshooting
    - Increased team confidence in the deployments
    - Allows business insights

- Drawbacks of this pattern:
    - Only effective if the team already has metric collection and visualization system.
    - Not all monitoring tools support drawing vertical markers or binary metrics over time-series graphs.

- *Canary Releases* and *Infrastructure/App Metrics* are related patterns that should ideally be implemented before Deployment Tracking to provide the baseline data needed for correlation.

### `5. Exception Tracking`

- This section details the Exception Tracking design pattern, which formalizes how to handle unexpected system behaviors that standard logging often obscures.

- The Problem: Standard log files are poor at handling exceptions because stack traces are multi-line with big files, making it difficult to de-duplicate recurring errors or track their resolution.

- The Solution: Developers should use an Exception Tracking Library to forward uncaught exceptions to a centralized service. This service automatically aggregates similar errors, attaches context like stack traces and user actions, and manages the lifecycle of the fix.

- Benefits of this pattern:
    - Reduces MTTR (Mean Time to Repair)
    - Cross-platform visibility
    - Proactive fixing

- Drawbacks of this pattern:
    - Requires instrumenting the source code with external SDKs.
    - Third-party SaaS tools or self-hosting a tracking server introduces new operational expenses.

## Questions/Discussion Points

- This paper was published in 2024, what happened later? More papers/patterns? 

## Links/Resources

- Previous work referenced that this paper builds on/continues:

> Carlos Albuquerque. 2022. *Monitoring Design Patterns For Cloud Applications.* Master’s thesis. Faculty of Engineering, University of Porto. https://repositorio-aberto.up.pt/handle/10216/143462

> Carlos Albuquerque, Kadu Relvas Barral, Filipe F Correia, and Kyle Brown. 2022. Proactive monitoring design patterns for cloud applications. In *Proceedings of the 25th European Conference on Pattern Languages of Programs*. ACM, Irsee, Germany, 21.
