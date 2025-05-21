COLLEGE CODE: 1106

 COLLEGE NAME: IIET

 DEPARTMENT: BE [CSE]

 STUDENT NM-ID : 	E6E161D789C96179E4546E75D196CB4E
 ROLL NO: 110623104018

 DATE TECHNOLOGY-PROJECT NAME : AI-EBPL-STURCTURAL HEALTH MONITORING


SUBMITTED BY, : 
•	MEENAKSHI A N
TEAM MEMBERS: 
•	JANARTHANAN C
•	KAVYA M
•	YUVASHREE V 
•	KOWSALYA 

Phase 5: Project Demonstration & Documentation

  Title:  AI - Structural Health Monitoring

Abstract

The Structural Health Monitoring (SHM) System aims to enhance infrastructure safety through continuous monitoring of structural parameters using IoT sensors, data analytics, and AI-based predictive modeling. The final phase integrates real-time data collection from strategically placed sensors on infrastructures (e.g., bridges, buildings), automated fault detection algorithms, and performance visualization dashboards. This documentation details the completed project, including demonstration insights, architecture, source code, testing outcomes, and user manuals. Screenshots and schematic representations are also included to provide a complete picture of the system’s capabilities and deployment readiness.


1. Project Demonstration
Overview:
The SHM system will be demonstrated to show its ability to monitor and analyze structural integrity through real-time sensor data. The system is capable of detecting anomalies like cracks, stress, and vibrations.
Demonstration Details:
•	System Walkthrough: A live walkthrough from sensor data capture to real-time dashboard analytics.
•	AI Anomaly Detection: The AI model will analyze sensor inputs to detect potential structural issues.
•	IoT Sensor Display: Real-time readings (vibration, strain, tilt, temperature) from IoT sensors will be shown.
•	Performance Metrics: System load handling, latency, and reliability under different environmental conditions.
•	Data Security: Encryption and secure protocols for data integrity and remote access will be demonstrated.




Outcome:
Stakeholders will see a working system that can provide early warnings for structural issues, ensuring public safety and infrastructure longevity.

2. Project Documentation
Overview:
Detailed documentation of the SHM system, explaining technical design, implementation strategies, and operational guidelines.
Documentation Sections:
•	System Architecture: Diagrams of sensor placement, data flow, and backend architecture.
•	Code Documentation: Source code with comments, including AI analysis modules and sensor interface scripts.
•	User Guide: Instructions for facility managers on reading alerts and responding to notifications.
•	Admin Guide: System configuration, maintenance procedures, and sensor calibration protocols.
•	Testing Reports: Validation results from stress simulations, failure detection accuracy, and real-time data performance.

Outcome:
A fully documented system ready for replication, deployment, or future extension.
AI Model Development
Overview 
The primary feature of the AI-Powered Healthcare Assistant is its ability to assess user symptoms and provide health-related recommendations. In Phase 3, the AI model will be trained and implemented to recognize basic health issues.
 Implementation 
• Natural Language Processing (NLP) Model: The AI system uses NLP to understand user inputs in the form of symptoms. During this phase, the AI is developed to analyze text-based inputs, such as symptoms provided by users in natural language, and output recommendations based on a pre-trained medical dataset.
 • Data Source: The model is based on a medical dataset that contains common symptoms and their associated health conditions. Real-time data will not be integrated at this stage, but will be included in future iterations.
 Outcome 
By the end of this phase, the AI model is expected to provide basic symptom-related advice such as recommending rest, hydration, or consultation with a medical professional. The system should function with high accuracy for common symptoms like fever, cold, and headache.
2. Sensors
Overview
Fibbers Bragg Grating (FBG) sensors are a type of fibber optic sensor used in structural health monitoring to measure strain and temperature with high precision. They consist of a periodic variation in the refractive index along the optical fiber, which reflects specific wavelengths of light and transmits others.

Implementation
• Data Acquisition System (DAQ): The DAQ system collects data from the interrogator and stores it for further analysis. This can be a dedicated system or embedded hardware like a Raspberry Pi or a National Instruments (NI) system.
• Host Computer: The host computer processes the data from the DAQ and can be used to visualize the results, send alerts, or trigger maintenance actions when the strain or temperature exceeds predefined thresholds.
Outcome

The real-time monitoring capabilities of FBG sensors enable early detection of structural issues. By continuously measuring strain and temperature, the system can detect anomalies, such as unusual shifts in the Bragg wavelength, which might indicate developing cracks, deformations, or material fatigue.
3. Data Acquisition System (DAQ)
Overview
A Data Acquisition System (DAQ) is a crucial component, serving as the interface between the sensors (e.g., fibre Bragg Grating (FBG) sensors, accelerometers, strain gauges, etc.) and the system that processes and stores the collected data. The DAQ system collects data from sensors, converts it into a usable form, and transmits it for analysis, display, or storage.
Implementation
• Data Collection: The DAQ system is responsible for collecting raw data from various sensors installed on a structure. These sensors measure parameters like strain, temperature, displacement, acceleration, and vibration
 • Data Conversion: The data collected from sensors, like strain or temperature readings, is often in an analog format. 
Outcome
The Data Acquisition System (DAQ) is a central providing the essential function of capturing, processing, and transmitting data from sensors installed on the monitored structure. 

