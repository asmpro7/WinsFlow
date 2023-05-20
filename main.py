# Created by Ahmed ElSaeed
# Telegram: @asmprotk
# GitHub: @asmpro7

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import subprocess

class WinsFlow(FlowLauncher):

    def query(self, query):
        results=[]
        if query == "min":
            subprocess.run(f"nircmd.exe win min alltopnodesktop")
        elif query == "max":
            subprocess.run(f"nircmd.exe win max alltopnodesktop")
        elif query == "close":
            subprocess.run(f"nircmd.exe win close alltopnodesktop")
        else:
            results.append({
                    "Title": "Click to Minimize all windows",
                    "IcoPath": f"Images/min.png",
                    "JsonRPCAction": {"method": "min", "parameters":[]  }
                    })
            results.append({
                    "Title": "Click to Maximize all windows",
                    "IcoPath": f"Images/max.png",
                    "JsonRPCAction": {"method": "max", "parameters":[]  }
                    })
            results.append({
                    "Title": "Click to Close all windows",
                    "IcoPath": f"Images/close.png",
                    "JsonRPCAction": {"method": "Close", "parameters":[]  }
                    })


        return results
    def min(self):
        subprocess.run(f"nircmd.exe win min alltopnodesktop") 
    def max(self):
        subprocess.run(f"nircmd.exe win max alltopnodesktop") 
    def Close(self):
        subprocess.run(f"nircmd.exe win close alltopnodesktop") 

if __name__ == "__main__":
    WinsFlow()
