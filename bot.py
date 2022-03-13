import pyautogui as bot
import time 
time.sleep(10)
# bot.moveTo(522,406)
# bot.click(clicks=1)

while 1 > -1:
    for i in range(0,100):
        i = str(i)
        bot.typewrite('000'+i)
        bot.hotkey('enter')
        time.sleep(1)
        bot.click(clicks=1)
        if i == '10':
            for i in range(10,101):
                i = str(i)
                bot.typewrite('00'+i)
                bot.hotkey('enter')
                time.sleep(1)
                bot.click(clicks=1)
                if i == '100':    
                    for i in range(100,3000000):
                        i = str(i)
                        bot.typewrite('0'+i)
                        bot.hotkey('enter')
                        time.sleep(1)
                        bot.click(clicks=1)
                        if i == '1000':
                            for i in range(1000,3000000):
                                i = str(i)
                                bot.typewrite(i)
                                bot.hotkey('enter')
                                time.sleep(1)
                                bot.click(clicks=1)
                                # if i == '10000':
                                #     for i in range(10000,3000000):
                                #         i = str(i)
                                #         bot.typewrite('0'+i)
                                #         bot.hotkey('enter')
                                #         time.sleep(1)
                                #         bot.click(clicks=1)
                                #         if i == '100000':
                                #             for i in range(100000,1000000):
                                #                 i = str(i)
                                #                 bot.typewrite(i)
                                #                 bot.hotkey('enter')
                                #                 time.sleep(1)
                                #                 bot.click(clicks=1)
                        
                                        
                                    
                    



        
