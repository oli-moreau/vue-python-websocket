import tkinter as tk
import sqlite3
import websockets
import asyncio
import json

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

async def send_update():
    cursor.execute('SELECT * FROM bookshelf')
    updated_data = cursor.fetchall()

    async with websockets.connect('ws://localhost:12345') as websocket:
        await websocket.send(json.dumps(updated_data))

# Function to insert a new row into the bookshelf table
def insert_book():
    title = title_entry.get()
    summary = summary_entry.get()
    category = category_entry.get()
    nb_pages = nb_pages_entry.get()
    rating = rating_entry.get()
    author_name = author_name_entry.get()
    author_lastname = author_lastname_entry.get()

    # Insert the data into the database
    cursor.execute('''
        INSERT INTO bookshelf (title, summary, category, nb_pages, rating, author_name, author_lastname)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (title, summary, category, nb_pages, rating, author_name, author_lastname))
    
    conn.commit()
    clear_entries()

    asyncio.get_event_loop().run_until_complete(send_update())

# Function to clear the input fields
def clear_entries():
    title_entry.delete(0, tk.END)
    summary_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    nb_pages_entry.delete(0, tk.END)
    rating_entry.delete(0, tk.END)
    author_name_entry.delete(0, tk.END)
    author_lastname_entry.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("Bookshelf Database")

# Create and place input fields and labels
tk.Label(app, text="Title:").grid(row=0, column=0)
title_entry = tk.Entry(app)
title_entry.grid(row=0, column=1)

tk.Label(app, text="Summary:").grid(row=1, column=0)
summary_entry = tk.Entry(app)
summary_entry.grid(row=1, column=1)

tk.Label(app, text="Category:").grid(row=2, column=0)
category_entry = tk.Entry(app)
category_entry.grid(row=2, column=1)

tk.Label(app, text="Number of Pages:").grid(row=3, column=0)
nb_pages_entry = tk.Entry(app)
nb_pages_entry.grid(row=3, column=1)

tk.Label(app, text="Rating (1-5):").grid(row=4, column=0)
rating_entry = tk.Entry(app)
rating_entry.grid(row=4, column=1)

tk.Label(app, text="Author Name:").grid(row=5, column=0)
author_name_entry = tk.Entry(app)
author_name_entry.grid(row=5, column=1)

tk.Label(app, text="Author Lastname:").grid(row=6, column=0)
author_lastname_entry = tk.Entry(app)
author_lastname_entry.grid(row=6, column=1)

# Create and place the "Insert" button
insert_button = tk.Button(app, text="Insert Book", command=insert_book)
insert_button.grid(row=7, column=0, columnspan=2)

# Start the Tkinter main loop
app.mainloop()

# Close the database connection when the application is closed
conn.close()
