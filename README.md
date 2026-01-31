# hackernews-api-test
Take Home by Together AI

## Overview
Automated API tests for the Hacker News API using pytest and requests.

## Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

## Setup

1. **Clone the repository** (if not already done):
```bash
cd hackernews-api-test
```

2. **Create a virtual environment**:
```bash
python3 -m venv venv
```

3. **Activate the virtual environment**:
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

4. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Running Tests

**Run all tests**:
```bash
pytest
```

**Run with verbose output**:
```bash
pytest -v
```

**Run with output capture disabled** (see print statements):
```bash
pytest -v -s
```

**Run specific test file**:
```bash
pytest tests/test_topstories.py
pytest tests/test_items.py
```

**Run specific test**:
```bash
pytest tests/test_topstories.py::test_topstories_returns_200
```

## Configuration

The base URL for the Hacker News API can be configured via environment variable:
```bash
export HB_BASE_URL="https://hacker-news.firebaseio.com/v0"
pytest
```

Default URL: `https://hacker-news.firebaseio.com/v0`

## Test Coverage

- **Top Stories Endpoint** (`/topstories.json`):
  - Response status and format validation
  - Data type and uniqueness checks
  
- **Items Endpoint** (`/item/{id}.json`):
  - Story metadata validation
  - Comment structure validation
  - Invalid ID handling
