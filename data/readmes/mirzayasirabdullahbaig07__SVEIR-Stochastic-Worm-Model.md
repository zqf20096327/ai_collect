# SVEIR Stochastic Worm Model

This repository implements a stochastic **SVEIR** model to study the spread of computer worms in wireless networks such as WSN, MANETs, and IoT systems. The model incorporates stochastic differential equations (SDEs) and Lyapunov stability analysis to determine worm extinction conditions.

---

## Video Demo
https://github.com/user-attachments/assets/b841f9af-d598-4c87-8ee0-962906ebf1b1

---

## ## 1. Model Description

The SVEIR model divides devices into the following compartments:

| Compartment | Description |
|-------------|-------------|
| **S – Susceptible** | Devices that can get infected |
| **V – Vaccinated** | Devices protected by security patches or antivirus |
| **E – Exposed** | Devices that received the worm but are not yet infectious |
| **I – Infected** | Devices actively spreading the worm |
| **R – Recovered** | Devices cleaned or immune |

The stochastic nature accounts for randomness in wireless communication.

---

## ## 2. Why Stochastic?

Wireless networks are unpredictable due to:

- random node mobility  
- uncertain contact events  
- probabilistic transmission  
- environmental noise  

SDEs allow the model to capture this uncertainty.

---

## ## 3. Objectives

The model aims to:

- analyze worm spread in wireless networks  
- determine conditions for infection persistence or extinction  
- examine the impact of vaccination, exposure, and recovery  
- evaluate how randomness affects system behavior  
- use Lyapunov theory to verify extinction  

---

A Lyapunov function is constructed to test system stability and worm extinction.

---

## ## 4. Features

- Stochastic SVEIR model  
- Numerical simulation  
- Lyapunov-based extinction analysis  
- Streamlit GUI for interactive testing  
- Parameter-based experimentation  

---

## ## 5. Installation

Clone the repository:
Install required packages:

---



## ## 6. Running the Model

Run the simulation script:


---

## ## 7. Applications

- Wireless sensor network security  
- Mobile ad hoc network modeling  
- IoT malware analysis  
- Cybersecurity planning  
- Worm propagation research  

---

## ## 8. Summary

This project models how a computer worm spreads in wireless networks using a stochastic SVEIR system. It provides simulation tools and mathematical analysis to determine when the infection will die out and how security measures influence worm behavior.





