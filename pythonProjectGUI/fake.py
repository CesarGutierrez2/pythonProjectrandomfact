import tkinter as tk

class StarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hollywood Walk of Fame Star")
        self.star_color = "gold"
        self.text_color = "black"

        # Create a canvas
        self.canvas = tk.Canvas(self.master, width=200, height=200, bg=self.star_color)
        self.canvas.pack()

        # Draw a star on the canvas
        self.draw_star()

        # Create a button to invert colors
        self.button = tk.Button(self.master, text="Invert Colors", command=self.invert_colors)
        self.button.pack()

        # Create a label with your name
        self.name_label = tk.Label(self.master, text="ChatGPT", fg=self.text_color, font=("Arial", 12, "bold"))
        self.name_label.pack()

    def draw_star(self):
        # Coordinates for a star
        star_coords = [100, 10, 130, 80, 200, 80, 145, 120, 160, 190, 100, 150, 40, 190, 55, 120, 0, 80, 70, 80]

        # Draw the star on the canvas
        self.canvas.create_polygon(star_coords, fill=self.star_color, outline="black")

    def invert_colors(self):
        # Invert star and text colors
        self.star_color, self.text_color = self.text_color, self.star_color

        # Update canvas background color
        self.canvas.config(bg=self.star_color)

        # Update text color
        self.name_label.config(fg=self.text_color)

# Create the main window
root = tk.Tk()

# Create an instance of the StarApp class
app = StarApp(root)

# Run the Tkinter event loop
root.mainloop()
