
import tkinter
from tkinter import ttk
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    def __init__(self, db):
        super().__init__()
        self.db = db

        # Define window
        self.geometry("1100x580")
        self.title("Helio System")

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_input_dialog_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.label_top = customtkinter.CTkLabel(self, text= "Ultimos Voos", width=800, height=20)
        self.label_top.grid(row=0, column=2, padx=(20, 0), pady=(5, 0))
        self.label_top = customtkinter.CTkLabel(self, text= "APARECE AQUI", width=800, height=20)
        self.label_top.grid(row=1, column=2, padx=(20, 0), pady=(5, 0))

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=800)
        self.tabview.grid(row=2, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Pilots")
        self.tabview.add("Helicopters")
        self.tabview.add("Cities")
        self.tabview.add("Reservations")        
        self.tabview.tab("Pilots").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Helicopters").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Cities").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Reservations").grid_columnconfigure(0, weight=1)

        self.table = ttk.Treeview(self.tabview.tab("Pilots"), columns=('Name', 'CPF', 'CR','ToF','Age'), show = 'headings')
        self.table.heading('Name', text = 'Name')
        self.table.column("Name",minwidth=100, width=150)
        self.table.heading('CPF', text = 'CPF')
        self.table.column("CPF",minwidth=50, width=100)
        self.table.heading('CR', text = 'CR')
        self.table.column("CR",minwidth=50, width=100)
        self.table.heading('ToF', text = 'Tof')
        self.table.column("ToF",minwidth=50, width=100)
        self.table.heading('Age', text = 'Age')
        self.table.column("Age",minwidth=50, width=100)

        self.valores = ('José','12512124124','2.032141','1542','34')
        self.table.insert(parent='', index=0, values=self.valores)
        self.table.insert(parent='', index=0, values=self.valores)
        self.table.insert(parent='', index=0, values=self.valores)
        self.table.insert(parent='', index=0, values=self.valores)
        self.table.insert(parent='', index=0, values=self.valores)
        self.table.insert(parent='', index=0, values=self.valores)

        self.table.grid(row=0, column=0, padx=20, pady=(0, 0))



        self.table.bind('<<TreeviewSelect>>', self.item_select)

        '''
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Pilots"), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Pilots"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Pilots"), text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
'''

        

    def item_select(self, event):
        #print(self.table.selection())
        for i in self.table.selection():
            print(self.table.item(i)['values'])

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Insert a pilot   ")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        

        print("sidebar_button click")

if __name__ == "__main__":
    app = App()
    app.mainloop()


#app = App()