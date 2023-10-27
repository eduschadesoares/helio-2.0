
from tkinter import *
from tkinter import ttk
import customtkinter
import difflib

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


    db = db

        # Define window
        geometry("1100x580")
        title("Helio System")

        # create sidebar frame with widgets
        sidebar_frame = customtkinter.CTkFrame( width=140, corner_radius=0)
        sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        sidebar_frame.grid_rowconfigure(4, weight=1)
        logo_label = customtkinter.CTkLabel(sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        sidebar_button_1 = customtkinter.CTkButton(sidebar_frame, command=open_input_dialog_event)
        sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        sidebar_button_2 = customtkinter.CTkButton(sidebar_frame, command=sidebar_button_event)
        sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        sidebar_button_3 = customtkinter.CTkButton(sidebar_frame, command=sidebar_button_event)
        sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        appearance_mode_label = customtkinter.CTkLabel(sidebar_frame, text="Appearance Mode:", anchor="w")
        appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        appearance_mode_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=change_appearance_mode_event)
        appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        scaling_label = customtkinter.CTkLabel(sidebar_frame, text="UI Scaling:", anchor="w")
        scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        scaling_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=change_scaling_event)
        scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        label_top = customtkinter.CTkLabel( text= "Ultimos Voos", width=800, height=20)
        label_top.grid(row=0, column=2, padx=(20, 0), pady=(5, 0))
        label_top = customtkinter.CTkLabel( text= "APARECE AQUI", width=800, height=20)
        label_top.grid(row=1, column=2, padx=(20, 0), pady=(5, 0))

        # create tabview
        tabview = customtkinter.CTkTabview( width=800)
        tabview.grid(row=2, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        tabview.add("Pilots")
        tabview.add("Helicopters")
        tabview.add("Destinations")
        tabview.add("Reservations")        
        tabview.tab("Pilots").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        tabview.tab("Helicopters").grid_columnconfigure(0, weight=1)
        tabview.tab("Destinations").grid_columnconfigure(0, weight=1)
        tabview.tab("Reservations").grid_columnconfigure(0, weight=1)



        # Create automatically all tables
        create_all_tables()

        #table.bind('<<TreeviewSelect>>', item_select)


    def create_all_tables():
        create_pilots_table()
        update_pilots_table()
        create_helicopters_table()
        update_helicopters_table()
        create_destinations_table()
        update_destinations_table()
        create_reservations_table()
        update_reservations_table()

    def create_pilots_table():
        column_list = ["Name", "CPF", "CR", "ToF", "Age"]

        pilots_table = ttk.Treeview(tabview.tab("Pilots"), columns=column_list, show = 'headings')
        
        for i in column_list:
            pilots_table.heading(i, text = i)
            pilots_table.column(i,minwidth=100, width=150)

        pilots_table.grid(row=0, column=0, padx=20, pady=(0, 0))

        #pilots_table.bind('<<TreeviewSelect>>', pilots_item_select)
        pilots_table.bind('<Double-1>', pilots_open_edit)

        

    def update_pilots_table():
        all_results = db.get_all_generic("pilots")
        values = {}
        for i in all_results:
            values = (
                i['name'],
                i['cpf'],
                i['commission_rate'],
                i['total_flight_hours'],
                i['age'],
            )
            pilots_table.insert(parent='', index=0, values=values)

    def create_helicopters_table():
        column_list = ["Serial", "Current City", "Flight Hours", "Age"]

        helicopters_table = ttk.Treeview(tabview.tab("Helicopters"), columns=column_list, show = 'headings')
        
        for i in column_list:
            helicopters_table.heading(i, text = i)
            helicopters_table.column(i,minwidth=100, width=150)

        helicopters_table.grid(row=0, column=0, padx=20, pady=(0, 0))
        helicopters_table.bind('<<TreeviewSelect>>', helicopters_item_select)

    def update_helicopters_table():
        all_results = db.get_all_generic("helicopters")
        values = {}
        for i in all_results:
            values = (
                i['serial'],
                i['current_city'],
                i['flight_hours'],
                i['age'],
            )
            helicopters_table.insert(parent='', index=0, values=values)

    def create_destinations_table():
        column_list = ["Code", "City", "Distance", "Open"]

        destinations_table = ttk.Treeview(tabview.tab("Destinations"), columns=column_list, show = 'headings')
        
        for i in column_list:
            destinations_table.heading(i, text = i)
            destinations_table.column(i,minwidth=100, width=150)

        destinations_table.grid(row=0, column=0, padx=20, pady=(0, 0))
        destinations_table.bind('<<TreeviewSelect>>', destinations_item_select)

    def update_destinations_table():
        all_results = db.get_all_generic("destinations")
        values = {}
        for i in all_results:
            values = (
                i['code'],
                i['city'],
                i['distance'],
                i['is_open'],
            )
            destinations_table.insert(parent='', index=0, values=values)

    def create_reservations_table():
        column_list = ["Reservation ID", "Destination", "Date", "Time", "Helicopter Serial"]

        reservations_table = ttk.Treeview(tabview.tab("Reservations"), columns=column_list, show = 'headings')
        
        for i in column_list:
            reservations_table.heading(i, text = i)
            reservations_table.column(i,minwidth=100, width=150)

        reservations_table.grid(row=0, column=0, padx=20, pady=(0, 0))
        reservations_table.bind('<<TreeviewSelect>>', reservations_item_select)

    def update_reservations_table():
        all_results = db.get_all_generic("reservations")
        values = {}
        for i in all_results:
            values = (
                i['reservation_id'],
                f"({i['destination']}) - {db.return_destination_city(i['destination'])}",
                i['date'],
                i['time'],
                i['helicopter_serial']
            )
            reservations_table.insert(parent='', index=0, values=values)

    def pilots_item_select( event):
        for i in pilots_table.selection():
            print(pilots_table.item(i)['values'])

    def helicopters_item_select( event):
        for i in helicopters_table.selection():
            print(helicopters_table.item(i)['values'])

    def destinations_item_select( event):
        for i in destinations_table.selection():
            print(destinations_table.item(i)['values'])
    
    def reservations_item_select( event):
        for i in reservations_table.selection():
            print(reservations_table.item(i)['values'])

    def pilots_open_edit( event):
        # creates a pop-up editor
        pop_up = Toplevel()
        pop_up.title("Edit Pilot")
        pop_up.grab_set()
        pop_up.geometry("600x400")
            
        pop_up.label_nome_pilot = customtkinter.CTkLabel(pop_up, text="Name",width=200, height=20)
        pop_up.label_cpf_pilot = customtkinter.CTkLabel(pop_up, text="CPF",width=200, height=20)
        pop_up.label_com_pilot = customtkinter.CTkLabel(pop_up, text="Commission Rate",width=200, height=20)
        pop_up.label_tof_pilot = customtkinter.CTkLabel(pop_up, text="ToF",width=200, height=20)
        pop_up.label_age_pilot = customtkinter.CTkLabel(pop_up, text="Age",width=200, height=20)
        pop_up.text_name_pilot = customtkinter.CTkTextbox(pop_up, width=200, height=20)
        pop_up.text_cpf_pilot = customtkinter.CTkTextbox(pop_up, width=200, height=20)
        pop_up.text_com_pilot = customtkinter.CTkTextbox(pop_up, width=200, height=20)
        pop_up.text_tof_pilot = customtkinter.CTkTextbox(pop_up, width=200, height=20)
        pop_up.text_age_pilot = customtkinter.CTkTextbox(pop_up, width=200, height=20)
        pop_up.update_button_pilot = customtkinter.CTkButton(pop_up, text="Update")
        pop_up.cancel_button_pilot = customtkinter.CTkButton(pop_up, text="Cancel")
        pop_up.text_name_pilot.grid(row=1, column=0, padx=50, pady=0)
        pop_up.text_cpf_pilot.grid(row=1, column=1, padx=50, pady=0)
        pop_up.text_com_pilot.grid(row=3, column=0, padx=50, pady=0)
        pop_up.text_tof_pilot.grid(row=3, column=1, padx=50, pady=0)
        pop_up.text_age_pilot.grid(row=5, column=0, padx=50, pady=0, columnspan=2)
        pop_up.label_nome_pilot.grid(row=0, column=0, padx=50, pady=5)
        pop_up.label_cpf_pilot.grid(row=0, column=1, padx=50, pady=5)
        pop_up.label_com_pilot.grid(row=2, column=0, padx=50, pady=5)
        pop_up.label_tof_pilot.grid(row=2, column=1, padx=50, pady=5)
        pop_up.label_age_pilot.grid(row=4, column=0, padx=50, pady=5, columnspan=2)
        pop_up.update_button_pilot.grid(row=6, column=0,padx=50, pady=10)
        pop_up.cancel_button_pilot.grid(row=6, column=1,padx=50, pady=10)


        pop_up.update_button_pilot.bind('<Button-1>', save_changes)
        pop_up.cancel_button_pilot.bind('<Double-1>', destroy())


    def save_changes( event):
        print("Update")

    def cancel_changes( event):
        print(event.cancel_button_pilot.state)



    def open_input_dialog_event():
        print("kkkkk")
        '''
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Insert a pilot   ")
        print("CTkInputDialog:", dialog.get_input())
        '''

    def change_appearance_mode_event( new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event( new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event():
        

        print("sidebar_button click")

if __name__ == "__main__":
    app = App()
    app.mainloop()


#app = App()