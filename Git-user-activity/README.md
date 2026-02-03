# GitHub API CLI Tool — Python

## Project Description

Command-line application developed in Python to consume the GitHub API without using external libraries, focusing on robustness, defensive programming, and a deeper understanding of HTTP communication.

## Key Responsibilities & Achievements

- Implemented HTTP requests using Python’s native `urllib.request`, leveraging context managers (`with`) to ensure proper connection handling and resource cleanup.
- Designed resilient error handling using specific exceptions (`HTTPError`, `URLError`) to gracefully manage API errors and network failures.
- Safely navigated complex and nested JSON responses by using dictionary `.get()` methods, preventing runtime errors such as `KeyError`.
- Built a dynamic Command Line Interface (CLI) using `sys.argv`, including argument validation to improve usability and prevent invalid executions.

## Technologies & Concepts

- Python  
- GitHub REST API  
- HTTP Protocol  
- JSON Parsing  
- CLI Applications  
- Error Handling & Defensive Programming
