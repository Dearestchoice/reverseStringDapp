# ReverseString DApp

This is a simple backend application for the ReverseString DApp, built using Python and Flask. It takes an input string, reverses it, and can interact with the Cartesi Rollups APIs (Notice, Voucher, and Reports).

## Project Structure

- `Dockerfile`: The Docker configuration file to build and run the app in a container.
- `dapp.py`: The main application script that handles the reverse string logic.
- `requirements.txt`: Lists the dependencies required to run the DApp.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Prerequisites

- Docker installed on your machine
- Python 3.9 installed (for local development)
- Cartesi CLI (if you plan to extend this DApp)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/reverse-string-dapp.git
   cd reverse-string-dapp

   #Build the docker image   
docker build -t reverse-string-dapp .

#Run the Docker container:
docker run --rm -p 5000:5000 reverse-string-dapp

#Test the DApp:

You can test the DApp by sending a POST request to the /reverse endpoint. 
For example:  curl -X POST -H "Content-Type: application/json" -d '{"input": "hello"}' http://localhost:5000/reverse
The response will be:

json
Copy code
{
  "input": "hello",
  "reversed": "olleh"


