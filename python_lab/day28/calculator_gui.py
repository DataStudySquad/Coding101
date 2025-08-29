#!/usr/bin/env python3
"""
Day 28: Advanced Calculator GUI Application
A comprehensive tkinter application demonstrating professional GUI programming

This program showcases:
- Complete GUI application architecture using tkinter
- Professional interface design with proper layout management
- Event-driven programming with mouse and keyboard input
- Object-oriented GUI design patterns
- Error handling and user feedback in GUI applications
- Advanced features like memory operations and history
- Menu systems and keyboard shortcuts

Think of this as a complete desktop application built with Python!
"""

import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import math
import json
from datetime import datetime


class AdvancedCalculator:
    """
    A comprehensive calculator application demonstrating professional GUI programming
    Like building a complete desktop application with Python
    """
    
    def __init__(self):
        """
        Initialize the calculator application
        """
        self.root = tk.Tk()
        self.setup_window()
        self.setup_variables()
        self.create_widgets()
        self.setup_keyboard_bindings()
        self.create_themes()
        
        print("🧮 Advanced Calculator GUI initialized!")
        print("📱 Features: Basic arithmetic, scientific functions, memory, history")
        print("⌨️ Keyboard shortcuts enabled!")
    
    def setup_window(self):
        """
        Configure the main application window
        """
        self.root.title("Advanced Calculator - Python GUI Demo")
        self.root.geometry("420x700")
        self.root.resizable(False, False)
        
        # Set window icon and styling
        self.root.configure(bg="#2c3e50")
        
        # Center window on screen
        self.center_window()
        
        # Handle window closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def center_window(self):
        """
        Center the window on the screen
        """
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (self.root.winfo_width() // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.root.winfo_height() // 2)
        self.root.geometry(f"+{x}+{y}")
    
    def setup_variables(self):
        """
        Initialize calculator state variables
        """
        self.current_expression = ""
        self.display_var = tk.StringVar(value="0")
        self.expression_var = tk.StringVar(value="")
        
        # Calculator state
        self.memory_value = 0
        self.last_operation = None
        self.result_displayed = False
        
        # History and settings
        self.calculation_history = []
        self.angle_mode = "deg"  # "deg" or "rad"
        self.current_theme = "dark"
        
        # Constants for special operations
        self.constants = {
            'π': math.pi,
            'e': math.e
        }
    
    def create_widgets(self):
        """
        Create all GUI components
        """
        # Create main container
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create components
        self.create_menu_bar()
        self.create_display_area(main_frame)
        self.create_info_panel(main_frame)
        self.create_button_panel(main_frame)
        self.create_status_bar()
    
    def create_menu_bar(self):
        """
        Create application menu bar
        """
        menubar = tk.Menu(self.root, bg="#34495e", fg="white")
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0, bg="#34495e", fg="white")
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save History", command=self.save_history)
        file_menu.add_command(label="Load History", command=self.load_history)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0, bg="#34495e", fg="white")
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Copy Result", command=self.copy_result)
        edit_menu.add_command(label="Clear All", command=self.clear_all)
        edit_menu.add_separator()
        edit_menu.add_command(label="Settings", command=self.show_settings)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0, bg="#34495e", fg="white")
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="History", command=self.show_history_window)
        view_menu.add_command(label="Memory", command=self.show_memory_window)
        view_menu.add_separator()
        view_menu.add_command(label="Toggle Theme", command=self.toggle_theme)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0, bg="#34495e", fg="white")
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Unit Converter", command=self.show_unit_converter)
        tools_menu.add_command(label="Angle Mode", command=self.toggle_angle_mode)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0, bg="#34495e", fg="white")
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Keyboard Shortcuts", command=self.show_shortcuts)
        help_menu.add_command(label="About", command=self.show_about)
    
    def create_display_area(self, parent):
        """
        Create the calculator display section
        """
        display_frame = tk.Frame(parent, bg="#34495e", relief=tk.RAISED, bd=3)
        display_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Expression display (shows current calculation)
        expression_label = tk.Label(display_frame,
                                  textvariable=self.expression_var,
                                  font=("Consolas", 12),
                                  fg="#7f8c8d",
                                  bg="#34495e",
                                  anchor="e",
                                  height=2)
        expression_label.pack(fill=tk.X, padx=15, pady=(10, 5))
        
        # Main result display
        self.display_entry = tk.Entry(display_frame,
                                     textvariable=self.display_var,
                                     font=("Consolas", 28, "bold"),
                                     justify=tk.RIGHT,
                                     state="readonly",
                                     bg="#ecf0f1",
                                     fg="#2c3e50",
                                     relief=tk.FLAT,
                                     bd=10,
                                     readonlybackground="#ecf0f1")
        self.display_entry.pack(fill=tk.X, padx=15, pady=(5, 15))
    
    def create_info_panel(self, parent):
        """
        Create information panel showing mode and memory status
        """
        info_frame = tk.Frame(parent, bg="#2c3e50")
        info_frame.pack(fill=tk.X, pady=(0, 5))
        
        # Mode indicator
        self.mode_var = tk.StringVar(value=f"Mode: {self.angle_mode.upper()}")
        mode_label = tk.Label(info_frame,
                             textvariable=self.mode_var,
                             font=("Arial", 10),
                             fg="#95a5a6",
                             bg="#2c3e50")
        mode_label.pack(side=tk.LEFT)
        
        # Memory indicator
        self.memory_var = tk.StringVar(value="M: 0")
        memory_label = tk.Label(info_frame,
                               textvariable=self.memory_var,
                               font=("Arial", 10),
                               fg="#95a5a6",
                               bg="#2c3e50")
        memory_label.pack(side=tk.RIGHT)
    
    def create_button_panel(self, parent):
        """
        Create the calculator button interface
        """
        button_frame = tk.Frame(parent, bg="#2c3e50")
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # Button configuration
        btn_config = {
            'font': ("Arial", 12, "bold"),
            'relief': tk.RAISED,
            'bd': 2,
            'width': 8,
            'height': 2
        }
        
        # Define button layout with colors and commands
        self.buttons = [
            # Row 0 - Memory operations
            [("MC", self.memory_clear, "#e74c3c", "white"), 
             ("MR", self.memory_recall, "#e74c3c", "white"),
             ("M+", self.memory_add, "#e74c3c", "white"), 
             ("M-", self.memory_subtract, "#e74c3c", "white")],
            
            # Row 1 - Scientific functions
            [("sin", lambda: self.apply_function("sin"), "#9b59b6", "white"),
             ("cos", lambda: self.apply_function("cos"), "#9b59b6", "white"),
             ("tan", lambda: self.apply_function("tan"), "#9b59b6", "white"),
             ("π", lambda: self.insert_constant("π"), "#9b59b6", "white")],
            
            # Row 2 - More functions
            [("√", lambda: self.apply_function("sqrt"), "#9b59b6", "white"),
             ("x²", lambda: self.apply_function("square"), "#9b59b6", "white"),
             ("1/x", lambda: self.apply_function("reciprocal"), "#9b59b6", "white"),
             ("log", lambda: self.apply_function("log"), "#9b59b6", "white")],
            
            # Row 3 - Clear and backspace
            [("C", self.clear_all, "#e74c3c", "white"),
             ("CE", self.clear_entry, "#e74c3c", "white"),
             ("⌫", self.backspace, "#e74c3c", "white"),
             ("/", lambda: self.add_operator("/"), "#f39c12", "white")],
            
            # Row 4-6 - Number pad and basic operations
            [("7", lambda: self.add_digit("7"), "#3498db", "white"),
             ("8", lambda: self.add_digit("8"), "#3498db", "white"),
             ("9", lambda: self.add_digit("9"), "#3498db", "white"),
             ("*", lambda: self.add_operator("*"), "#f39c12", "white")],
            
            [("4", lambda: self.add_digit("4"), "#3498db", "white"),
             ("5", lambda: self.add_digit("5"), "#3498db", "white"),
             ("6", lambda: self.add_digit("6"), "#3498db", "white"),
             ("-", lambda: self.add_operator("-"), "#f39c12", "white")],
            
            [("1", lambda: self.add_digit("1"), "#3498db", "white"),
             ("2", lambda: self.add_digit("2"), "#3498db", "white"),
             ("3", lambda: self.add_digit("3"), "#3498db", "white"),
             ("+", lambda: self.add_operator("+"), "#f39c12", "white")],
            
            # Row 7 - Zero, decimal, and equals
            [("±", self.toggle_sign, "#3498db", "white"),
             ("0", lambda: self.add_digit("0"), "#3498db", "white"),
             (".", lambda: self.add_digit("."), "#3498db", "white"),
             ("=", self.calculate, "#27ae60", "white")]
        ]
        
        # Create button grid
        self.button_widgets = {}
        for row_idx, row in enumerate(self.buttons):
            for col_idx, (text, command, bg_color, fg_color) in enumerate(row):
                btn = tk.Button(button_frame,
                               text=text,
                               command=command,
                               bg=bg_color,
                               fg=fg_color,
                               activebackground=self.get_lighter_color(bg_color),
                               **btn_config)
                btn.grid(row=row_idx, column=col_idx, padx=2, pady=2, sticky="nsew")
                self.button_widgets[text] = btn
        
        # Configure grid weights for responsive design
        for i in range(8):  # 8 rows
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):  # 4 columns
            button_frame.grid_columnconfigure(j, weight=1)
    
    def create_status_bar(self):
        """
        Create status bar at bottom of window
        """
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(self.root,
                             textvariable=self.status_var,
                             relief=tk.SUNKEN,
                             anchor=tk.W,
                             font=("Arial", 9),
                             bg="#34495e",
                             fg="#ecf0f1")
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def create_themes(self):
        """
        Define color themes for the calculator
        """
        self.themes = {
            'dark': {
                'bg_primary': '#2c3e50',
                'bg_secondary': '#34495e',
                'fg_primary': '#ecf0f1',
                'fg_secondary': '#7f8c8d'
            },
            'light': {
                'bg_primary': '#ecf0f1',
                'bg_secondary': '#bdc3c7',
                'fg_primary': '#2c3e50',
                'fg_secondary': '#7f8c8d'
            }
        }
    
    def setup_keyboard_bindings(self):
        """
        Set up keyboard shortcuts for calculator operations
        """
        # Bind keyboard events
        self.root.bind('<Key>', self.handle_keypress)
        self.root.bind('<KeyPress-Return>', lambda e: self.calculate())
        self.root.bind('<KeyPress-Escape>', lambda e: self.clear_all())
        self.root.bind('<KeyPress-Delete>', lambda e: self.clear_entry())
        self.root.bind('<KeyPress-BackSpace>', lambda e: self.backspace())
        
        # Focus on root to capture keyboard events
        self.root.focus_set()
        self.root.focus_force()
    
    def handle_keypress(self, event):
        """
        Handle keyboard input for calculator operations
        """
        key = event.char.lower()
        keysym = event.keysym
        
        # Numbers and decimal point
        if key in '0123456789':
            self.add_digit(key)
            self.flash_button(key)
        elif key == '.':
            self.add_digit('.')
            self.flash_button('.')
        
        # Operators
        elif key in '+-*/':
            self.add_operator(key)
            self.flash_button(key)
        
        # Special functions
        elif key == '=' or keysym == 'Return':
            self.calculate()
            self.flash_button('=')
        elif key == 'c':
            self.clear_all()
            self.flash_button('C')
        elif keysym in ['Delete', 'BackSpace']:
            if keysym == 'Delete':
                self.clear_entry()
            else:
                self.backspace()
        
        # Update status
        self.status_var.set(f"Key pressed: {event.keysym}")
        self.root.after(2000, lambda: self.status_var.set("Ready"))
    
    def flash_button(self, button_text):
        """
        Visual feedback for button press
        """
        if button_text in self.button_widgets:
            btn = self.button_widgets[button_text]
            original_bg = btn['bg']
            btn.configure(bg='#ffffff')
            self.root.after(100, lambda: btn.configure(bg=original_bg))
    
    def get_lighter_color(self, color):
        """
        Generate a lighter shade of the given color for hover effects
        """
        color_variants = {
            "#3498db": "#5dade2",
            "#e74c3c": "#ec7063",
            "#f39c12": "#f7c52d",
            "#27ae60": "#52c78a",
            "#9b59b6": "#bb77d6"
        }
        return color_variants.get(color, "#95a5a6")
    
    # Calculator Logic Methods
    
    def add_digit(self, digit):
        """
        Add a digit to the current number
        """
        current = self.display_var.get()
        
        if self.result_displayed or current == "0":
            if digit == "." and current == "0":
                self.display_var.set("0.")
            elif digit != ".":
                self.display_var.set(digit)
            self.result_displayed = False
        else:
            if digit == "." and "." in current:
                return  # Don't allow multiple decimal points
            self.display_var.set(current + digit)
        
        self.update_status("Entering number...")
    
    def add_operator(self, operator):
        """
        Add an operator to the expression
        """
        current_display = self.display_var.get()
        
        if not self.current_expression:
            self.current_expression = current_display
        elif not self.result_displayed:
            # Auto-calculate if there's a pending operation
            if self.current_expression and self.current_expression[-1] not in "+-*/":
                self.current_expression += current_display
                try:
                    result = eval(self.current_expression)
                    self.display_var.set(str(self.format_result(result)))
                    self.current_expression = str(result)
                except:
                    pass
        
        # Add operator to expression
        if self.current_expression and self.current_expression[-1] in "+-*/":
            self.current_expression = self.current_expression[:-1] + operator
        else:
            self.current_expression += operator
        
        self.expression_var.set(self.current_expression)
        self.result_displayed = False
        self.update_status(f"Operation: {operator}")
    
    def calculate(self):
        """
        Perform the calculation and display result
        """
        if not self.current_expression:
            return
        
        try:
            # Add current display to expression if needed
            if not self.result_displayed and self.current_expression[-1] in "+-*/":
                self.current_expression += self.display_var.get()
            
            # Evaluate expression
            result = eval(self.current_expression)
            
            # Handle special cases
            if math.isinf(result):
                self.display_var.set("∞")
                self.update_status("Result: Infinity")
            elif math.isnan(result):
                self.display_var.set("Error")
                self.update_status("Error: Invalid operation")
            else:
                formatted_result = self.format_result(result)
                self.display_var.set(str(formatted_result))
                
                # Add to history
                history_entry = f"{self.current_expression} = {formatted_result}"
                self.add_to_history(history_entry)
                
                self.update_status(f"Calculated: {self.current_expression}")
            
            # Reset for next calculation
            self.current_expression = ""
            self.expression_var.set("")
            self.result_displayed = True
            
        except ZeroDivisionError:
            self.display_var.set("Cannot divide by zero")
            self.update_status("Error: Division by zero")
            self.reset_calculator()
        except Exception as e:
            self.display_var.set("Error")
            self.update_status(f"Error: {str(e)}")
            self.reset_calculator()
    
    def apply_function(self, function_name):
        """
        Apply mathematical functions to current value
        """
        try:
            current_val = float(self.display_var.get())
            result = None
            
            if function_name == "sqrt":
                if current_val < 0:
                    raise ValueError("Cannot take square root of negative number")
                result = math.sqrt(current_val)
                
            elif function_name == "square":
                result = current_val ** 2
                
            elif function_name == "reciprocal":
                if current_val == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = 1 / current_val
                
            elif function_name == "log":
                if current_val <= 0:
                    raise ValueError("Cannot take log of non-positive number")
                result = math.log10(current_val)
                
            elif function_name in ["sin", "cos", "tan"]:
                # Convert degrees to radians if needed
                angle = current_val
                if self.angle_mode == "deg":
                    angle = math.radians(current_val)
                
                if function_name == "sin":
                    result = math.sin(angle)
                elif function_name == "cos":
                    result = math.cos(angle)
                elif function_name == "tan":
                    result = math.tan(angle)
                
                # Handle very small numbers (essentially zero)
                if abs(result) < 1e-15:
                    result = 0
            
            if result is not None:
                formatted_result = self.format_result(result)
                self.display_var.set(str(formatted_result))
                self.result_displayed = True
                
                # Add to history
                function_display = {
                    "sqrt": "√", "square": "²", "reciprocal": "1/x",
                    "log": "log", "sin": "sin", "cos": "cos", "tan": "tan"
                }
                history_entry = f"{function_display.get(function_name, function_name)}({current_val}) = {formatted_result}"
                self.add_to_history(history_entry)
                
                self.update_status(f"Applied {function_name}")
                
        except (ValueError, ZeroDivisionError) as e:
            self.display_var.set("Error")
            self.update_status(f"Error: {str(e)}")
        except Exception as e:
            self.display_var.set("Error")
            self.update_status(f"Unexpected error: {str(e)}")
    
    def insert_constant(self, constant_name):
        """
        Insert mathematical constants
        """
        if constant_name in self.constants:
            value = self.constants[constant_name]
            formatted_value = self.format_result(value)
            self.display_var.set(str(formatted_value))
            self.result_displayed = True
            self.update_status(f"Inserted constant: {constant_name}")
    
    def format_result(self, result):
        """
        Format calculation results for display
        """
        if isinstance(result, int) or result.is_integer():
            return int(result)
        else:
            # Round to avoid floating point precision issues
            rounded = round(result, 12)
            if rounded == 0:
                return 0
            
            # Format with appropriate precision
            if abs(rounded) < 1e-6 or abs(rounded) > 1e12:
                return f"{rounded:.6e}"
            else:
                return round(rounded, 10)
    
    def clear_all(self):
        """
        Clear everything and reset calculator
        """
        self.display_var.set("0")
        self.expression_var.set("")
        self.current_expression = ""
        self.result_displayed = False
        self.update_status("Calculator cleared")
    
    def clear_entry(self):
        """
        Clear only the current entry
        """
        self.display_var.set("0")
        self.update_status("Entry cleared")
    
    def backspace(self):
        """
        Remove last character from display
        """
        current = self.display_var.get()
        if len(current) > 1 and current != "Error":
            self.display_var.set(current[:-1])
        else:
            self.display_var.set("0")
        self.update_status("Backspace")
    
    def toggle_sign(self):
        """
        Toggle the sign of current number
        """
        current = self.display_var.get()
        try:
            value = float(current)
            self.display_var.set(str(self.format_result(-value)))
            self.update_status("Sign toggled")
        except:
            pass
    
    def reset_calculator(self):
        """
        Reset calculator state after error
        """
        self.current_expression = ""
        self.expression_var.set("")
        self.result_displayed = True
    
    # Memory Operations
    
    def memory_clear(self):
        """
        Clear memory
        """
        self.memory_value = 0
        self.update_memory_display()
        self.update_status("Memory cleared")
    
    def memory_recall(self):
        """
        Recall value from memory
        """
        self.display_var.set(str(self.format_result(self.memory_value)))
        self.result_displayed = True
        self.update_status(f"Memory recalled: {self.memory_value}")
    
    def memory_add(self):
        """
        Add current value to memory
        """
        try:
            current_val = float(self.display_var.get())
            self.memory_value += current_val
            self.update_memory_display()
            self.update_status(f"Added {current_val} to memory")
        except:
            self.update_status("Error: Cannot add to memory")
    
    def memory_subtract(self):
        """
        Subtract current value from memory
        """
        try:
            current_val = float(self.display_var.get())
            self.memory_value -= current_val
            self.update_memory_display()
            self.update_status(f"Subtracted {current_val} from memory")
        except:
            self.update_status("Error: Cannot subtract from memory")
    
    def update_memory_display(self):
        """
        Update memory indicator
        """
        self.memory_var.set(f"M: {self.format_result(self.memory_value)}")
    
    # History Management
    
    def add_to_history(self, calculation):
        """
        Add calculation to history
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {calculation}"
        self.calculation_history.append(entry)
        
        # Keep only last 100 calculations
        if len(self.calculation_history) > 100:
            self.calculation_history.pop(0)
    
    def show_history_window(self):
        """
        Display calculation history in separate window
        """
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_window.geometry("500x400")
        history_window.configure(bg="#34495e")
        
        # Create scrollable text widget
        text_frame = tk.Frame(history_window, bg="#34495e")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        history_text = tk.Text(text_frame,
                              yscrollcommand=scrollbar.set,
                              font=("Consolas", 11),
                              bg="#ecf0f1",
                              fg="#2c3e50",
                              wrap=tk.WORD)
        history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=history_text.yview)
        
        # Populate history
        if self.calculation_history:
            for entry in reversed(self.calculation_history):  # Most recent first
                history_text.insert(tk.END, entry + "\n")
        else:
            history_text.insert(tk.END, "No calculations performed yet.")
        
        history_text.config(state=tk.DISABLED)
        
        # Buttons frame
        btn_frame = tk.Frame(history_window, bg="#34495e")
        btn_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        tk.Button(btn_frame, text="Clear History",
                 command=lambda: self.clear_history(history_text),
                 bg="#e74c3c", fg="white").pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="Close",
                 command=history_window.destroy,
                 bg="#95a5a6", fg="white").pack(side=tk.RIGHT, padx=5)
    
    def clear_history(self, text_widget=None):
        """
        Clear calculation history
        """
        self.calculation_history = []
        if text_widget:
            text_widget.config(state=tk.NORMAL)
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, "History cleared.")
            text_widget.config(state=tk.DISABLED)
        self.update_status("History cleared")
    
    # Utility Methods
    
    def toggle_angle_mode(self):
        """
        Switch between degrees and radians
        """
        self.angle_mode = "rad" if self.angle_mode == "deg" else "deg"
        self.mode_var.set(f"Mode: {self.angle_mode.upper()}")
        self.update_status(f"Angle mode: {self.angle_mode.upper()}")
    
    def toggle_theme(self):
        """
        Switch between light and dark themes
        """
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        self.update_status(f"Switched to {self.current_theme} theme")
        messagebox.showinfo("Theme", f"Theme changed to {self.current_theme}.\nRestart calculator to apply changes.")
    
    def update_status(self, message):
        """
        Update status bar message
        """
        self.status_var.set(message)
        # Clear status after 3 seconds
        self.root.after(3000, lambda: self.status_var.set("Ready"))
    
    def copy_result(self):
        """
        Copy current result to clipboard
        """
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.display_var.get())
            self.update_status("Result copied to clipboard")
        except:
            self.update_status("Failed to copy result")
    
    def save_history(self):
        """
        Save calculation history to file
        """
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("JSON files", "*.json")]
            )
            if filename:
                with open(filename, 'w') as f:
                    if filename.endswith('.json'):
                        json.dump(self.calculation_history, f, indent=2)
                    else:
                        for entry in self.calculation_history:
                            f.write(entry + "\n")
                self.update_status(f"History saved to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save history: {str(e)}")
    
    def load_history(self):
        """
        Load calculation history from file
        """
        try:
            filename = filedialog.askopenfilename(
                filetypes=[("Text files", "*.txt"), ("JSON files", "*.json")]
            )
            if filename:
                with open(filename, 'r') as f:
                    if filename.endswith('.json'):
                        self.calculation_history = json.load(f)
                    else:
                        self.calculation_history = [line.strip() for line in f.readlines()]
                self.update_status(f"History loaded from {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load history: {str(e)}")
    
    # Dialog Windows
    
    def show_settings(self):
        """
        Show settings dialog
        """
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("300x200")
        settings_window.configure(bg="#34495e")
        
        tk.Label(settings_window, text="Calculator Settings",
                font=("Arial", 14, "bold"), bg="#34495e", fg="white").pack(pady=10)
        
        # Angle mode setting
        tk.Label(settings_window, text="Angle Mode:",
                bg="#34495e", fg="white").pack()
        
        angle_frame = tk.Frame(settings_window, bg="#34495e")
        angle_frame.pack(pady=5)
        
        tk.Button(angle_frame, text="Degrees",
                 command=lambda: setattr(self, 'angle_mode', 'deg') or self.mode_var.set('Mode: DEG'),
                 bg="#3498db", fg="white").pack(side=tk.LEFT, padx=5)
        
        tk.Button(angle_frame, text="Radians",
                 command=lambda: setattr(self, 'angle_mode', 'rad') or self.mode_var.set('Mode: RAD'),
                 bg="#3498db", fg="white").pack(side=tk.LEFT, padx=5)
        
        tk.Button(settings_window, text="Close",
                 command=settings_window.destroy,
                 bg="#95a5a6", fg="white").pack(pady=20)
    
    def show_shortcuts(self):
        """
        Display keyboard shortcuts
        """
        shortcuts_text = """Keyboard Shortcuts:

