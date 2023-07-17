import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import xlsxwriter
import plotly.graph_objects as go
from kivy.uix.popup import Popup
import numpy as np
import pandas as pd
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import os


global N,T,A,Aplt,Ncpt,Nd,Ad,Td,Date,Flag
N=[]
Flag=0
Date=[]
Nd=[]
T=[]
Td=[]
A=[]
Ad = []
Aplt=[]

class FirstWindow(Screen):
    
    
    #initialize infinite keywords
    '''name = ObjectProperty(None)
    title = ObjectProperty(None)
    amt = ObjectProperty(None)'''
    
    def press(self):
        nme= self.nme.text
        title = self.title.text
        Amount = self.amt.text
        date= self.date.text
        if nme!="" or title!="" or Amount!="":
            
        

            print(nme,Amount,title)
            #self.dspl= Label(text= f'{name},{title},{Amount}')
            #self.add_widget(self.dspl)
            #for j in range (i):
            
            N.append(nme)
            Nd.append(nme)
            T.append(title)
            Td.append(title)
            A.append(Amount)
            Ad.append(Amount)
            Date.append(date)
            
            Ncpt = [x.upper() for x in N]
            if len(N)>1:
            
                for t in range (len(A)):
                    u = int(A[t])
                    Aplt.append(u)
                    #x = N[p].upper
                    #print(x)
                for m in range (len(N)):

                
                    for p in range (len(N)) :
                        if p+1 == len(N):
                            break
                        if p+1>m:
                            if Ncpt[m] == Ncpt[p+1]:
                                Aplt[m]= Aplt[m]+Aplt[(p+1)]
                                if len(A)>1:
                                    del A[(p+1)]
                                if len(A)>0:
                                    del A[0]
                                
                                del Aplt[(p+1)]
                                del N[(p+1)]
                                break
                            elif len(A)!= 0:
                                if len(A)==2:
                                    A.pop()
                                    A.pop()
                                else:
                                    A.pop()
           
                
                
                
                #A = [str(Aplt[x]) for x in range(len(Aplt))]
            self.nme.text=""
            self.title.text=""
            self.amt.text=""
        
    def graph(self):
        data = Aplt
        
        
        labels = N

        
        print(Aplt)
        print(A)
        plt.xticks(range(len(data)), labels)
        plt.xlabel('Names')
        plt.ylabel('Amounts')
        plt.bar(range(len(data)), data) 
        plt.show()

        

    def press3(self):
      pass

class SecondWindow(Screen):
    def view(self):
        color1 = 'lightgreen'
        color2 = 'lightblue'
  
        fig = go.Figure(data=[go.Table(
            header=dict(values=['Name', 'Amount','Title']),
            cells=dict(values=[[Nd[x] for x in range (len(Nd))],
                               [Ad[x] for x in range (len(Ad))],
                               [Td[x] for x in range (len(Td))]],
                       fill_color=[[color1, color2, color1,
                                    color2, color1]*2],))
        ])
        fig.show()


        
    def press2(self):
        i = 1
        j="A"
        k="B"
        l="C"
        v="D"
        x=str(i)
        a=self.filename.text
        
        outworkbook = xlsxwriter.Workbook(a+".xlsx")
        outsheet = outworkbook.add_worksheet()
        for o in range (len(Nd)):
            print(Nd[o],Td[o],Ad[o])
        for r in range (len(N)):
            x=str(r+2)
            print(x)
            outsheet.write(j+x ,Nd[r])
            outsheet.write(k+x ,Ad[r])
            outsheet.write(l+x , Td[r])
            outsheet.write(v+x , Date[r])
        outworkbook.close()

    def openxl(self):
        if self.filename1.text != "":
            b = os.getcwd()
            a= self.filename1.text+".xlsx"
            os.startfile(b+"\\"+a)

    def graph(self):
        data = Aplt
        
        
        labels = N

        
        print(Aplt)
        print(A)
        plt.xticks(range(len(data)), labels)
        plt.xlabel('Names')
        plt.ylabel('Amounts')
        plt.bar(range(len(data)), data) 
        plt.show()
	

class WindowManager(ScreenManager):
	pass


kv=Builder.load_file("elder.kv")
'''class MyGridlayout(Widget):
    pass'''
'''class MyGridlayout(Widget):'''

    #initialize infinite keywords
name = ObjectProperty(None)
date = ObjectProperty(None)
title = ObjectProperty(None)
amt = ObjectProperty(None)
filename = ObjectProperty(None)
filename1 = ObjectProperty(None) 
    
        
class AwesomeApp(App):
    def build(self):
        return kv
if __name__=='__main__':
    AwesomeApp().run()

