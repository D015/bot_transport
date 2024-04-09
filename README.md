# Bot translator

### Prerequisites
What you need to install on your computer to use the project:

Python 3.11 or higher
The latest version of pip

### Installation
A step-by-step series of examples that tell you how to get a development environment running.

1. Clone the repository:
```bash
git clone <URL репозитория>
```
2. Navigate to the project directory:
```bash
cd <directory name>
```
3. Set up a virtual environment:
```bash
python -m venv venv
```
4. Activate the virtual environment:
```bash
source venv/bin/activate
```
5. Install the dependencies:
```bash
pip install -r requirements.txt
```
6. Create an .env file in the root directory:
```bash
touch .env
```
and add the environment variables to it:
```bash
TELEGRAM_BOT_TOKEN=<your_telegram_bot_token>
DISCORD_BOT_TOKEN=<your_discord_bot_token>
```
7. Launch the project:
```bash
python main.py
```

## Testing
... 

