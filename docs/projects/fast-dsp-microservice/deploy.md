# Deploy a FastAPI Microservice to AWS EC2

This guide walks you through building and deploying a simple FastAPI microservice that fetches tide data from an external API and serves it through a REST endpoint. You'll write the FastAPI app, deploy it to an AWS EC2 instance, and access the live data using your browser or `curl`. This is a common microservice pattern: encapsulate external APIs, reformat the data, and serve it to other systems — all via a single, stateless endpoint.

## Prerequisites

This tutorial assumes:
- Python 3.10+ installed locally
- An AWS account with EC2 access
- Basic familiarity with HTTP APIs, Python, and the terminal

---

## 1. Create the FastAPI app

```bash
mkdir tide-api && cd tide-api
touch main.py .env requirements.txt
