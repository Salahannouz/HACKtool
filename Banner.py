import time
from time import sleep
import os
import sys


start =  """
           \033[0;32m     $                  $
               $$                  $$
               $$                  $$
               $$s                s$$
               $$$$              $$$$
               ³$$$$  ¶¶¶¶¶¶¶¶  $$$$³
                ³$$$$  ¶¶¶¶¶¶  $$$$³
              ¶..$$$$$  ¶¶¶¶  $$$$$..¶
            ¶¶¶¶..$$$  ¶¶¶¶¶¶  $$$.¶¶¶¶
              ¶¶¶¶¶  ¶¶¶¶¶¶¶¶¶¶  ¶¶¶¶
               ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                ¶¶¶\033[31mSALAH\033[0;32m¶¶¶¶\033[31mSALAH\033[32m¶¶¶
                ¶¶¶¶\033[31mhack \033[0;32m¶¶\033[31mhack \033[32m¶¶¶¶
                 ¶¶¶¶¶¶¶¶  ¶¶¶¶¶¶¶¶
                   ¶¶¶¶¶¶  ¶¶¶¶¶¶¶
             ¶        ¶¶¶¶¶¶¶¶¶        ¶
              ``™`°^¶..¶..¶..¶..¶^°'™``
                  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
            \033[31m¶¶                        \033[31m¶¶
            \033[31m¶¶                        \033[31m¶¶
            \033[31m¶¶                        \033[31m¶¶
        \033[0;32m¶¶  \033[31m¶¶  \033[32m¶¶                ¶¶  \033[31m¶¶  \033[32m¶¶
     ¶  ¶¶  \033[31m¶¶  \033[32m¶¶  ¶¶        ¶¶  ¶¶  \033[31m¶¶  \033[32m¶¶  ¶
    ¶¶  ¶¶  \033[31m¶¶  \033[32m¶¶  ¶¶        ¶¶  ¶¶  \033[31m¶¶  \033[32m¶¶  ¶¶
    ¶¶  ¶¶  \033[31m¶¶  \033[32m¶¶  ¶¶        ¶¶  ¶¶  \033[31m¶¶  \033[32m¶¶  ¶¶
     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶          ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶

          YouTube : \033[31m AMATERASS \033[0;32m
          Github  : \033[31m https://github.com/Salahannouz\033[0;32m
          Moroccan hackers S...

  """
os.system("clear")
sleep(1)
os.system("xdg-open https://m.youtube.com/channel/UCy5Z4RnSKUHkIiBSjRobdUw")
sleep(2)
os.system("clear")
for s in start:
	sys.stdout.write(s)
	sys.stdout.flush()
	sleep(0.03)
print ("\n")
