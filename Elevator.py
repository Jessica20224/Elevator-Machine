import tkinter as tk
import time
from tkinter import messagebox

class Elevator:
    def __init__(self, canvas, name, color, min_floor, max_floor, x_pos):
        self.canvas = canvas
        self.name = name
        self.color = color
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.x_pos = x_pos
        self.current_floor = 0  # Starting at G floor
        self.door_open = False
        self.moving = False

        # Create elevator shaft (adjusted to remove extra space at top)
        self.shaft = self.canvas.create_rectangle(
            x_pos-30, 30, x_pos+30, 580,  # Reduced height to exactly fit 10 floors
            outline="gray", fill="lightgray", width=2
        )

        # Create elevator car (starting at G floor)
        self.car = self.canvas.create_rectangle(
            x_pos-25, 550, x_pos+25, 500,  # G floor position
            outline="black", fill=color, width=2
        )

        # Create elevator doors
        self.door_left = self.canvas.create_rectangle(
            x_pos-25, 550, x_pos-5, 500, 
            outline="black", fill="white", width=2
        )
        self.door_right = self.canvas.create_rectangle(
            x_pos+5, 550, x_pos+25, 500, 
            outline="black", fill="white", width=2
        )

        # Add elevator name label
        self.label = self.canvas.create_text(
            x_pos, 525, text=name, font=("Arial", 10, "bold")
        )
    
    def move_to_floor(self, target_floor):
        if self.moving:
            return False
            
        if target_floor < self.min_floor or target_floor > self.max_floor:
            error_msg = f"{self.name} cannot go to floor {format_floor(target_floor)}"
            log(error_msg)
            messagebox.showerror("Invalid Floor", error_msg)
            return False
            
        if target_floor == self.current_floor:
            log(f"{self.name} is already on floor {format_floor(self.current_floor)}")
            return True
            
        self.moving = True
        self.close_doors()
        
        direction = 1 if target_floor > self.current_floor else -1
        
        log(f"{self.name} moving from {format_floor(self.current_floor)} to {format_floor(target_floor)}")
        
        for floor in range(self.current_floor, target_floor + direction, direction):
            self.current_floor = floor
            y_pos = 550 - floor * 50  # Adjusted calculation for exact floor positions
            self.canvas.coords(self.car, self.x_pos-25, y_pos+50, self.x_pos+25, y_pos)
            self.canvas.coords(self.door_left, self.x_pos-25, y_pos+50, self.x_pos-5, y_pos)
            self.canvas.coords(self.door_right, self.x_pos+5, y_pos+50, self.x_pos+25, y_pos)
            self.canvas.coords(self.label, self.x_pos, y_pos+25)
            self.canvas.update()
            time.sleep(0.2)
        
        self.open_doors()
        log(f"{self.name} arrived at floor {format_floor(self.current_floor)}")
        self.moving = False
        return True
    
    def open_doors(self):
        if self.door_open or self.moving:
            return
            
        left_door_x = self.x_pos-25
        right_door_x = self.x_pos+25
        
        for i in range(5):
            left_door_x += 2
            right_door_x -= 2
            y_pos = 550 - self.current_floor * 50
            self.canvas.coords(self.door_left, self.x_pos-25, y_pos+50, left_door_x, y_pos)
            self.canvas.coords(self.door_right, right_door_x, y_pos+50, self.x_pos+25, y_pos)
            self.canvas.update()
            time.sleep(0.08)
        
        self.door_open = True
    
    def close_doors(self):
        if not self.door_open:
            return
            
        left_door_x = self.x_pos-15
        right_door_x = self.x_pos+15
        
        for i in range(5):
            left_door_x -= 2
            right_door_x += 2
            y_pos = 550 - self.current_floor * 50
            self.canvas.coords(self.door_left, self.x_pos-25, y_pos+50, left_door_x, y_pos)
            self.canvas.coords(self.door_right, right_door_x, y_pos+50, self.x_pos+25, y_pos)
            self.canvas.update()
            time.sleep(0.08)
        
        self.door_open = False

def format_floor(floor):
    return "G" if floor == 0 else str(floor)

def log(message):
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)

