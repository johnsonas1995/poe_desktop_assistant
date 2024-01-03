from tkinter import Tk, ttk
from api_mod import APIs

class App:
    def __init__(self, root: Tk):
        self.root = root
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=15, expand=True)
        self.live_tab = ttk.Frame(self.notebook, width=400, height=280)
        self.live_tab.pack(fill="both", expand=True)
        self.categories_tab = ttk.Frame(self.notebook, width=400, height=280)
        self.categories_tab.pack(fill="both", expand=True)
        self.notebook.add(self.live_tab, text="Live Browser")
        self.notebook.add(self.categories_tab, text="Categories")
        self.league = "Hardcore Affliction"
        self.tab_index = 0
        #Live Browser
        self.get_tabs_btn = ttk.Button(
            self.live_tab,
            text="Get Tabs",
            command=lambda : APIs(self).getStashTabs(self.league, self.tab_index)
        ).pack()

        #Categories
        
        