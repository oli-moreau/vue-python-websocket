# Vue 3 with python websocket template

This template provides a quick starting point for a Vue 3 project that utilizes SQLite and allows to monitor real-time changes that are made in a Python script with Websocket.

The template structure follows this logic:
- A Python script with a very basic GUI that writes the database
- A Vue interface that monitor the changes in real time
- A Python script that serves Websocket

If the database is created after the Websocket server is started, the HomeView vue needs to be refreshed only once to work properly.

## Project Setup
### Node Dependencies
Run the following command in the project's root directory to install the dependencies:
```sh
npm install
```
### Python Dependencies
Next, install the Python dependencies:
```sh
pip install websockets
```
## Development
### Start the Node.js Development Server
To start the development server, use the following command:
```sh
npm run dev
```
### Start the WebSocket Server
The WebSocket server, located in `sql/websocket.py`, allows real-time communication between the Vue 3 frontend and the Python backend. Start the WebSocket server with the following command:
```sh
python websocket.py
```
### Manual Database Insertion
To make changes to the SQLite database and see the real-time updates in the Vue 3 application, use the `sqlite/database_handler.py` Python script. This script is responsible for managing database insertion by providing a very basic GUI:
```sh
python database_handler.py
```
## Files to Modify
Websocket configuration file:
```
sqlite/websocket.py
```
Database handler:
```
sqlite/database_handler.py
```
Websocket event:
```
src/views/HomeView.vue
```