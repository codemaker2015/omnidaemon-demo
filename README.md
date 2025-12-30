# OmniDeamon Demo

A practical demonstration of **OmniDeamon**, the universal event-driven runtime engine. This repository showcases a simple, scalable agent-based system for producing, managing, and executing tasks in a decoupled architecture.

## 🎯 Overview

This demo project illustrates the core principles of the OmniDeamon engine, which orchestrates autonomous agents ("daemons") that react to events. It provides a foundational blueprint for building resilient, distributed systems where components communicate asynchronously.

### Key Concepts Demonstrated
- **Event-Driven Architecture**: Components communicate through events rather than direct calls.
- **Agent-Based Runtime**: Lightweight, single-purpose agents (`producer`, `runner`) perform specific tasks.
- **Loose Coupling**: Agents are independent and interact via a defined event bus or message queue.
- **Scalability**: The pattern allows for horizontal scaling of individual agent types.

## 🏗️ System Architecture

The demo consists of three primary components that work together:

```
                    [Event Bus / Message Queue]
                            /       \
                           /         \
                    (Publish)       (Consume)
                     /                   \
                    /                     \
            [Producer Agent]      [Agent Runner]
           (Generates events)    (Executes tasks)
```

1.  **Producer Agent** (`producer.py`): Generates events or tasks with payloads.
2.  **Agent Runner** (`agent_runner.py`): Listens for events and executes the corresponding logic or workload.
3.  **Orchestrator** (`main.py`): The main application entry point that initializes the system and coordinates the agents.

## 🚀 Getting Started

### Prerequisites
- **Python 3.11+**
- A package manager like `uv` (recommended via `pyproject.toml`) or `pip`.

### Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/codemaker2015/omnideamon-demo.git
    cd omnideamon-demo
    ```

2.  **Install dependencies**
    The project uses `pyproject.toml` for dependency management.
    ```bash
    # Using uv (preferred)
    uv sync

    # Alternatively, using pip
    pip install .
    ```

### Running the Demo

Execute the main orchestrator script to start the OmniDeamon system:

```bash
python main.py
```

This will typically start the producer and agent runner components, demonstrating the event flow between them.

## 📁 Project Structure

```
omnideamon-demo/
├── .gitignore
├── .python-version        # Specifies Python 3.11+
├── pyproject.toml         # Project metadata and dependencies
├── uv.lock                # Locked dependencies (if using uv)
├── main.py                # Primary orchestrator and entry point
├── producer.py            # Agent responsible for generating events/tasks
├── agent_runner.py        # Agent responsible for consuming and acting on events
└── README.md              # This file
```

## 🔧 How It Works

1.  **Initialization**: The `main.py` script sets up the necessary components, which could include a message broker connection or an in-memory event bus.
2.  **Event Production**: The `producer.py` agent creates task objects or events, often serializes them (e.g., to JSON), and publishes them to a central channel.
3.  **Event Consumption**: The `agent_runner.py` agent subscribes to the same channel. It continuously listens for new events.
4.  **Task Execution**: Upon receiving an event, the runner deserializes the payload and executes the defined task logic.
5.  **Lifecycle Management**: The orchestrator manages the startup and graceful shutdown of all agents.

## 🧪 Extending the Demo

This project serves as a template. You can extend it by:

*   **Adding New Agents**: Create new `.py` files for agents that perform different roles (e.g., a `logger_agent`, `storage_agent`).
*   **Implementing a Real Message Queue**: Replace the simple in-memory event bus with a robust system like **Redis Pub/Sub**, **RabbitMQ**, or **Apache Kafka**.
*   **Modifying the Event Protocol**: Define more complex event schemas using Pydantic models.
*   **Adding Resilience**: Implement retry logic, dead-letter queues, or agent health checks.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/amazing-feature`).
3.  Commit your changes (`git commit -m 'Add some amazing feature'`).
4.  Push to the branch (`git push origin feature/amazing-feature`).
5.  Open a Pull Request.

## 📄 License

This project is licensed under the **MIT License**. See the LICENSE file (if present) for details.

## 🔗 Related Projects

*   **[Intelligent Log Insights Generator](https://github.com/codemaker2015/intelligent-log-insights-generator)** - A full implementation using the OmniDeamon pattern for AI-powered log analysis.

---

**OmniDeamon Demo** - Your starting point for building scalable, event-driven systems with autonomous agents.