Numbers: 0-9
Decimal: .
Operations: +, -, *, /
Calculate: Enter or =
Clear All: C or Escape
Clear Entry: Delete
Backspace: Backspace
Sign Toggle: ± button only

Memory Operations:
MC - Clear Memory
MR - Recall Memory  
M+ - Add to Memory
M- - Subtract from Memory

Scientific Functions:
Available via buttons only

Menu Operations:
File menu for save/load
View menu for history
Tools menu for settings"""
        
        messagebox.showinfo("Keyboard Shortcuts", shortcuts_text)
    
    def show_about(self):
        """
        Display about information
        """
        about_text = """Advanced Calculator v2.0

A comprehensive GUI calculator built with Python and tkinter.
Demonstrates professional GUI programming techniques.

Features:
• Basic arithmetic operations
• Scientific functions (sin, cos, tan, log, sqrt)
• Memory operations (MC, MR, M+, M-)
• Calculation history with save/load
• Keyboard shortcuts
• Multiple themes
• Error handling and validation

Built for Python Programming Tutorial - Day 28
© 2024 Educational Project

This calculator showcases:
• Object-oriented GUI design
• Event-driven programming
• Professional interface design
• File handling integration
• Error handling in GUI applications"""
        
        messagebox.showinfo("About Advanced Calculator", about_text)
    
    def show_memory_window(self):
        """
        Show memory operations window
        """
        memory_window = tk.Toplevel(self.root)
        memory_window.title("Memory Operations")
        memory_window.geometry("250x150")
        memory_window.configure(bg="#34495e")
        
        tk.Label(memory_window, text="Memory Operations",
                font=("Arial", 14, "bold"), bg="#34495e", fg="white").pack(pady=10)
        
        tk.Label(memory_window, text=f"Current Memory: {self.format_result(self.memory_value)}",
                font=("Arial", 12), bg="#34495e", fg="white").pack(pady=5)
        
        btn_frame = tk.Frame(memory_window, bg="#34495e")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Clear (MC)", command=self.memory_clear,
                 bg="#e74c3c", fg="white", width=12).pack(pady=2)
        tk.Button(btn_frame, text="Recall (MR)", command=self.memory_recall,
                 bg="#3498db", fg="white", width=12).pack(pady=2)
    
    def show_unit_converter(self):
        """
        Show simple unit converter
        """
        converter_window = tk.Toplevel(self.root)
        converter_window.title("Unit Converter")
        converter_window.geometry("300x200")
        converter_window.configure(bg="#34495e")
        
        tk.Label(converter_window, text="Simple Unit Converter",
                font=("Arial", 14, "bold"), bg="#34495e", fg="white").pack(pady=10)
        
        # Temperature converter example
        temp_frame = tk.Frame(converter_window, bg="#34495e")
        temp_frame.pack(pady=10)
        
        tk.Label(temp_frame, text="Temperature:", bg="#34495e", fg="white").pack()
        
        entry_var = tk.StringVar()
        tk.Entry(temp_frame, textvariable=entry_var, width=20).pack(pady=5)
        
        result_var = tk.StringVar(value="Enter temperature in Celsius")
        result_label = tk.Label(temp_frame, textvariable=result_var,
                               bg="#34495e", fg="white", wraplength=250)
        result_label.pack(pady=5)
        
        def convert_temp():
            try:
                celsius = float(entry_var.get())
                fahrenheit = (celsius * 9/5) + 32
                kelvin = celsius + 273.15
                result_var.set(f"{celsius}°C = {fahrenheit:.1f}°F = {kelvin:.1f}K")
            except ValueError:
                result_var.set("Please enter a valid number")
        
        tk.Button(temp_frame, text="Convert", command=convert_temp,
                 bg="#27ae60", fg="white").pack(pady=5)
        
        tk.Button(converter_window, text="Close",
                 command=converter_window.destroy,
                 bg="#95a5a6", fg="white").pack(pady=10)
    
    def on_closing(self):
        """
        Handle application closing
        """
        if messagebox.askokcancel("Quit", "Do you want to quit the calculator?"):
            self.root.quit()
            self.root.destroy()
    
    def run(self):
        """
        Start the calculator application
        """
        print("🚀 Starting Advanced Calculator GUI...")
        print("✨ Ready for calculations!")
        self.root.mainloop()


def main():
    """
    Main function to run the calculator application
    """
    print("🧮" * 20)
    print("    ADVANCED CALCULATOR GUI APPLICATION")
    print("🧮" * 20)
    print("Professional GUI programming demonstration with tkinter")
    print()
    
    try:
        calculator = AdvancedCalculator()
        calculator.run()
    except KeyboardInterrupt:
        print("\n👋 Calculator closed by user")
    except Exception as e:
        print(f"❌ Error running calculator: {e}")
    finally:
        print("📱 Thank you for using the Advanced Calculator!")
        print("💡 This demonstrates professional GUI development with Python!")


if __name__ == "__main__":
    main()