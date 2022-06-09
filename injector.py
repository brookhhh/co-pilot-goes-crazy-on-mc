from pymem import Pymem
import os
import subprocess

# Make a DLL injector for Minecraft using Pymem (i added this line, i also added take some lines down below to make it work in theory 
MC = subprocess.Popen('Minecraft.Bedrock.exe')

pm = Pymem('Minecraft.Bedrock.exe')
pm.inject_python_interpreter()
filepath = os.path.join(os.path.abspath('.'), 'INJECTION.txt')
filepath = filepath.replace('\\', '\\\\')
shellcode = """"""
f = open("{}", 'w')
f.write("INJECTION")
f.close()
pm.write_bytes(0x00400000, shellcode)
pm.write_bytes(0x00400000, filepath)
pm.write_bytes(0x00400000, "INJECTION")
pm.write_bytes(0x00400000, "INJECTION")
pm.write_bytes(0x00400000, "INJECTION")
pm.write_bytes(0x00400000, "INJECTION")
pm.write_bytes(0x00400000, "INJECTION")
pm.write_bytes(0x00400000, "INJECTION")
pm.write_bytes(0x00400000, "INJECTION")
pm.write_bytes(0x00400000, "INJECTION")
pm.write_bytes(0x00400000, "INJECTION")
pm.write_bytes(0x00400000, "INJECTION")
pm.write_bytes(0x00400000, "INJECTION")
"""""".format(filepath)
pm.inject_python_shellcode(shellcode)
MC.kill()
