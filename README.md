# Agentic AI Task Manager

This project implements an agentic AI task manager application that allows users to manage tasks through natural language prompts. It leverages the Agno framework to orchestrate multiple specialized agents that interact with a database (Supabase/PostgreSQL) and Google Calendar.

## ✅ Project Overview

This application enables users to input tasks via natural language prompts, such as "Remind me to call Alex tomorrow at 5 PM." Behind the scenes, a team of intelligent agents processes these prompts to store the tasks in a database and, when appropriate, add events to the user's Google Calendar.

**💡 Functionality:**

* **Natural Language Input:** Users interact with the application using simple prompts.
* **Task Extraction:** Extracts crucial information (task description, date, time, etc.) from user prompts.
* **Database Integration:** Stores, reads, and updates task information in a Supabase/PostgreSQL database.
* **Google Calendar Integration:** Creates and updates events in the user's Google Calendar.
* **Intelligent Reasoning:** Determines whether a task warrants an entry in the Google Calendar.

**⚙️ Agents:**

* **Task Extractor (`agents/task_extractor_agent.py`):** This agent is responsible for parsing user prompts and identifying key details such as the task itself, due dates, times, and any other relevant information.
* **DB Agent (`agents/db_agent.py`):** This agent handles all interactions with the task database. It can create new task entries, retrieve existing tasks, and update task information as needed.
* **Calendar Agent (`agents/calendar_agent.py`):** This agent interfaces with the Google Calendar API. It can create new calendar events, modify existing ones, and potentially retrieve calendar information.
* **Reasoning Agent (`agents/reasoning_agent.py`):** This agent employs an LLM (likely via OpenAI/GPT) to decide whether a given task should be added to the user's Google Calendar. For example, it might determine that a simple reminder doesn't need a calendar event, while a time-specific appointment does.

**🛠️ Tools:**

* **Agno:** Used for orchestrating the workflow of the different agents, ensuring they work together seamlessly to process user requests.
* **Supabase/PostgreSQL:** Serves as the persistent storage for task data.
* **Google Calendar API:** Enables the application to interact with Google Calendar for event management.
* **OpenAI/GPT:** Powers the Reasoning Agent, providing the language understanding and decision-making capabilities needed to determine calendar event creation.

## 📂 Folder Structure

```bash
agentic-task-app/
├── agents/
│   ├── task_extractor.py        # Extracts task, date, time, etc.
│   ├── db_agent.py              # Interacts with DB to store/retrieve tasks
│   ├── calendar_agent.py        # Connects to Google Calendar
│   └── reasoning_agent.py       # Decides whether calendar update is needed
│
├── db/                          # Pluggable DB interface
│ ├── base.py
│ ├── file_db.py
│ └── supabase_db.py             # (optional - for prod)
│
├── workflows/
│   └── task_workflow.py         # Agno workflow that calls the agents in sequence
│
├── utils/                   
│   ├── calendar.py              # Google Calendar setup/auth
│   └── schema.py                # Task data model
│
├── config.py                    # Environment config (dev/prod db switch)
├── Dockerfile                   # Docker configuration file
├── .env                         # API keys and secrets
├── main.py                      # Entry point
├── requirements.txt
├── tasks.json                   # Created automatically in dev
└── README.md
```

* **`agents/`:** Contains modular agent implementations used in the Agno workflow. These include:
  - `task_extractor_agent.py` – Extracts task info from user input
  - `reasoning_agent.py` – Determines if a task is time-sensitive and calendar-worthy
  - `calendar_agent.py` – Adds tasks to Google Calendar (with user consent)
  - `db_agent.py` – Abstracts database interaction via the configured DB backend

* **`workflows/`:** Defines end-to-end workflows using Agno. Currently includes `task_workflow.py`, which orchestrates the full task processing pipeline (extraction → DB → reasoning → calendar interaction).

* **`db/`:** Contains the database abstraction layer following the repository pattern:
  - `base.py` – Abstract base class/interface for DBs
  - `file_db.py` – File-based (JSON) DB for development
  - `supabase_db.py` – Placeholder for production-ready DB implementation

* **`utils/`:** Helper modules used across the app:
  - `calendar.py` – Google Calendar API setup and helper functions
  - `schema.py` – Optional data model schemas (e.g., for task structure)

* **`config.py`:** Manages app configuration such as environment mode (e.g., selecting between file DB or production DB via `.env`).

* **`.env`:** Stores sensitive environment variables like API keys and DB mode. **Do not commit this file to version control.**

* **`main.py`:** CLI-based entry point for interacting with the task agent system.

* **`requirements.txt`:** Lists all required Python packages to run the project (Agno, OpenAI, dotenv, etc.).

* **`README.md`:** You're reading it – a full guide and documentation for the project.


## ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd agentic-task-app
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    * Create a `.env` file in the root directory.
    * Add the necessary API keys and credentials. This will likely include:
        * Supabase/PostgreSQL connection details (e.g., database URL, API key).
        * Google Calendar API credentials (e.g., client ID, client secret, refresh token - refer to the Google Calendar API documentation for setup).
        * OpenAI API key.

    ```
    SUPABASE_URL=your_supabase_url
    SUPABASE_KEY=your_supabase_api_key
    GOOGLE_CLIENT_ID=your_google_client_id
    GOOGLE_CLIENT_SECRET=your_google_client_secret
    GOOGLE_REFRESH_TOKEN=your_google_refresh_token
    OPENAI_API_KEY=your_openai_api_key
    ```

4.  **Set up the database:**
    * Ensure you have a Supabase/PostgreSQL database set up.
    * The `utils/db.py` file likely contains the logic to connect to and potentially initialize the database schema. Refer to this file for any specific database setup instructions.

5.  **Set up Google Calendar API:**
    * Follow the Google Calendar API documentation to create credentials and obtain the necessary client ID, client secret, and refresh token. Store these in your `.env` file.

## 🚀 Running the Application

To run the application, execute the `main.py` script:

```bash
python main.py
```

Refer to the main.py file for instructions on how to interact with the application (e.g., through command-line prompts or a web interface, if implemented).

## 🐳 Docker Support
This project includes a Dockerfile for easy containerization.  You can use Docker to build and run the application in a consistent environment.

**Prerequisites**

- Docker installed on your system.

**Building the Docker Image**

- Navigate to the project root directory in your terminal.

- Run the following command to build the Docker image:
    ```bash
    docker build -t agentic-task-app .
    ```
    This command builds an image named agentic-task-app based on the Dockerfile in the current directory.

**Running the Docker Container**

After the image is built, run the following command to start a container:

```bash
docker run -it --env-file .env agentic-task-app
```

**`-it`:** Runs the container in interactive mode with a pseudo-TTY.

**`--env-file .env`:**  Passes the environment variables from your .env file to the container.  Ensure .env is in the same directory, or provide the correct path.

**`agentic-task-app`:**  The name of the Docker image to run.

## 🤝 Contributing

Contributions to this project are welcome. Please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.   
- Make your changes and commit them with clear and concise messages.
- Push your changes to your fork.
- Submit a pull request to the main repository.

## 📄 License

This project is under [MIT License](LICENSE)