# 📝 Todo API - Django (DevSecOps Project)

A production-ready **Todo API** built with Django REST Framework, designed with a DevSecOps mindset. This project includes robust development workflows, containerization, secure coding practices, static code analysis, and CI/CD automation.

---

## 🚀 Features

* ✅ RESTful API for managing TODO tasks
* 🐳 Dockerized for consistent and isolated environments
* 🦢 Unit tests for endpoints and models
* 🧹 Code formatting and linting with `Black`, `Flake8`, and `isort`
* 🔐 Secret detection and pre-commit hooks
* ✅ GitHub Actions CI/CD pipeline

  * Code linting and formatting checks
  * Unit testing
  * Static code analysis with **SonarQube**
  * Image vulnerability scanning with **Docker Scout**
* 📦 Infrastructure-as-Code using `Docker` and GitHub Workflows

---

## 📂 Project Structure

```bash
todo-api-django/
├── .github/workflows/         # CI/CD pipelines
├── app/                       # Django project root
│   ├── todo/                  # Django app: models, views, urls, serializers
│   └── tests/                 # Unit tests
├── Dockerfile                 # Docker container definition
├── docker-compose.yml         # Local development setup
├── requirements.txt           # Python dependencies
├── .flake8                    # Flake8 configuration
├── pyproject.toml             # Black & isort config
└── .pre-commit-config.yaml    # Pre-commit hooks
```

---

## 🐳 Quick Start (Docker)

```bash
# Build and run the API
docker-compose up --build

# Access the API at
http://localhost:8000/api/todos/
```

---

## ✅ Run Tests

```bash
# Using Docker
docker-compose run web python manage.py test

# Locally (after setting up a virtualenv)
python manage.py test
```

---

## 🔨 Pre-Commit Setup (Flake8, Black, isort, Secrets)

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run pre-commit on all files
pre-commit run --all-files
```

Includes:

* `flake8` for Python linting
* `black` for code formatting
* `isort` for import sorting
* `detect-secrets` for secret detection

---

## 🛠️ GitHub Actions CI/CD

On each push, the following are automatically triggered:

* ✅ Lint & format check
* ✅ Unit testing
* ✅ SonarQube code analysis
* ✅ Docker Scout for image vulnerabilities
* ✅ Docker image build & push

---

## 📊 SonarQube Integration

The project integrates with **SonarQube** for:

* Code smells
* Duplications
* Test coverage
* Security hotspots
* Vulnerabilities

> The analysis is triggered in the GitHub Actions pipeline and uses the SonarQube Scanner CLI.

---

## 🔍 Docker Scout

Image security is scanned automatically using **Docker Scout** to identify vulnerabilities and supply chain issues.

---

## 📦 API Endpoints

| Method | Endpoint           | Description            |
| ------ | ------------------ | ---------------------- |
| GET    | `/api/todos/`      | List all todos         |
| POST   | `/api/todos/`      | Create a new todo      |
| GET    | `/api/todos/{id}/` | Retrieve a single todo |
| PUT    | `/api/todos/{id}/` | Update a todo          |
| DELETE | `/api/todos/{id}/` | Delete a todo          |

---

## 🔒 Security Practices

* Pre-commit secret scanning
* SonarQube static analysis
* Docker Scout vulnerability scans
* Minimal base image and pinned dependencies

---

## 📈 CI/CD Status

[![CI](https://github.com/Mficius/todo-api-django/actions/workflows/main.yml/badge.svg)](https://github.com/Mficius/todo-api-django/actions)

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## 📜 License

MIT License © [Mayitoukou Sigmund](https://github.com/Mficius)

---

## 🔗 Project Link

👉 [GitHub Repository](https://github.com/Mficius/todo-api-django)

---
