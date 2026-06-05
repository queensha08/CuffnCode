# Distributed Smart Energy Monitoring System (MCU Pipeline Simulation)

## IFB-206 KOMPUTASI PARAREL & SISTEM TERDISTRIBUSI

- **Nama** : Ratu Syifa Nur Felisha - 152024170

---

> **Parallel Computing & Distributed Systems – MCU Pipeline Simulation (No Hardware)**

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/UI%20Framework-Streamlit-red.svg)](https://streamlit.io/)
[![Data Processing](https://img.shields.io/badge/Processing-NumPy%20%26%20Pandas-green.svg)]()
[![Visualization](https://img.shields.io/badge/Visualization-Plotly%20%26%20Matplotlib-orange.svg)]()
[![Category](https://img.shields.io/badge/Course-Parallel%20Computing%20%26%20Distributed%20Systems-purple.svg)]()

---

## 1. Project Overview

The **Distributed Smart Energy Monitoring System** is an advanced simulation-based project designed to model a multi-node MCU (Microcontroller Unit) pipeline architecture for real-time energy monitoring and anomaly detection.

This project is developed as part of the **Parallel Computing and Distributed Systems** course and demonstrates key computing paradigms such as:

- **Distributed Pipeline Processing**  
  Each processing stage is modeled as an independent computational node, simulating a real MCU-based distributed embedded system.

- **Parallel Execution Simulation**  
  Node operations are structured as modular processes, mimicking parallel execution in embedded systems.

- **Streaming Telemetry System**  
  Data flows continuously across nodes, simulating real-time sensor-to-dashboard communication.

- **SCADA-style Monitoring Interface**  
  A real-time Streamlit-based dashboard visualizes system behavior, metrics, and telemetry logs.

This system is fully simulated using Python, without requiring physical hardware, while preserving architectural fidelity of real embedded distributed systems.

---

## 2. Key Features

- **Multi-Node MCU Pipeline Simulation**
  - Node 1: Signal Acquisition (Voltage & Current)
  - Node 2: Feature Extraction (Power & RMS)
  - Node 3: Anomaly Detection
  - Node 4: Classification Engine
  - Node 5: Output & Logging Layer

- **Real-Time SCADA Dashboard (Streamlit)**
  - Live system metrics
  - Power and voltage visualization
  - Latency monitoring
  - Status indicators (NORMAL / ANOMALY / FAULT)

- **Streaming Data Visualization**
  - Real-time line charts
  - Dynamic metric updates
  - System log viewer

- **CSV Telemetry Logging**
  - Automatic structured logging of all system outputs
  - Timestamped dataset generation for analysis

- **Performance Metrics Engine**
  - Latency calculation per pipeline cycle
  - Throughput estimation
  - System performance tracking

---

## 3. System Architecture

The system is designed as a sequential distributed pipeline simulating MCU-based embedded processing nodes:

```mermaid
graph LR
    A[Node 1: Signal Acquisition] --> B[Node 2: Feature Extraction]
    B --> C[Node 3: Anomaly Detection]
    C --> D[Node 4: Classification]
    D --> E[Node 5: Output & Logging]
    E --> F[Streamlit SCADA Dashboard]
   
Each node is responsible for a specific stage of computation, mimicking real embedded MCU task partitioning.

---

##  4. Distributed System Design

Although implemented in Python, the system follows a distributed systems paradigm:
- Each node represents an independent processing unit
- Data flows sequentially through pipeline stages
- Communication is simulated via function-based message passing
- No shared state between nodes
    ```mermaid
    sequenceDiagram
        participant S as Sensor Simulation
        participant N1 as Node 1
        participant N2 as Node 2
        participant N3 as Node 3
        participant N4 as Node 4
        participant N5 as Node 5
        participant UI as Streamlit Dashboard

        loop Real-Time Simulation Cycle
            S->>N1: Generate Voltage & Current
            N1->>N2: Feature Extraction (Power, RMS)
            N2->>N3: Anomaly Detection
            N3->>N4: Classification
            N4->>N5: Final Output
            N5->>UI: Stream Data + Metrics + Logs
        end
---

## 5. Parallel Computing Concept

Although not using multiprocessing directly, the system simulates parallel computing through:
- Modular node decomposition
- Independent computation stages
- Pipeline-based execution model
- Continuous streaming loop execution
This reflects how embedded systems distribute workloads across MCU units in real IoT systems.

---

## 6. SCADA Dashboard Features

The Streamlit SCADA interface provides:
- Real-time voltage, current, and power monitoring
- System status indicators:
  - 🟢 NORMAL
  - 🟡 ANOMALY
  - 🔴 FAULT
- Latency performance tracking
- Time-series visualization
- Live system logs (CSV-backed)
- Interactive sidebar controls

---

## 7. CSV Logging System

All system outputs are stored in:
logs/system_log.csv

Each record contains structured telemetry data generated from the MCU pipeline simulation:

| Field       | Description                                  |
| :---------- | :------------------------------------------- |
| **timestamp** | Execution time of each pipeline cycle       |
| **voltage**   | Simulated sensor voltage reading (V)        |
| **current**   | Simulated sensor current reading (A)        |
| **power**     | Computed electrical power (V × A)           |
| **rms**       | Root Mean Square value of voltage signal    |
| **status**    | System state classification (NORMAL/ANOMALY/FAULT) |

This structured logging enables:
- Post-simulation performance analysis
- System behavior tracking over time
- Benchmarking of distributed MCU pipeline execution
- Dataset generation for further machine learning experiments

---

## 8. Performance Metrics


The system computes:
- Latency per cycle → time required for one full pipeline execution
- Throughput estimation → number of processed cycles per second
These metrics simulate performance evaluation in distributed embedded systems.

---

## 9. Installation Requirements

- Prerequisites
Python 3.10+
- Install Dependencies
pip install streamlit numpy pandas

---

## 10. How To Run

- Run SCADA Dashboard
streamlit run app.py

---
```md id="treefix"
## 11. Project Structure

```text
DISTRIBUTED-MCU-SIM/
│
├── app.py                     # STREAMLIT DASHBOARD (UI layer)
├── main.py                    # SINGLE PIPELINE TEST RUNNER
├── run_system.py              # SYSTEM LAUNCHER (dashboard + tools)
│
├── core/
│   ├── pipeline.py            # orchestrator (MCU chain logic)
│   └── metrics.py             # latency & throughput calculator
│
├── nodes/
│   ├── acquisition.py         # Node 1: sensor simulation
│   ├── feature.py             # Node 2: feature extraction
│   ├── anomaly.py             # Node 3: anomaly detection
│   ├── classifier.py          # Node 4: classification
│   └── output.py              # Node 5: output formatter
│
├── simulator/
│   └── signal.py              # synthetic sensor generator
│
├── monitoring/
│   ├── logger.py              # CSV telemetry logging system
│   └── event_bus.py           # inter-node communication
│
├── benchmark/
│   └── benchmark.py           # performance evaluation
│
├── logs/
│   └── system_log.csv         # runtime telemetry
│
└── docs/
    ├── architecture.md
    ├── analytics.png
    ├── monitoring.png
    └── systemLog.png

---

## 12. Conclusion

This project demonstrates a simulation-based distributed MCU pipeline system integrating:
- Parallel computing principles
- Distributed system architecture
- Real-time telemetry processing
- SCADA-style visualization dashboard
Although fully software-based, the system accurately models embedded IoT pipeline behavior.

---

## 13. Future Improvements

- Real multiprocessing distributed node execution
- RTOS-based MCU simulation layer
- WebSocket real-time streaming
- Hardware integration (STM32 / ESP32)
- Advanced anomaly detection using TinyML models