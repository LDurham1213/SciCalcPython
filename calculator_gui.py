import tkinter as tk
from tkinter import messagebox
from sciCalc import SciCalc

class CalculatorGUI:
    def __init__(self):
        self.calc = SciCalc()

        #Values used for two-number operations
        self.first_number = None
        self.pending_operation = None
        self.start_new_number = True

        #Main window.
        self.window = tk.Tk()
        self.window.title("Python Scientific Calculator")
        self.window.geometry("620x720")
        self.window.resizable(False, False)

        # Value shown on the GUI display. 
        self.display_text = tk.StringVar(value="0")

        self.create_display()
        self.create_mode_label()
        self.create_buttons()

    # ------------------------------
    # GUI SETUP
    # ------------------------------

    def create_display(self):
        self.display = tk.Entry(
            self.window, textvariable=self.display_text,
            font=("Arial", 30),
            justify="right",
            state="readonly",
            readonlybackground="white",
            borderwidth=6
        )

        self.display.grid(
            row=0,
            column=0
            columnspan=6,
            padx=12,
            pady=(12,5),
            sticky="nsew"
        )
        
        def create_mode_label(self):
            self.mode_text = tk.StringVar(
                value=f"Trig Mode: {self.calc.getTrigMode()}"
            )

            mode_label = tk.Label(
                self.window,
                textvariable=self.mode_text,
                font=("Arial", 12)
            )