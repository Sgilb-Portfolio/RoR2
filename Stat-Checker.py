"""
TODO:
    * Edit display labels
    * Fix problem with reading in max size
"""


import pymem
import pymem.process
import time
import tkinter as tk

# Attach to Risk of Rain 2 process
pm = pymem.Pymem('Risk of Rain 2.exe')
mod_base = pm.base_address  # gets the base address of the games module


# Traverses a pointer chain to find actual memory address where a particular value is stored
def find_dynamic_address(base_address, offsets):
    addr = pm.read_int(base_address)
    for offset in offsets:
        addr = pm.read_int(addr + offset)
    return addr



"""
const int MAX_NUM = 512
const char buf[MAX_NUM]
"""

#attack_speed_base = mod_base + 0x0074B099
#attack_speed_offsets =  [0x40]

movement_speed_base = mod_base + 0x0074B098
movement_speed_offsets = [0x40, 0x538, 0x40, 0x48, 0xB0, 0x30, 0x3E0]

#crit_chance_base = mod_base + 0x0074B088
#crit_chance_offsets = [0x10, 0x20, 0x30]

#bleed_chance_base = mod_base + 0x0074B097
#bleed_chance_offsets = [0x10, 0x20, 0x30]

#health_regen_base = mod_base + 0x0074B093
#health_regen_offsets = [0x10, 0x20, 0x30]

#armor_base = mod_base + 0x0074B091
#armor_offsets = [0x10, 0x20, 0x30]


# Finds the memory address for each stat and stores them in the global variables
def find_addresses():
    global movement_speed
"""
    global attack_speed_address, movement_speed_address, crit_chance_address
    global bleed_chance_address, health_regen_address, armor_address
"""
    #attack_speed_address = find_dynamic_address(attack_speed_base, attack_speed_offsets)
     movement_speed_address = find_dynamic_address(movement_speed_base, movement_speed_offsets)

    #crit_chance_address = find_dynamic_address(crit_chance_base, crit_chance_offsets)
    #bleed_chance_address = find_dynamic_address(bleed_chance_base, bleed_chance_offsets)
    #health_regen_address = find_dynamic_address(health_regen_base, health_regen_offsets)
    #armor_address = find_dynamic_address(armor_base, armor_offsets)


# Call to initialize
find_addresses()

"""
# Shows item descriptions
def item_description(event, ):
"""

# Define colors and styles for the Risk of Rain 2 theme
background_color = "#1e1e1e"  # Dark background similar to the game's UI
text_color = "#7ec8f0"  # Cyan-like color used in the game
font_style = ("Consolas", 14, "bold")  # Consolas font is close to the futuristic feel
highlight_color = "#ffd700"  # Gold color for highlighting important stats

# Create the overlay window
root = tk.Tk()
root.title("Game Stats Overlay")
root.attributes("-topmost", True)
root.attributes("-alpha", 0.85)  # Adjust transparency for better visibility
root.geometry("250x250+10+35")  # Slightly larger to accommodate the new font
root.configure(bg=background_color)  # Set background color
root.overrideredirect(True)  # Removes the window border

# Create labels to display the stats
#attack_speed_label = tk.Label(root, text="Attack Speed:", font=font_style, fg=text_color, bg=background_color)
#attack_speed_label.pack(anchor="w", padx=10, pady=5)

movement_speed_label = tk.Label(root, text="Movement Speed:", font=font_style, fg=text_color, bg=background_color)
movement_speed_label.pack(anchor="w", padx=10, pady=5)

#crit_chance_label = tk.Label(root, text="Crit Chance:", font=font_style, fg=highlight_color, bg=background_color)
#crit_chance_label.pack(anchor="w", padx=10, pady=5)

#bleed_chance_label = tk.Label(root, text="Bleed Chance:", font=font_style, fg=text_color, bg=background_color)
#bleed_chance_label.pack(anchor="w", padx=10, pady=5)

#health_regen_label = tk.Label(root, text="Health Regen:", font=font_style, fg=highlight_color, bg=background_color)
#health_regen_label.pack(anchor="w", padx=10, pady=5)

#armor_label = tk.Label(root, text="Armor:", font=font_style, fg=text_color, bg=background_color)
#armor_label.pack(anchor="w", padx=10, pady=5)


def update_stats():
    # Reading item counts from memory
    #attack_speed = pm.read_float(attack_speed_address)
    movement_speed = pm.read_float(movement_speed_address)
    #crit_chance = pm.read_float(crit_chance_address)
    #bleed_chance = pm.read_float(bleed_chance_address)
    #health_regen = pm.read_float(health_regen_address)
    #armor = pm.read_float(armor_address)

    # Update the text labels
    #attack_speed_label.config(text=f"Attack Speed: {attack_speed}")
    movement_speed_label.config(text=f"Movement Speed: {movement_speed} m/s")
    #crit_chance_label.config(text=f"Crit Chance: {crit_chance}%")
    #bleed_chance_label.config(text=f"Bleed Chance: {bleed_chance}%")
    #health_regen_label.config(text=f"Health Regen: {health_regen} HP/s")
    #armor_label.config(text=f"Armor: {armor}")

    # Schedule the next update in ms
    root.after(500, update_stats)


# Start updating the stats
update_stats()

# Run the GUI loop
root.mainloop()
