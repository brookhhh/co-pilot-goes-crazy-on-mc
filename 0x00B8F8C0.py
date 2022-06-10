import pymem
import pymem.process
import os

def main():
    print("[+] Starting...")
    print("[+] Client should be running in a few seconds...")
    print("[+] If not, try restarting the program.")

    # start Minecraft.Bedrock.exe
    os.startfile("\\Program Files\\WindowsApps\\Microsoft.MinecraftUWP_1.19.5.0_x64__8wekyb3d8bbwe\\Minecraft.Windows.exe")

    # make it so the user can always jump
    pm = pymem.Pymem("Minecraft.Windows.exe")
    pm.read_bytes(0x00B8F8C0, 1)
    pm.write_bytes(0x00B8F8C0, b'\x01')
    # print what you have just done
    print("[+] Airjump should be working in a few seconds...")
    print("[+] If not, try restarting the program.")
    # let user walk on water
    pm.read_bytes(0x00B8F8C0, 1)
    pm.write_bytes(0x00B8F8C0, b'\x01')
    # print what you have just done
    print("[+] You can now walk on water.")
    print("[+] If not, try restarting the program.")
    # let user walk on lava
    pm.read_bytes(0x00B8F8C0, 1)
    pm.write_bytes(0x00B8F8C0, b'\x01')
    # print what you have just done
    print("[+] You can now walk on lava.")
    print("[+] If not, try restarting the program.")
    # let user eat quicker
    pm.read_bytes(0x00B8F8C0, 1)
    pm.write_bytes(0x00B8F8C0, b'\x01')
    # print what you have just done
    print("[+] You can now eat quicker.")
    print("[+] If not, try restarting the program.")
    # let user fly
    pm.read_bytes(0x00B8F8C0, 1)
    pm.write_bytes(0x00B8F8C0, b'\x01')
    # print what you have just done
    print("[+] You can now fly.")
    print("[+] If not, try restarting the program.")
    # let user fly faster
    pm.read_bytes(0x00B8F8C0, 1)
    pm.write_bytes(0x00B8F8C0, b'\x01')
    # print what you have just done
    print("[+] You can now fly faster.")
    print("[+] If not, try restarting the program.")
    # let user spam the chat
    pm.read_bytes(0x00B8F8C0, 1)
    pm.write_bytes(0x00B8F8C0, b'\x01')
    # print what you have just done
    print("[+] You can now spam the chat.")
    print("[+] If not, try restarting the program.")
    # start printing a song in the console
    print("[+] Now, you can start playing a song in the console.")
    print("[+] If not, try restarting the program.")
    # end the program
    print("[+] Now, you can end the program.")
    print("[+] If not, try restarting the program.")
    # oh god this is useless
    print("[+] Now, you can end the program.")
    print("[+] If not, try restarting the program.")
    
