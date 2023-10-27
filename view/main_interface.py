
from tkinter import *
from tkinter import ttk
import customtkinter
import difflib
from CTkMessagebox import CTkMessagebox

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

pilot_id = None
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
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text= "Update Tables", command=self.update_all_table)
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
        self.tabview.add("Destinations")
        self.tabview.add("Reservations")        
        self.tabview.tab("Pilots").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Helicopters").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Destinations").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Reservations").grid_columnconfigure(0, weight=1)

        # Create automatically all tables
        self.create_all_tables()

    def create_all_tables(self):
        self.create_pilots_table()
        self.update_pilots_table()
        self.create_helicopters_table()
        self.update_helicopters_table()
        self.create_destinations_table()
        self.update_destinations_table()
        self.create_reservations_table()
        self.update_reservations_table()

    def create_pilots_table(self):
        column_list = ["Name", "CPF", "CR", "ToF", "Age"]

        self.pilots_table = ttk.Treeview(self.tabview.tab("Pilots"), columns=column_list, show = 'headings',selectmode='browse')

        for i in column_list:
            self.pilots_table.heading(i, text = i)
            self.pilots_table.column(i,minwidth=100, width=150)

        self.pilots_table.grid(row=0, column=0, padx=20, pady=(0, 0))

        #self.pilots_table.bind('<<TreeviewSelect>>', self.pilots_item_select)
        self.pilots_table.bind('<Double-1>', self.pilots_open_edit)

        

    def update_pilots_table(self):
        self.pilots_table.delete(*self.pilots_table.get_children())
        all_results = self.db.get_all_generic("pilots")
        values = {}
        for i in all_results:
            values = (
                i['name'],
                i['cpf'],
                i['commission_rate'],
                i['total_flight_hours'],
                i['age'],
            )
            self.pilots_table.insert(parent='', index=0, values=values)

    def create_helicopters_table(self):
        column_list = ["Serial", "Current City", "Flight Hours", "Age"]

        self.helicopters_table = ttk.Treeview(self.tabview.tab("Helicopters"), columns=column_list, show = 'headings')
        
        for i in column_list:
            self.helicopters_table.heading(i, text = i)
            self.helicopters_table.column(i,minwidth=100, width=150)

        self.helicopters_table.grid(row=0, column=0, padx=20, pady=(0, 0))
        self.helicopters_table.bind('<<TreeviewSelect>>', self.helicopters_item_select)

    def update_helicopters_table(self):
        all_results = self.db.get_all_generic("helicopters")
        values = {}
        for i in all_results:
            values = (
                i['serial'],
                i['current_city'],
                i['flight_hours'],
                i['age'],
            )
            self.helicopters_table.insert(parent='', index=0, values=values)

    def create_destinations_table(self):
        column_list = ["Code", "City", "Distance", "Open"]

        self.destinations_table = ttk.Treeview(self.tabview.tab("Destinations"), columns=column_list, show = 'headings')
        
        for i in column_list:
            self.destinations_table.heading(i, text = i)
            self.destinations_table.column(i,minwidth=100, width=150)

        self.destinations_table.grid(row=0, column=0, padx=20, pady=(0, 0))
        self.destinations_table.bind('<<TreeviewSelect>>', self.destinations_item_select)

    def update_destinations_table(self):
        all_results = self.db.get_all_generic("destinations")
        values = {}
        for i in all_results:
            values = (
                i['code'],
                i['city'],
                i['distance'],
                i['is_open'],
            )
            self.destinations_table.insert(parent='', index=0, values=values)

    def create_reservations_table(self):
        column_list = ["Reservation ID", "Destination", "Date", "Time", "Helicopter Serial"]

        self.reservations_table = ttk.Treeview(self.tabview.tab("Reservations"), columns=column_list, show = 'headings')
        
        for i in column_list:
            self.reservations_table.heading(i, text = i)
            self.reservations_table.column(i,minwidth=100, width=150)

        self.reservations_table.grid(row=0, column=0, padx=20, pady=(0, 0))
        self.reservations_table.bind('<<TreeviewSelect>>', self.reservations_item_select)

    def update_reservations_table(self):
        all_results = self.db.get_all_generic("reservations")
        values = {}
        for i in all_results:
            values = (
                i['reservation_id'],
                f"({i['destination']}) - {self.db.return_destination_city(i['destination'])}",
                i['date'],
                i['time'],
                i['helicopter_serial']
            )
            self.reservations_table.insert(parent='', index=0, values=values)

    def pilots_item_select(self, event):
        for i in self.pilots_table.selection():
            print(self.pilots_table.item(i)['values'])

    def helicopters_item_select(self, event):
        for i in self.helicopters_table.selection():
            print(self.helicopters_table.item(i)['values'])

    def destinations_item_select(self, event):
        for i in self.destinations_table.selection():
            print(self.destinations_table.item(i)['values'])
    
    def reservations_item_select(self, event):
        for i in self.reservations_table.selection():
            print(self.reservations_table.item(i)['values'])

    def pilots_open_edit(self, event):
        global pilot_id
        dict_info = []
        for i in self.pilots_table.selection():
            dict_info = self.pilots_table.item(i)['values']

        pilot_data = self.db.get_pilot_by_cpf(str(dict_info[1]))
        pilot_id = pilot_data['_id']
        #print(pilot_id)

        # creates a pop-up editor
        self.pop_up = Toplevel(self)
        self.pop_up.title("Edit Pilot")
        self.pop_up.grab_set()
        self.pop_up.geometry("600x400")
            
        self.pop_up.label_nome_pilot = customtkinter.CTkLabel(self.pop_up, text="Name",width=200, height=20)
        self.pop_up.label_cpf_pilot = customtkinter.CTkLabel(self.pop_up, text="CPF",width=200, height=20)
        self.pop_up.label_com_pilot = customtkinter.CTkLabel(self.pop_up, text="Commission Rate",width=200, height=20)
        self.pop_up.label_tof_pilot = customtkinter.CTkLabel(self.pop_up, text="ToF",width=200, height=20)
        self.pop_up.label_age_pilot = customtkinter.CTkLabel(self.pop_up, text="Age",width=200, height=20)
        self.pop_up.text_name_pilot = customtkinter.CTkTextbox(self.pop_up, width=200, height=20)
        self.pop_up.text_cpf_pilot = customtkinter.CTkTextbox(self.pop_up, width=200, height=20)
        self.pop_up.text_com_pilot = customtkinter.CTkTextbox(self.pop_up, width=200, height=20)
        self.pop_up.text_tof_pilot = customtkinter.CTkTextbox(self.pop_up, width=200, height=20)
        self.pop_up.text_age_pilot = customtkinter.CTkTextbox(self.pop_up, width=200, height=20)
        self.pop_up.update_button_pilot = customtkinter.CTkButton(self.pop_up, text="Update")
        self.pop_up.cancel_button_pilot = customtkinter.CTkButton(self.pop_up, text="Cancel")
        self.pop_up.delete_button_pilot = customtkinter.CTkButton(self.pop_up, text="Delete")
        self.pop_up.text_name_pilot.grid(row=1, column=0, padx=50, pady=0)
        self.pop_up.text_cpf_pilot.grid(row=1, column=1, padx=50, pady=0)
        self.pop_up.text_com_pilot.grid(row=3, column=0, padx=50, pady=0)
        self.pop_up.text_tof_pilot.grid(row=3, column=1, padx=50, pady=0)
        self.pop_up.text_age_pilot.grid(row=5, column=0, padx=50, pady=0, columnspan=2)
        self.pop_up.label_nome_pilot.grid(row=0, column=0, padx=50, pady=5)
        self.pop_up.label_cpf_pilot.grid(row=0, column=1, padx=50, pady=5)
        self.pop_up.label_com_pilot.grid(row=2, column=0, padx=50, pady=5)
        self.pop_up.label_tof_pilot.grid(row=2, column=1, padx=50, pady=5)
        self.pop_up.label_age_pilot.grid(row=4, column=0, padx=50, pady=5, columnspan=2)
        self.pop_up.update_button_pilot.grid(row=6, column=0,padx=50, pady=10)
        self.pop_up.cancel_button_pilot.grid(row=6, column=1,padx=50, pady=10)
        self.pop_up.delete_button_pilot.grid(row=7, column=0,padx=50, pady=10, columnspan=2)

        self.pop_up.text_name_pilot.insert("0.0", pilot_data['name'])
        self.pop_up.text_cpf_pilot.insert("0.0", pilot_data['cpf'])
        self.pop_up.text_com_pilot.insert("0.0", pilot_data['commission_rate'])
        self.pop_up.text_tof_pilot.insert("0.0", pilot_data['total_flight_hours'])
        self.pop_up.text_age_pilot.insert("0.0", pilot_data['age'])


        self.pop_up.bind('<Escape>', self.cancel_chances)
        self.pop_up.update_button_pilot.bind('<Button-1>', self.save_changes)
        self.pop_up.cancel_button_pilot.bind('<Button-1>', self.cancel_chances)
        self.pop_up.delete_button_pilot.bind('<Button-1>', self.delete_pilot)

    def delete_pilot(self, event):
        msg = CTkMessagebox(title="Delete?", message="Do you want to delete this pilot?",
                        icon="warning", option_1="Cancel", option_2="No", option_3="Yes")
        response = msg.get()
    
        if response=="Yes":
            self.db.delete_pilot(pilot_id)
            self.pop_up.destroy()
            self.update_pilots_table()
        else:
            print("Click 'Yes' to exit!")


    def save_changes(self, event):
        
        new_value = {
                    "name": self.pop_up.text_name_pilot.get("1.0", INSERT),
                    "cpf": self.pop_up.text_cpf_pilot.get("1.0", INSERT),
                    "commission_rate": self.pop_up.text_com_pilot.get("1.0", INSERT),
                    "total_flight_hours": self.pop_up.text_tof_pilot.get("1.0", INSERT),
                    "age": self.pop_up.text_age_pilot.get("1.0", INSERT),
                    }
        
        print(new_value)
        print(pilot_id)
        if self.db.update_pilot(pilot_id, new_value):
            CTkMessagebox(message="Pilot Updated!",icon="check", option_1="Ok").grab_set()
            self.pop_up.destroy()
            self.update_pilots_table()
        else:
            CTkMessagebox(title="Error", message="Something went wrong!", icon="cancel")

    def cancel_chances(self, event):
        self.pop_up.destroy()

    def update_all_table(self):
        self.update_pilots_table()
        self.update_helicopters_table()
        self.update_destinations_table()
        self.update_reservations_table()


    def open_input_dialog_event(self):
        print("kkkkk")
        '''
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Insert a pilot   ")
        print("CTkInputDialog:", dialog.get_input())
        '''

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