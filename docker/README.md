# 📦 Containerization: Introduction to Docker and Container Orchestration with Kubernetes

Containerization is a way of packaging and running applications in isolated environments.  
It simplifies deployment, ensures consistency, and enables easy scaling of applications.

---

## 🔑 Key Topics

1. Docker  
2. Kubernetes

---

## 🐳 Docker

**Docker** is a platform for shipping and running applications inside lightweight containers.  
These containers hold the application code along with its dependencies, ensuring consistency across different environments.

---

### 🔧 Key Concepts

#### **Images**
- Blueprints for containers, created from `Dockerfile`s.
- Templates used to create container instances.

#### **Containers**
- Lightweight, standalone, and executable packages that include everything needed to run an application:
  - Code
  - Runtime
  - System tools
  - Libraries
  - Configuration files
- They share the host system's OS kernel but are isolated from each other.
- A running instance of an image.

#### **Environment**
The **environment** is the set of conditions in which an application runs — the setup it depends on. This includes:
- Operating System
- Installed libraries and tools
- Environment variables (e.g., `DATABASE_URL`, `DEBUG=True`)
- Runtime (e.g., Python 3.11, Node.js 18, Java 17)
- File paths and directory structures

| Type           | Purpose                                  |
|----------------|-------------------------------------------|
| Development    | Where you write and test code locally     |
| Testing/Staging| Where code is tested before going live    |
| Production     | The live system that users interact with  |

#### **Dependencies**
External packages, libraries, or tools the application needs to function.  
Examples (in Python): `flask`, `gunicorn`, `requests`, `psycopg2`.

#### **Installing Dependencies in Docker**

```dockerfile
# Python
RUN pip install -r requirements.txt

# Node.js
RUN npm install
```

---

### 📚 Important Docker Terms

| Term         | Description                                                     |
|--------------|-----------------------------------------------------------------|
| `Dockerfile` | Text file with instructions to build a Docker image            |
| `Image`      | Snapshot of a container, built from a Dockerfile                |
| `Container`  | A running instance of an image                                  |
| `Docker Hub` | Public registry for Docker images                               |
| `Volume`     | Used to persist data outside the container lifecycle            |
| `Network`    | Enables communication between containers                        |

---

### 💻 Common Docker Commands

\`\`\`bash
# Build an image
docker build -t myapp .

# Run a container
docker run -d -p 5000:5000 myapp

# List running containers
docker ps

# Stop a container
docker stop <container_id>

# Remove a container
docker rm <container_id>

# Remove an image
docker rmi myapp
\`\`\`

---

### ✅ Benefits of Docker

- **Consistency**: Same behavior in development, testing, and production.
- **Portability**: Runs anywhere Docker is installed.
- **Efficiency**: Uses fewer resources than virtual machines (VMs).
- **Isolation**: Keeps applications and services isolated from each other.

---

## 🧩 Docker Compose

**Docker Compose** is a tool for defining and running multi-container Docker applications.  
It links services, manages networks, and handles volumes through a single configuration file: `docker-compose.yml`.

### 🧱 Key Concepts

| Concept     | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| **Service** | A container definition (e.g., web, db), defined in YAML                     |
| **Network** | Docker Compose links containers automatically so they can communicate       |
| **Volume**  | Persistent storage used by containers                                       |

### ⚙️ Example Commands

\`\`\`bash
# Start all services defined in docker-compose.yml
docker-compose up

# Stop and remove all services and resources
docker-compose down
\`\`\`

**Use Case:** Ideal for local development or small-scale environments running multiple services (e.g., a web app + database).
