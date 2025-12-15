# Spacial AI Home Assignment for Avi Noam

**Author:** Yotam Aloni  
**Date:** 15.12.2025

---

## System Requirements

- **Operating System:** Windows / Linux / macOS  
- **Python Version:** 3.10 or higher  

---

## Technologies Used

- **Python 3.10**
- **ChatGPT AI**
- **Claude AI**

---


## Python Dependencies

The project requires the following Python packages:

> All dependencies are listed in `requirements.txt`.

---

## Description
The project is designed 


### Assumptions
1. Connected nodes ordering - Connected nodes are stored consecutively in the polygon node array.

2. Surface connectivity - Each roof surface is assumed to be connected to at least one other surface.

### Improvement

1. A new field called `support` has been added to the JSON file but it is not currently used by the application.
   This field defines support points on the model. For example:
   ```json
   "support": [
   {
      "x": 1.0,
      "y": -0.5,
      "z": 0.0,
      "pinned_x" : true,
      "pinned_y" : false,
      "pinned_z" : false,
      "fixed_x": false,
      "fixed_y": true,
      "fixed_z": false,
   }
   ]
   ```
---

## 🚀 How to Run the Project (Windows)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yotamaloni/Spacial.git
   cd Spacial
   ```

2. **Create and activate the virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install the project dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

---

## 📌 Notes
- Do not commit the `.venv` directory
- Always activate the virtual environment before running the project

---
