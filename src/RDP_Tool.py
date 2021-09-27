import tkinter as tk
import pandas as pd
import os
import csv
from pathlib import Path
import subprocess


serverSelection = None

window = tk.Tk()

window.title('Quick RDP Tool')
window.geometry('300x200')
window.configure(background='white')

bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.RIGHT)

def readInputFile2DataFrame(inputFileName):
    df = pd.read_csv(inputFileName)
    print('File:', inputFileName, 'is loaded')
    return df

def readCfg2DataFrame():
    fileName = 'config.csv'
    return readInputFile2DataFrame(Path("../cfg/"+ fileName))

def openRDP():
  for i in LB.curselection():
    key = LB.get(i)
    serverHost = dictHost[key]
    # print(f"Remote Desktop to {LB.get(i)}: {serverHost}")

    cmd = f"mstsc /v:{serverHost}"

    out = subprocess.run(cmd, shell=True, timeout=2)
    # print(out)


def LBSelection(event):
  selection = event.widget.curselection()
  if selection:
      index = selection[0]
      data = event.widget.get(index)
      serverSelection = data
    #   print(f"ListBox Val: {data}")
  else:
      serverSelection = None
    #   print(f"ListBox Val: No Selection")




bottom_button = tk.Button(bottom_frame, text='Connect', fg='black', command=openRDP)

bottom_button.place(x=50,y=10,anchor='w')
bottom_button.pack(side=tk.BOTTOM)

LB = tk.Listbox(window)
LB.bind("<<ListboxSelect>>", LBSelection)

df = readCfg2DataFrame()
dictHost = dict()


for index, row in df.iterrows():
  LB.insert(index, row['Name'])
  dictHost[row['Name']] = row['Host']
  LB.pack()

# print(dictHost)


window.mainloop()