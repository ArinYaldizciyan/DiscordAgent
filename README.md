# LangChain Discord Bot

A basic Discord bot built with LangChain that can interact with users through natural language processing.

## Setup Instructions

### 1. Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Navigate to the "Bot" tab in the left sidebar
4. Click "Add Bot" and confirm
5. Under the "Bot" section, click "Reset Token" to generate a new token
6. Copy the token - you'll need it later
7. Under "Privileged Gateway Intents", enable:
   - Message Content Intent
   - Server Members Intent
   - Presence Intent

### 2. Invite the Bot to Your Server

1. Go to the "OAuth2" tab in the left sidebar
2. In the "URL Generator" section:
   - Select the `bot` scope
   - Select the following permissions:
     - Send Messages
     - Read Message History
     - Use Slash Commands
     - Read Messages/View Channels
3. Copy the generated URL and open it in your browser
4. Select the server you want to add the bot to

### 3. Environment Setup

1. Create a `.env` file in the root directory of the project
2. Add your Discord bot token:
   ```
   DISCORD_BOT_KEY=your_bot_token_here
   ```
   Replace `your_bot_token_here` with the token you copied from the Discord Developer Portal

### 4. Installation

1. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 5. Running the Bot

1. Make sure your virtual environment is activated
2. Run the bot:
   ```bash
   python bot.py
   ```

## Features

- Basic LangChain integration for natural language processing
- Discord slash commands support
- Message handling and response generation

## Security Note

- Never commit your `.env` file or share your bot token
- The `.env` file is already included in `.gitignore` to prevent accidental commits
- If your token is ever exposed, immediately reset it in the Discord Developer Portal

## Requirements

See `requirements.txt` for all required Python packages.
