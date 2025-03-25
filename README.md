# Introduction
This project demonstrates how to set up a Security Operations Center (SOC) lab using Azure Sentinel (Microsoft Sentinel) to monitor and analyze security threats. It includes log collection, threat detection, and incident response workflows.

## Architecture & Components

### Lab Overview

This SOC setup is built using Azure Sentinel, Log Analytics Workspace, and connected data sources. The architecture includes:

- Azure Sentinel – SIEM for log analysis and threat detection, and visualize logs on a global attack map.
- Data Sources – Windows Event Logs, security logs, and custom log exporters.
- Data Connection Rule: Defines where data is collected and transformed and where to send it.
- Data Connection Endpoint: Connection bridge to receive collected logs and send to log analytics workspace. 
- Log Analytics Workspace – Central repository for custom logs.

#

<img src="https://github.com/azak00/SOC-WITH-SIEM/assets/26345001/43742caa-cffe-4972-aa2f-855d5074e2ca" alt="MINI-SOC-SIEM-ARCHI" style="height: 450px; width:850;"/> 

## Step-by-Step Setup

1. **Deploy Azure Sentinel**
   - Create an **Azure Log Analytics Workspace**.
   - Navigate to **Microsoft Sentinel** in Azure and connect it to the workspace.

2. **Attach Log Sources**
   - Enable **Windows Event Logs**.
   - Configure **custom log exporters** (`Windows_Log_Exporter.py`).
   - Attach custom logs to the **analytics workspace**

3. **Configure Threat Detections**
   - Create **custom analytics rules** using KQL queries. [Sample_KQL Query](https://github.com/azak00/SOC-WITH-SIEM/blob/main/Debian-based_KQL%20Query)

## Dashboards & Alerts
<img width="800" alt="Failed-RDP2" src="https://github.com/user-attachments/assets/110254d3-b9d1-44ae-a753-9761c6228dc9" />

## Challenges & Lessons Learned

- What worked smoothly: Log collection, KQL queries.

- Challenges experienced: Log delays, rule fine-tuning.

- Ongoing improvements – Automating incident response, integrating external threat intelligence.





<!--
![Mini-Soc with SIEM](https://github.com/azak00/SOC-WITH-SIEM/assets/26345001/43742caa-cffe-4972-aa2f-855d5074e2ca)

## 



- ### Environment/Tools/Service Used

- Azure Virtual Machines
- Data Connection Rule: Defines where data is collected and transformed and where to send it.
- Data Connection Endpoint: Connection bridge to receive collected logs and send to log analytics workspace. 
- Azure Log Analytics Workspaces
- Azure Sentinel: Azure SIEM to analyse and visualize logs on a global attack map. 


