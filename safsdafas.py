import tkinter as tk
from tkinter import messagebox

# Dummy function to perform search
def search(query):
    # Placeholder for actual search functionality
    results = [
        {"title": "Example Search Result 1", "url": "https://example.com"},
        {"title": "Example Search Result 2", "url": "https://example.org"},
    ]
    return results

# Function to handle search button click event
def search_button_clicked():
    query = search_entry.get()
    if query:
        results = search(query)
        display_results(results)
    else:
        messagebox.showwarning("Warning", "Please enter a search query.")

# Function to display search results
def display_results(results):
    results_text.config(state=tk.NORMAL)
    results_text.delete(1.0, tk.END)
    for result in results:
        title = result["title"]
        url = result["url"]
        results_text.insert(tk.END, f"{title}: {url}\n")
    results_text.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("HackNet Search")

# Create widgets
search_label = tk.Label(root, text="Enter your query:")
search_entry = tk.Entry(root, width=50)
search_button = tk.Button(root, text="Search", command=search_button_clicked)
results_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
results_text.config(state=tk.DISABLED)

# Arrange widgets using grid layout
search_label.grid(row=0, column=0, padx=10, pady=10)
search_entry.grid(row=0, column=1, padx=10, pady=10)
search_button.grid(row=0, column=2, padx=10, pady=10)
results_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Run the application
root.mainloop()

