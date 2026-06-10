import os,time,random, pygame, pyttsx3, cx_Freeze
from cx_Freeze import setup, Executable
setup(
    name="Rodolfinho 2.0",
    version="1.0",
    description="Jogo em Pygame",
    executables=[Executable("main.py")])
