---
title: "Next Decade of Telecommunications Artificial Intelligence"
labels: "5g, ai, telecom"
year: 2021
---

# Next Decade of Telecommunications Artificial Intelligence

**Author(s):** Ye Ouyang, Lilei Wang, Aidong Yang, Tongqing Gao, Leping Wei, Yaqin Zhang

**Paper URL:** https://www.sciopen.com/article/10.26599/AIR.2022.9150003

**Pages:** 23

**Summary:** This paper contains a comprehensive review and foward-looking perspective on the integration of mobile communication and AI from 5G and beyond 5G (B5G). 

## Sections Summary

- `1. Mobile Communication and AI`
  - Mobile communication has gone through a significant evolution from analog to digital, from voice-only to voice and data, and from circuit switching to IP-based systems.
  - When 4G was established, the industry started to emphasize automation and intelligence to handle increasingly complex communication networks and personalized services.
  - We are now generating vast amounts of data which facilitates the application of AI in the communication field.
  
- `2. Development Roadmap of Mobile Communication and AI`
  - Mobile industry evolved through 3GPP standards from 2G to 5G, with AI concepts introduced around 2008 via self-organizing networks (SON).
  - Telecom AI evolution: Initially limited, AI in telecom grew rapidly post-2017 with 3GPP research on 5G features, network optimization, and data analytics.
  - Organizations like 3GPP, ETSI, O-RAN, and ITU developed AI frameworks and standardization for mobile networks and federated learning integration into 5G.
 
- `3. Development of Telecommunications AI`
  - In traditional communication systems, mathematical models are often used to describe how signals are transmitted, processed, and received, such as with modulation, noise filtering, or error correction. Deep Learning (DL) allows for optimization without needing these explicit models. Instead, it learns patterns and solutions from large amounts of data, making decisions without having a formal mathematical representation of the problem. 
  - Communication systems are structured hierarchically, like microservices in IT, optimizing subsystems independently. AI (especially DL) could optimize systems holistically rather than in parts.
  - AI in Network Infrastructure improves the physical and functional components that make up telecom networks, such as base stations, routers, and terminals. This is illustrated from 4 aspects:
      - Wireless Access Network: AI-techniques such as DNN and CNN is applied at multiple layers (physical, MAC, network) to optimize channel quality, signal detection, coding, signal processing, resource management, etc. Self-Organizing Networks (SON) aim for self-configuration and optimization, but faces commercialization struggles due to vendor-specific implementations.
      - Core Network: NWDAF (Network Data Analytics Function) - an AI component in the core network - was standardized by 3GPP in 2017 to integrate AI into the 5G core network for managing mobility, QoS, and network elements - operators are testing this in 5G standalone (SA) networks. O-RAN developed the RIC (RAN Intelligent Controller) for AI-driven radio access network management but it is still in early trials.
      - Transport Network: The backbone of communication, AI helps monitor, optimize, and guarantee network service quality but it's still in early stages of research.
      - Terminal: Terminals can report performance data to optimize networks using AI in SON and OSS systems, but most AI-focus on integrating intelligence within terminals and chips.
  - AI in Network Management enhances the management and operation of telecom networks. It addresses how networks are maintained, optimized, and secured from a management perspective. This is structured around three main components:
      - MDAF: analyze network data for configuration and optimisation of performance to support QoS. Defined by 3GPP standards.
      - ENI Engine: network adapts over time based on performance data and feedback to help with network management and overall network reliability. Established by ETSI.
      - Network OSS: manage and automate various network operations, maintenance, resource optimization and efficient handling of faults based on predictive analytics.
  - AI development in cross-domain integration intelligence has led to a variety of other use cases in telecom business, e.g. customer experience/sales/service, billing, network policy control and private networks.
 
- `4. Next Decade of Telecommunications AI`
  - Forward-looking of AI in telecom network infrastructure, from the 4 aspects:
      - Wireless Access Network: 3GPP SA5 and RAN3 focus on studying SON (Self-Organizing Networks) for 5G, data collection and utilization for LTE and NR, making SON an independent logical entity within RAN, and RAN-DAF (Radio Access Network Data Analytics Function) to perform data analysis and decision-making on the radio side.
      - Core Network: NWDAF can communicate with other core network functions such as NF (Network Function), AF (Application Function), and OAM (Operations, Administration, and Maintenance) to collect and analyze data in real time, support decision-making in the control plane, optimize network slice selection and load balancing, support user-driven analytics where UE (user equipment) data such as location and profile information informs network slicing decisions, and integrate with multi-access edge computing (MEC) to empower applications in vertical industries like manufacturing and healthcare. 3GPP SA5 explores how NWDAF can extend analysis functions to OAM and RAN.
      - Transport Network: Edge computing and cloud resources evolve into fully distributed architecture, new business model with blockchain (elastic computing combined with smart contacts) for security, and transitioning from IPv6 to IPv6+ for business-specific demands.
      - Terminal: AI at terminals predicts seamless network switching for uninterrupted connection, improve wireless access via chip-based AI, and AI-driven intelligent beamforming using deep reinforcement learning for better network speed and robustness.
  - Forward-looking of AI in telecom network management from the aspects:
      - MDAF: The SA5 working group in 3GPP will continue enhancing MDAF to strengthen intelligent operations for network management. MDAF will have better integration with network functions like NWDAF for cohesive approach.
      - ETSI ENI: The ENI working group is expected to define interfaces that enable practical deployment and application of ENI => integrating data processing within ENI architecture, deployment strategies for ENI in operator systems, flow information telemetry, etc.
      - IBN (intent-based network): IBN reduces complexity and the need for in-depth device knowledge, streamlining network management, especially in multi-vendor settings. China Telecom is actively researching IBN implementation.
      - Operator's O&M system defined by ISO: Differ from traditional 4G and 5G signaling by being a command structure for AI interactions between network elements, OAM modules, and OSS systems, connecting northbound and southbound interfaces with the AI middle-office. Standard interfaces link the AI middle-office to various systems, such as 3GPP SON, NWDAF, O-RAN RIC, ETSI ENI, and 5G OSS, for tasks like network orchestration and performance monitoring.
  - AI will support in BSS intelligence and management finance through customized customer experience, establish effective operations and rapid innovation towards new services/models/tech (business vs operations model).
  - For cross-domain intelligence in networks & business it's expected that customer experience perception system will evolve from SLA (Service Level Agreement) to ELA.
  - For private network applications one of the core values of 5G is proprietary apps for enterprise ToB, forward-looking to fully intelligent vehicles, telemedicine and smart cities.

- `5. Expectable Future: Comprehensive Promotion of Telecommunication Intelligentization in the Next Decade`
  - 6G will integrate air, sea and land systems, using AI to solve complex optimization challenges across diverse ecosystems.
  - ITU-R’s formal 6G standard anticipated around 2027-2028.
  - SON and O-RAN RIC systems evolving for AI-enhanced wireless optimization.
  - Federated learning, blockchain, and privacy computing will protect data and privacy.
  - Early commercial 5G private networks will use AI for SLA guarantees and resource optimization, with hybrid and standalone private networks focusing on QoS and real-time service monitoring in later stages.
  - Combining digital twin technology, network simulation, and AI will enable advanced network LCM.

### Questions/Discussion Points

- AI and 5G are considered General Purpose Technologies (GPTs). GPTs are foundational technologies that have broad applications and potential for significant impact on the economy and society, characterized by their ability to spur innovaction, drive productivity and transform multiple industries.
- This whitepaper was written in 2021, it's now 2024 Q4 - how far did we come with the progress now..?
