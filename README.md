# NIST Incident Response Playbook & Tabletop Exercise

## 📝 Objective
This project demonstrates the ability to design, document, and test a formal Incident Response (IR) Playbook based on the NIST SP 800-61 Revision 2 framework. The goal was to establish a repeatable process for handling cyber threats and to validate that process by conducting a simulated tabletop exercise.

## 🛠️ Tools & Frameworks Used
*   **Framework:** NIST Cybersecurity Framework (CSF) / NIST SP 800-61 Rev. 2
*   **Documentation:** Microsoft Word / Google Docs (for Playbook creation)
*   **Automation:** Python (for Tabletop Exercise Inject generation)
*   **Skills Demonstrated:** IR Lifecycle, Tabletop Testing, Process Engineering, Policy Drafting

## 🗺️ The Incident Response Lifecycle (NIST)

### 1. Preparation
Developed a comprehensive Incident Response Playbook detailing roles, responsibilities, and communication protocols. The playbook establishes clear escalation paths for the Security Operations Center (SOC) when a threat is identified.

### 2. Detection & Analysis
Defined the criteria for classifying an event as a security incident. Outlined steps for gathering indicators of compromise (IOCs), analyzing log telemetry, and determining the scope of the impact.

### 3. Containment, Eradication & Recovery
Created specific action plans for different threat vectors (e.g., Ransomware, Phishing). 
*   **Containment:** Steps to isolate infected hosts from the network to prevent lateral movement.
*   **Eradication:** Procedures for removing malicious artifacts and patching vulnerabilities.
*   **Recovery:** Protocols for restoring systems from clean backups and monitoring for re-infection.

### 4. Post-Incident Activity (Lessons Learned)
Established a template for Post-Incident Reports to document what went right, what failed, and how to improve the playbook for future events.

## 🎲 Tabletop Exercise Simulation
To ensure the playbook was practical, I developed a **Python-based Tabletop Inject Generator** (`tabletop_inject_generator.py`). 

This script programmatically generates randomized security scenarios (e.g., a ransomware outbreak on an HR database). By running this script, an analyst can simulate an unexpected high-stress event and practice walking through the playbook phases to test their containment and eradication strategies, identifying any gaps in the documentation.

## 💡 Conclusion
Writing a policy is only the first step; testing it proves its value. This project highlights the importance of bridging governance with practical operations. By combining the NIST IR framework with automated tabletop testing, I ensured that the incident response plan is both compliant with industry standards and functionally effective in a simulated crisis.

---
*Note: The completed IR Playbook document (PDF) and the Python Inject Generator script are available in this repository.*
