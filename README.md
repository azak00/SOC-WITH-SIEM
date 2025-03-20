# Introduction
This project demonstrates how to set up a Security Operations Center (SOC) lab using Azure Sentinel (Microsoft Sentinel) to monitor and analyze security threats. It includes log collection, threat detection, and incident response workflows.

## Architecture & Components

### Lab Overview

This SOC lab is built using Azure Sentinel, Log Analytics Workspace, and connected data sources. The architecture includes:

- Azure Sentinel – SIEM for log analysis and threat detection.

- Log Analytics Workspace – Central repository for logs.

- Data Sources – Windows Event Logs, Sysmon, security logs, and custom log exporters.

- Threat Detection & Response – Custom KQL queries and alerting mechanisms.

#

<img src="https://github.com/azak00/SOC-WITH-SIEM/assets/26345001/43742caa-cffe-4972-aa2f-855d5074e2ca" alt="MINI-SOC-SIEM-ARCHI" style="height: 450px; width:850;"/> 

## Step-by-Step Setup

1. **Deploy Azure Sentinel**
   - Create an **Azure Log Analytics Workspace**.
   - Navigate to **Microsoft Sentinel** in Azure and connect it to the workspace.

2. **Onboard Log Sources**
   - Enable **Windows Event Logs & Sysmon**.
   - Configure **custom log exporters** (`Debian-based_Log_Exporter.py`, `Windows_Log_Exporter.py`).

3. **Configure Threat Detections**
   - Create **custom analytics rules** using KQL queries.
   - Set up **alert policies** to notify on suspicious activity.

## Sample KQL Queries
- Failed Login Attempts
- Detecting Brute Force Attacks

## Dashboards & Alerts
<img width="800" alt="Failed-RDP2" src="https://github.com/user-attachments/assets/110254d3-b9d1-44ae-a753-9761c6228dc9" />

## Challenges & Lessons Learned

- What worked well – Log collection, KQL queries.

- Challenges faced – Log delays, rule fine-tuning.

- Ongoing improvements – Automating incident response, integrating external threat intelligence.





<!--
![Mini-Soc with SIEM](https://github.com/azak00/SOC-WITH-SIEM/assets/26345001/43742caa-cffe-4972-aa2f-855d5074e2ca)

## 

### Environment/Tools/Service Used

- Azure Virtual Machines
- Data Connection Endpoint: Connection bridge to receive collected logs and send to log analytics workspace. 
- Azure Log Analytics Workspaces
- Data Connection Rule: Defines where data is collected and transformed and where to send it.
- Azure Sentinel: Azure SIEM to analyse and visualize logs on a global attack map. 




