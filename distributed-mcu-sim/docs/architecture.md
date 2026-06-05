# ⚡ Distributed MCU Simulation System Architecture

## 1. Overview

The system is a **simulated distributed multi-MCU pipeline architecture** designed to emulate real embedded TinyML inference systems using a modular Python-based framework.

Instead of physical MCU hardware, the system simulates each MCU node as an independent computational unit executing a specific stage of a data processing pipeline.

This design follows the concept of:

- Layer-wise distributed computation
- Streaming data pipeline execution
- Event-driven inter-node communication
- Real-time telemetry monitoring

---

## 2. System Objectives

The primary objectives of this system are:

- Simulate distributed MCU-based computation pipeline
- Model real-time sensor data processing
- Analyze latency and throughput of multi-stage processing
- Provide real-time visualization via a web-based dashboard
- Implement modular and scalable architecture

---

## 3. High-Level Architecture

The system consists of five main layers:
+----------------------+
| Streamlit Dashboard|
| (Visualization Layer)|
+----------+-----------+
^
|
+----------+-----------+
| Output Node (MCU5) |
+----------+-----------+
^
|
+----------+-----------+
| Classification Node |
| (MCU4) |
+----------+-----------+
^
|
+----------+-----------+
| Anomaly Detection |
| (MCU3) |
+----------+-----------+
^
|
+----------+-----------+
| Feature Extraction |
| (MCU2) |
+----------+-----------+
^
|
+----------+-----------+
| Acquisition Node |
| (MCU1) |
+----------+-----------+
^
|
+----------------------+
| Signal Simulator |
+----------------------+


---

## 4. Node-Level Architecture

### 🔹 Node 1: Acquisition Layer
- Generates synthetic sensor signals (voltage, current)
- Simulates real-world sensor acquisition in MCU systems
- Acts as entry point of the pipeline

---

### 🔹 Node 2: Feature Extraction Layer
- Computes derived features:
  - Power = Voltage × Current
  - RMS approximation
- Reduces raw sensor data into meaningful features

---

### 🔹 Node 3: Anomaly Detection Layer
- Applies threshold-based detection
- Identifies abnormal power consumption patterns
- Outputs system state: NORMAL / ANOMALY

---

### 🔹 Node 4: Classification Layer
- Converts anomaly status into system classification
- Produces final decision labels:
  - NORMAL
  - FAULT

---

### 🔹 Node 5: Output Layer
- Aggregates processed results
- Sends structured data to visualization layer
- Acts as final MCU in pipeline

---

## 5. Communication Model

The system uses a **simulated event-driven communication model**:

- Data flows sequentially between nodes
- Each node processes and forwards results
- Communication is abstracted as function calls (no physical UART)

Optional extension (future work):
- Event Bus system (message queue simulation)
- Async streaming pipeline

---

## 6. Performance Monitoring

The system includes a built-in performance analysis module:

### Metrics:
- **Latency**: Time per pipeline execution cycle
- **Throughput**: Number of processed cycles per second
- **Execution Time**: Total system runtime

These metrics simulate real embedded system benchmarking similar to MCU pipeline evaluation in distributed TinyML systems.

---

## 7. Data Logging System

All pipeline outputs are recorded into a CSV telemetry log:
logs/system_log.csv


Logged fields:
- Timestamp
- Voltage
- Current
- Power
- RMS
- Status

This enables:
- Offline analysis
- System debugging
- Performance evaluation

---

## 8. Visualization Layer

A Streamlit-based dashboard provides:

- Real-time system metrics
- Power and voltage trend visualization
- Live classification status
- Latency monitoring graph
- Tabular telemetry display

This acts as the **SCADA-like monitoring interface** of the system.

---

## 9. System Characteristics

- Modular architecture (node-based design)
- Distributed computation simulation
- Streaming pipeline processing
- Event-driven execution model
- Real-time monitoring interface

---

## 10. Future Improvements

Potential enhancements include:

- True asynchronous event bus (Kafka-like simulation)
- RTOS behavior emulation (task scheduling simulation)
- Multi-stream parallel pipeline execution
- Hardware-in-the-loop integration
- SPI/UART protocol simulation
- Advanced TinyML model integration

---

## 11. Conclusion

This system demonstrates a **software-based simulation of a distributed MCU pipeline architecture** inspired by real-world embedded TinyML systems.

It provides insights into:
- Distributed computation design
- Streaming data processing
- System performance trade-offs (latency vs throughput)
- Modular embedded system architecture

This makes the system suitable as a foundation for research in:
- Embedded AI systems
- Distributed edge computing
- Multi-node inference pipelines