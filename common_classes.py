import tkinter as tk


# File created to hold classes used across the GUI
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox(
            "insert")  # accessing the screen coordinates of the widget so tooltop appears in the correct place
        x += self.widget.winfo_rootx() + 25  # tells the tooltip where to appear in correlation to the widget it is for
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1,
                         font=("Century Gothic", 12))
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None


class LabelDropdownMenu(tk.Frame):
    def __init__(self, master, label_text, options, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.label = tk.Label(self, text=label_text, font=("Century Gothic", 20), fg="black")
        self.label.pack(side=tk.LEFT, padx=(0, 10))
        self.selected_value = tk.StringVar()
        self.option_var = tk.StringVar()
        self.option_menu = tk.OptionMenu(self, self.option_var, *options)
        self.option_menu.config(font=("Century Gothic", 18), bg="white", fg="black", bd=2, relief=tk.SOLID,
                                width=15, justify=tk.LEFT)
        self.option_menu.pack(side=tk.LEFT)
        self.option_var.set(options[0])
        self.option_var.trace("w", self.on_select)

    def on_select(self, *args):
        self.selected_value.set(self.option_var.get())


class Styles:
    FONT_FAMILY = "Century Gothic"
    FONT_COLOR = "black"
    FONT_XXSMALL = 10
    FONT_XSMALL = 14
    FONT_SMALL = 16
    FONT_MEDIUM = 18
    FONT_LARGE = 20


def create_label(parent, text, font=(Styles.FONT_FAMILY, Styles.FONT_LARGE), fg=Styles.FONT_COLOR, justify=tk.LEFT,
                 side=tk.LEFT, pady=0, padx=10):
    label = tk.Label(parent, text=text, font=font, fg=fg, justify=justify)
    label.pack(side=side, pady=pady, padx=padx)
    return label


def create_entry(parent, font=(Styles.FONT_FAMILY, Styles.FONT_MEDIUM), fg=Styles.FONT_COLOR, width=30, bd=2,
                 relief=tk.SOLID, side=tk.RIGHT, padx=10):
    entry = tk.Entry(parent, font=font, fg=fg, width=width, bd=bd, relief=relief)
    entry.pack(side=side, padx=padx)
    return entry


def create_label_frame(parent, pady=15):
    frame = tk.Frame(parent)
    frame.pack(pady=pady)
    return frame


def create_profile_label(parent,
                         text,
                         font=(Styles.FONT_FAMILY, Styles.FONT_XSMALL),
                         fg=Styles.FONT_COLOR,
                         justify=tk.LEFT,
                         side=tk.LEFT,
                         pady=0,
                         padx=10):
    profile_label = tk.Label(parent, text=text, font=font, fg=fg, justify=justify)
    profile_label.pack(side=side, pady=pady, padx=padx)
    return profile_label


def create_profile_info_display_label(parent,
                                      font=(Styles.FONT_FAMILY, Styles.FONT_XSMALL),
                                      fg=Styles.FONT_COLOR,
                                      borderwidth=0,
                                      relief=tk.FLAT,
                                      side=tk.RIGHT,
                                      padx=10):
    profile_info_display_label = tk.Label(parent, font=font, fg=fg, borderwidth=borderwidth, relief=relief)
    profile_info_display_label.pack(side=side, padx=padx)
    return profile_info_display_label


def create_profile_info_frame(parent, side=tk.TOP, pady=10):
    frame = tk.Frame(parent)
    frame.pack(side=side, pady=pady)
    return frame