def call_elevator(floor, elevator_index=None):
    if elevator_index is not None:
        elevator = elevators[elevator_index]
        if floor < elevator.min_floor or floor > elevator.max_floor:
            error_msg = f"⚠ Error: {elevator.name} does not serve floor {format_floor(floor)}."
            log(error_msg)
            messagebox.showerror("Invalid Floor", error_msg)
            error_label.config(text=error_msg)
        else:
            error_label.config(text="")
            elevator.move_to_floor(floor)
    else:
        if floor <= 5:
            elevators[0].move_to_floor(floor)
        elif floor <= 8:
            elevators[1].move_to_floor(floor)
        else:
            elevators[2].move_to_floor(floor)

def demo_sequence():
    elevators[0].move_to_floor(3)
    time.sleep(0.5)
    elevators[0].move_to_floor(5)
    time.sleep(0.5)
    elevators[0].move_to_floor(0)
    time.sleep(0.5)
    
    elevators[1].move_to_floor(6)
    time.sleep(0.5)
    elevators[1].move_to_floor(8)
    time.sleep(0.5)
    elevators[1].move_to_floor(0)
    time.sleep(0.5)
    
    elevators[2].move_to_floor(9)
    time.sleep(0.5)
    elevators[2].move_to_floor(10)
    time.sleep(0.5)
    elevators[2].move_to_floor(0)

# Create main window
root = tk.Tk()
root.title("Elevator Simulation - Clean Layout")
root.geometry("1000x650")

# Main frame for all content
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Left panel - Controls only
left_frame = tk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

# Control panel
control_frame = tk.Frame(left_frame)
control_frame.pack(pady=10)

error_label = tk.Label(control_frame, text="", fg="red", font=("Arial", 9))
error_label.pack(pady=(0, 5))

tk.Label(control_frame, text="Call Elevator", font=("Arial", 10, "bold")).pack()

# Floor selection buttons
for floor in range(11):
    floor_text = "G" if floor == 0 else str(floor)
    btn_row = tk.Frame(control_frame)
    btn_row.pack(pady=1)
    
    tk.Label(btn_row, text=f"{floor_text}:", width=3, anchor="e").pack(side=tk.LEFT)
    
    if floor <= 5:
        tk.Button(
            btn_row, text="A", width=2, bg="lightblue",
            command=lambda f=floor: call_elevator(f, 0)
        ).pack(side=tk.LEFT, padx=1)
    if floor <= 8:
        tk.Button(
            btn_row, text="B", width=2, bg="lightgreen",
            command=lambda f=floor: call_elevator(f, 1)
        ).pack(side=tk.LEFT, padx=1)
    if floor <= 10:
        tk.Button(
            btn_row, text="C", width=2, bg="lightcoral",
            command=lambda f=floor: call_elevator(f, 2)
        ).pack(side=tk.LEFT, padx=1)

# Demo button
tk.Button(
    control_frame, text="Run Demo", font=("Arial", 10),
    command=demo_sequence
).pack(pady=10)

# Center panel - Elevators with floor labels
center_frame = tk.Frame(main_frame)
center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create canvas for visualization (adjusted height)
canvas = tk.Canvas(center_frame, width=500, height=580, bg="white")
canvas.pack()

# Add floor labels on the left side (ascending from bottom)
for floor in range(11):
    y_pos = 550 - floor * 50
    canvas.create_text(
        30, y_pos+25, 
        text=format_floor(floor), 
        font=("Arial", 10), 
        anchor="e"
    )

# Create three elevators (Doors A, B, C)
elevators = [
    Elevator(canvas, "Door A", "lightblue", 0, 5, 100),
    Elevator(canvas, "Door B", "lightgreen", 0, 8, 250),
    Elevator(canvas, "Door C", "lightcoral", 0, 10, 400)
]

# Right panel - Activity log
right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

tk.Label(right_frame, text="Activity Log", font=("Arial", 10, "bold")).pack()

log_text = tk.Text(right_frame, height=30, width=30, font=("Arial", 9))
log_text.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(right_frame, command=log_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_text.config(yscrollcommand=scrollbar.set)

log("System initialized. All doors at Ground Floor.")

root.mainloop()