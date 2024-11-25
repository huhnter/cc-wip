import turtle
import time

# Initialize game variables
cookies = 0
total_cookies_earned = 0
cookies_per_click = 1
cookies_per_second = 0

# Upgrade settings
upgrades = {
    "cursor": {"cost": 10, "cps": 1, "amount": 0},
    "grandma": {"cost": 50, "cps": 5, "amount": 0},
    "farm": {"cost": 100, "cps": 10, "amount": 0}
}

# Set up the screen
screen = turtle.Screen()
screen.title("Cookie Clicker")
screen.setup(width=600, height=600)
screen.bgcolor("lightyellow")

# Draw the clickable cookie as a circle
cookie = turtle.Turtle()
cookie.shape("circle")
cookie.color("chocolate")
cookie.shapesize(stretch_wid=5, stretch_len=5)
cookie.penup()
cookie.goto(0, 0)

# Display cookie count
cookie_count_display = turtle.Turtle()
cookie_count_display.hideturtle()
cookie_count_display.penup()
cookie_count_display.goto(0, 220)
cookie_count_display.write(f"Cookies: {cookies}", align="center", font=("Arial", 24, "bold"))

# Display cookies per second (CPS)
cps_display = turtle.Turtle()
cps_display.hideturtle()
cps_display.penup()
cps_display.goto(0, 180)
cps_display.write(f"CPS: {cookies_per_second}", align="center", font=("Arial", 18, "bold"))

# Display overall cookies earned
total_cookies_display = turtle.Turtle()
total_cookies_display.hideturtle()
total_cookies_display.penup()
total_cookies_display.goto(0, 140)
total_cookies_display.write(f"Total Cookies Earned: {total_cookies_earned}", align="center", font=("Arial", 18, "bold"))

# Upgrade buttons with shapes and labels
buttons = {}
button_labels = {}
button_positions = {"cursor": (-200, -200), "grandma": (0, -200), "farm": (200, -200)}

# Create each upgrade button with a square shape and add a label for details
for upgrade, position in button_positions.items():
    # Button for the upgrade
    btn = turtle.Turtle()
    btn.shape("square")
    btn.color("lightblue")
    btn.shapesize(stretch_wid=2, stretch_len=6)
    btn.penup()
    btn.goto(position)
    buttons[upgrade] = btn

    # Text label for the button info
    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.goto(position[0], position[1] - 50)  # Position the label below the button
    button_labels[upgrade] = label

# Function to update the displays
def update_display():
    # Update the main cookie count, CPS, and total cookies earned
    cookie_count_display.clear()
    cookie_count_display.write(f"Cookies: {cookies}", align="center", font=("Arial", 24, "bold"))
    
    cps_display.clear()
    cps_display.write(f"CPS: {cookies_per_second}", align="center", font=("Arial", 18, "bold"))
    
    total_cookies_display.clear()
    total_cookies_display.write(f"Total Cookies Earned: {total_cookies_earned}", align="center", font=("Arial", 18, "bold"))

    # Update button labels with the name, cost, CPS boost, number of purchases, and next upgrade cost
    for upgrade, label in button_labels.items():
        label.clear()
        upgrade_info = upgrades[upgrade]
        label.write(
            f"{upgrade.capitalize()}\nCost: {upgrade_info['cost']}\nCPS: +{upgrade_info['cps']}\n"
            f"Purchased: {upgrade_info['amount']} times", 
            align="center", font=("Arial", 10, "bold")
        )

# Function to handle cookie clicks
def click_cookie(x, y):
    global cookies, total_cookies_earned
    cookies += cookies_per_click
    total_cookies_earned += cookies_per_click
    update_display()

# Function to buy an upgrade
def buy_upgrade(upgrade_name):
    global cookies, cookies_per_second
    upgrade = upgrades[upgrade_name]
    if cookies >= upgrade["cost"]:
        cookies -= upgrade["cost"]
        upgrade["amount"] += 1
        cookies_per_second += upgrade["cps"]
        # Increase the cost for the next purchase
        upgrade["cost"] = int(upgrade["cost"] * 1.15)
        update_display()
    else:
        print(f"Not enough cookies to buy {upgrade_name.capitalize()}.")

# Event handlers for upgrade buttons
def on_cursor_click(x, y):
    buy_upgrade("cursor")

def on_grandma_click(x, y):
    buy_upgrade("grandma")

def on_farm_click(x, y):
    buy_upgrade("farm")

# Attach click events
cookie.onclick(click_cookie)
buttons["cursor"].onclick(on_cursor_click)
buttons["grandma"].onclick(on_grandma_click)
buttons["farm"].onclick(on_farm_click)

# Main game loop for automatic cookie generation
def update_cookies():
    global cookies, total_cookies_earned
    cookies += cookies_per_second
    total_cookies_earned += cookies_per_second
    update_display()
    screen.ontimer(update_cookies, 1000)  # Update every second

# Start the cookie update loop
update_cookies()
turtle.done()
