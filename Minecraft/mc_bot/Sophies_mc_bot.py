from mctools import RCONClient  # Import the RCONClient
import sys

HOST = 'localhost'  # Hostname of the Minecraft server
PORT = 25565  # Port number of the RCON server
ME = "Sophie__Games"

# Create the RCONClient:

rcon = RCONClient(HOST)

def login():

    # Login to RCON:
    if rcon.login("HewwoWorld"):
        #print("RCON Connected")
        return True
    else:
        print("RCON Failed to Connect")
        return False
    

def MakeItRain(chatter):
    #print("chatter", chatter)

    rcon.start()
    response = rcon.command("weather rain")
    response = rcon.command(f"say {chatter} made it rain")
    rcon.stop()
    
def BlueSkies4U(chatter):
    rcon.start()
    response = rcon.command("weather clear")
    response = rcon.command(f"say {chatter} chased away the rain")
    rcon.stop()
    
def StormsABrewin(chatter):
    rcon.start()
    response = rcon.command("weather thunder")
    response = rcon.command(f"say Prepare for lighting, courtesy of {chatter}")
    rcon.stop()

def GiveWoodPick(chatter):
    rcon.start()
    response = rcon.command(f"give {ME} minecraft:wooden_pickaxe")
    response = rcon.command(f"say {chatter} gives Sophie a wooden pickaxe")
    rcon.stop()  
    
def GiveIronPick(chatter):
    rcon.start()
    response = rcon.command(f"give {ME} minecraft:iron_pickaxe")
    response = rcon.command(f"say {chatter} gives Sophie an iron pickaxe")
    rcon.stop() 

def GiveWoodSword(chatter):
    rcon.start()
    response = rcon.command(f"give {ME} minecraft:wooden_sword")
    response = rcon.command(f"say {chatter} gives Sophie a wooden sword")
    rcon.stop()   

def GiveIronSword(chatter):
    rcon.start()
    response = rcon.command(f"give {ME} minecraft:iron_sword")
    response = rcon.command(f"say {chatter} gives Sophie an iron sword")
    rcon.stop()     

def GiveApples(chatter):
    rcon.start()
    response = rcon.command(f"give {ME} minecraft:apple 3")
    response = rcon.command(f"say {chatter} gives Sophie some apples")
    rcon.stop()
    
def AccioKitty(chatter,name):
    rcon.start()
    cmd = "summon cat ~ ~ ~ "
    # /summon cat ~ ~ ~ {CustomName:"\"Daisy\"",Owner:Sophie__Games}
    
    if name != ".":
        cmd = cmd + '{CustomName:"\\"' + name + '\\"",Owner:Sophie__Games}'
    else:
        cmd = cmd + "{Owner:Sophie__Games}"
        
    print(cmd)
    
    response = rcon.command(cmd)
    response = rcon.command(f"say {chatter} thinks Sophie needs a kitty")
    if name != ".":
        response = rcon.command(f"say Meet {name}")
    rcon.stop()
    
if __name__ == "__main__":
    chatter = sys.argv[1]
    command = sys.argv[2]
    name = sys.argv[3]
    
    success = login()
    
    if success == True:
        print("command", command)
        
        if command == "MakeItRain":
            MakeItRain(chatter)
        if command == "BlueSkies4U":
            BlueSkies4U(chatter)
        if command == "StormsABrewin":
            StormsABrewin(chatter)
        
        if command == "GiveWoodPick":
            GiveWoodPick(chatter)
        if command == "GiveIronPick":
            GiveIronPick(chatter)
        if command == "GiveWoodSword":
            GiveWoodSword(chatter)
        if command == "GiveIronSword":
            GiveIronSword(chatter)
            
        if command == "GiveApples":
            GiveApples(chatter)
        
        if command == "AccioKitty":
            AccioKitty(chatter,name)