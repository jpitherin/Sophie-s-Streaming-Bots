from mctools import RCONClient  # Import the RCONClient
import sys

HOST = 'localhost'  # Hostname of the Minecraft server
PORT = 25565  # Port number of the RCON server
me = "Sophie__Games"

# Create the RCONClient:

rcon = RCONClient(HOST)

def login():

    # Login to RCON:
    if rcon.login("HewwoWorld"):
        print("RCON Connected")
        
        return True
    else:
        print("RCON Failed to Connect")
        return False
    

def MakeItRain(chatter):
    print("chatter", chatter)

    rcon.start()
    response = rcon.command("weather rain")
    response = rcon.command(f"say {chatter} made it rain")
    rcon.stop()
    
    
    
if __name__ == "__main__":
    chatter = sys.argv[1]
    command = sys.argv[2]
    
    success = login()
    
    if success == True:
        print("command", command)
        if command == "MakeItRain":
            MakeItRain(chatter)