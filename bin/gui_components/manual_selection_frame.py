from bin.gui_components.manual_selection_window import *

DEFAULT_MANUAL_SERVER_LABEL = '-----'

class ManualSelectionFrame(LabelFrame):
    def __init__(self, parent, background_color):
        super(ManualSelectionFrame, self).__init__(parent, text="Manual Selection")

        self.action_frame = Frame(self)
        self.use_manual = BooleanVar()
        self.use_manual.set("False")
        self.manual_checkbox = Checkbutton(self.action_frame, text='Select manually', selectcolor=background_color,
                                           variable=self.use_manual, command=parent.on_manual_change)
        self.manual_checkbox.pack(side=LEFT, padx=10)
        self.manual_select_button = Button(self.action_frame, command=self.select_server_manually, text='Select')
        self.manual_select_button.pack()
        self.action_frame.pack(pady=3)

        self.info_frame = Frame(self)
        self.static_server_label = Label(self.info_frame, text='Server Selected: ')
        self.static_server_label.pack(side=LEFT)
        self.dynamic_server_label = Label(self.info_frame, text=DEFAULT_MANUAL_SERVER_LABEL)
        self.dynamic_server_label.pack(side=LEFT)
        self.info_frame.pack(pady=5)

        self.pack(fill='x')

    def select_server_manually(self):
        ManualServerWindow(self)

    def __manual_frame_state_change__(self):
        if self.use_manual.get():
            # enabling manual selection frame
            self.manual_select_button.config(state=NORMAL)
            self.static_server_label.config(state=NORMAL)
            self.dynamic_server_label.config(state=NORMAL)
        else:
            # disabling manual selection frame
            self.manual_select_button.config(state=DISABLED)
            self.static_server_label.config(state=DISABLED)
            self.dynamic_server_label.config(state=DISABLED)

    def get_is_manual(self):
        return self.use_manual.get()

    def set_is_manual(self, is_manual):
        self.use_manual.set(is_manual)

    def get_manual_server(self):
        return self.dynamic_server_label.cget('text')

    def set_manual_server(self, server):
        self.dynamic_server_label.config(text=server)

    def manual_server_selected(self, server):
        self.set_manual_server(server + '.nordvpn.com')



