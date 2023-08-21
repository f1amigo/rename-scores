import tkinter as tk
import tkinter.ttk as ttk
import util

class App(tk.Tk):
    def __init__(self, **args):
        super().__init__()
        self.shared = {**args}

        # Create a container to switch the frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Iterate through frames to switch the view to different frames
        # self.frames = {}
        # for F in (Gui):
        #     frame = F(container, self)
        #     self.frames[F] = frame

        #     frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame(Gui)

        frame = Gui(container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()    

    def show_frame(self, page):
        """
        Display the current frame

        Args:
            page (str): name of the frame to be displayed
        """
        frame = self.frames[page]
        frame.tkraise()       


class Gui(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.scrollFrame = ScrollFrame(self)
        self.parent = parent
        self.controller = controller
        self.checkboxes = None
        self.vars = []
        self.selected_vars = []

        self.create_page()
        self.scrollFrame.pack(side="top", fill="both", expand=True)

    def create_page(self):
        ttk.Label(
            self.scrollFrame.viewPort,
            text="Select the parts that appeared in the piece.",
            font=("Arial", 20)
        ).pack(padx=5, pady=5)

        checkbox_frame = tk.Frame(self.scrollFrame.viewPort)
        self.checkboxes = self.create_checkboxes(checkbox_frame)
        checkbox_frame.pack(padx=10, pady=10)

        # Button to confirm
        btn_done = ttk.Button(
            self.scrollFrame.viewPort,
            text="Done",
            width=15,
            cursor="hand2"
        )

        btn_done.pack(side=tk.RIGHT, padx=50, pady=20)
        btn_done.bind("<Button-1>", self.done_btn_clicked)
    
    def done_btn_clicked(self, event):
        util.run(self.controller.shared.get("folder"), "piece_title", self.vars)
        self.master.quit()

    def create_checkboxes(self, frame):
        """
        Create a radio button for each header that is to be displayed.

        Args:
            frame (tk.Frame): the frame that the buttons will be under
            selected (str): the value of the radio button that is been clicked on
            selected_value (str): shared value that stores the selected value
            headers (list): list of header names to be displayed
        
        """

        checkboxes = {}

        # Extract part names
        part_names = util.extract_part_names("part_names.txt")
        col = 0
        r = 0

        for _ in part_names:
            if _ == "":
                r = 0
                col += 1
            else:
                # Create and pack the radio buttons
                var = tk.StringVar()
                checkbox = ttk.Checkbutton(
                    frame,
                    text=_,
                    command=check_changed,
                    variable=var
                )

                checkbox.grid(row=r, column=col, padx=2, pady=10)
                checkboxes[_] = checkbox
                self.vars.append(var)
                r += 1
        
        return checkboxes

    def check_changed(self, var):
        if int(var.get()):
            self.selected_vars.append(var.get())
        else:
            self.selected_vars.remove(var.get())
        


class ScrollFrame(tk.Frame):
    """
        Scrollable frame that enables mousewheel support
    """
    def __init__(self, parent):
        super().__init__(parent)

        # Place a canvas and binds a scrollbar to it
        self.canvas = tk.Canvas(self, borderwidth=0)
        self.viewPort = tk.Frame(self.canvas)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        # Pack the scrollbar to the right of the canvas
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_window = self.canvas.create_window((4,4), window=self.viewPort, anchor="nw", tags="self.viewPort")

        # Bind an event to resize the canvas and view port
        self.viewPort.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind("<Configure>", self.onCanvasConfigure)
            
        # Bind mouse wheel to scroll the view port
        self.viewPort.bind('<Enter>', self.onEnter)
        self.viewPort.bind('<Leave>', self.onLeave)

        # Perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize
        self.onFrameConfigure(None)
    
    def onFrameConfigure(self, event):   
        """
        Reset the scroll region to encompass the inner frame
        
        Args:
            event (mouse_event): unused
        """


        # Whenever the size of the frame changes, alter the scroll region respectively
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def onCanvasConfigure(self, event):
        """
        Resets the canvas window to encompass inner frame when required

        Args:
            event (mouse_event): unused
        """
        ''''''
        canvas_width = event.width

        # Whenever the size of the canvas changes, alter the window region respectively
        self.canvas.itemconfig(self.canvas_window, width = canvas_width)

    def onMouseWheel(self, event):
        self.canvas.yview_scroll(int(-1* (event.delta/120)), "units")
    
    def onEnter(self, event):
        """
        Binds wheel events when the cursor enters control

        Args:
            event (mouse_event): mouse event when entering control
        """
        self.canvas.bind_all("<MouseWheel>", self.onMouseWheel)

    def onLeave(self, event):
        """
        Unbinds wheel events when the cursor leaves control

        Args:
            event (mouse_event): mouse event when exiting control
        """
        self.canvas.unbind_all("<MouseWheel>")
