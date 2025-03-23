# **Resource Allocation Graph Simulator**
A graphical tool to simulate resource allocation graphs (RAG) and analyze deadlock scenarios interactively. This project includes a Python Flask backend and a frontend built with HTML, CSS, and JavaScript.

# **Features**
Visualize Processes and Resources:

processes and Resources are represented rectangles with black text.

## **Directed Edges:**

Edges represent allocations between processes and resources.

Arrowheads clearly indicate the direction of the allocation.

## **Deadlock Detection:**

Check for deadlocks in the resource allocation graph.

The backend uses a cycle detection algorithm to identify deadlocks.

## **Interactive Controls:**

Add processes and resources.

Create allocations between processes and resources.

Undo actions or restart the graph.

# **Screenshots:**
Example of a resource allocation graph with processes, resources, and directed edges.
![image](https://github.com/user-attachments/assets/41fc93a2-3e87-4458-98e7-aa670b4f8247)
![image](https://github.com/user-attachments/assets/f31ca845-737a-4029-8f49-86d30ff72c2b)


# **Technologies Used**
## **Frontend:**

HTML, CSS, JavaScript

SVG for graph visualization

## **Backend:**

Python Flask

Deadlock detection using cycle detection in graphs

# **How to Run the Project**
##Prerequisites
**Python 3.x:** Ensure Python is installed on your system.

**Flask:** Install Flask using pip.

```bash
pip install flask
```
**Web Browser:** Use a modern web browser like Chrome, Firefox, or Edge.

## Steps to Run
###Clone the Repository:
```bash
git clone https://github.com/your-username/resource-allocation-graph-simulator.git

cd resource-allocation-graph-simulator
```
## **Run the Backend:**

### Start the Flask server by running:

```bash
python app.py
```
The backend will start at http://127.0.0.1:5000.

## **Open the Frontend:**

Open the index.html file in your browser.

Alternatively, you can use a local server (e.g., VS Code Live Server) to serve the frontend.

## **Interact with the Simulator:**

Add processes and resources using the input fields.

Create allocations by specifying the "From" and "To" nodes.

Click "Check Deadlock" to analyze the graph for deadlocks.

# **Project Structure**
```
resource-allocation-graph-simulator/
├── app.py                  # Flask backend for deadlock detection
├── index.html              # Frontend HTML file
├── README.md               # Project documentation
├── screenshot.png          # Screenshot of the simulator
└── styles.css              # CSS for styling the frontend
```
# API Endpoints
The backend provides the following API endpoints:

## Check Deadlock:

**Endpoint:** GET /api/check-deadlock

**Description:** Checks for deadlocks in the current graph.

**Response:**

```json
{
  "deadlock": true/false
}
```
## Update Graph:

**Endpoint:** POST /api/graph

**Description:** Updates the graph with the current state of processes, resources, and edges.

**Request Body:**

```json
{
  "processes": ["P1", "P2"],
  "resources": ["R1", "R2"],
  "edges": [
    { "from": "P1", "to": "R1" },
    { "from": "R1", "to": "P2" }
  ]
}
```
**Response:**

```json
{
  "message": "Graph updated successfully"
}
```
# How It Works
**Graph Representation:**

Processes and resources are represented as nodes.

Allocations are represented as directed edges.

**Deadlock Detection:**

The backend builds a graph and checks for cycles using Depth-First Search (DFS).

If a cycle is detected, a deadlock exists.

**Frontend-Backend Communication:**

The frontend sends updates to the backend whenever processes, resources, or edges are added.

The frontend queries the backend to check for deadlocks.

# Example Workflow
Add processes (e.g., P1, P2).

Add resources (e.g., R1, R2).

Create allocations (e.g., P1 -> R1, R1 -> P2, P2 -> R2, R2 -> P1).

Click "Check Deadlock" to see if a deadlock exists.

# Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Commit your changes.

Submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments
Inspired by resource allocation graphs and deadlock detection algorithms.

Built with Flask, HTML, CSS, and JavaScript.

# Contact
For questions or feedback, please open an issue on GitHub or contact sabeena0.

Enjoy simulating resource allocation graphs and detecting deadlocks! 🚀
