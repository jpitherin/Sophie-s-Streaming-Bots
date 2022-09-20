from mctools import RCONClient  # Import the RCONClient
import sys
import os
from dotenv import load_dotenv
load_dotenv()

HOST = os.environ['HOST']  # Hostname of the Minecraft server
PORT = os.environ['PORT']  # Port number of the RCON server
ME = os.environ['ME']

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
        cmd = cmd + '{CustomName:"\\"' + name + '\\"",Owner:'+ME+'}'
    else:
        cmd = cmd + "{Owner:"+ME+"}"
        
    print(cmd)
    
    response = rcon.command(cmd)
    response = rcon.command(f"say {chatter} thinks Sophie needs a kitty")
    if name != ".":
        response = rcon.command(f"say Meet {name}")
    rcon.stop()
    
def Bzzz(chatter):
    rcon.start()    
    response = rcon.command("summon bee ~ ~ ~")
    response = rcon.command("summon bee ~ ~ ~")
    response = rcon.command("summon bee ~ ~ ~")
    response = rcon.command(f"say Bees?!?!?! (Thanks, {chatter}...)")
    rcon.stop()
    
def DayTime(chatter):
    rcon.start()    
    response = rcon.command("time set day")
    response = rcon.command(f"Good morning, {chatter}!")
    rcon.stop()
    
def NightTime(chatter):
    rcon.start()    
    response = rcon.command("time set night")
    response = rcon.command(f"Good night, {chatter}!")
    rcon.stop()
 
def HomeJeeves(chatter):
    rcon.start()    
    cmd = f"teleport {ME} 0 64 0"
    response = rcon.command(cmd)
    response = rcon.command(f"{chatter} is sending Sophie home")
    rcon.stop()

def GetLost(chatter):
    rcon.start()   
    cmd = f"spreadplayers ~ ~ 10 50000 false {ME}"
    response = rcon.command(cmd)
    response = rcon.command(f"{chatter} is sending Sophie on an adventure")
    rcon.stop()


 
if __name__ == "__main__":
    chatter = sys.argv[1]
    command = sys.argv[2]
    name = sys.argv[3]
    
    success = login()
    
    if success == True:
    
        #rcon.start()
        #cmd = f"op {ME}"
        #response = rcon.command(cmd)
        #rcon.stop()
        
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
        if command == "Bzzz":
            Bzzz(chatter)
            
        if command == "DayTime":
            DayTime(chatter)
        if command == "NightTime":
            NightTime(chatter)  
            
        if command == "HomeJeeves":
            HomeJeeves(chatter) 
        if command == "GetLost":
            GetLost(chatter)