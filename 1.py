from lib2to3.refactor import get_fixers_from_package
import numpy as np
from numpy.lib.npyio import zipfile_factory
from matplotlib.colors import rgb_to_hsv
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import mean
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import seaborn as sns
import sklearn
import time

# Define file name/address
Root_address = r'C:\Users\liuch\Desktop\Courses\MECE 4606 Digital manufacturing\HW\Laserbox'
F_name='SSS'
F_address=Root_address +f"\{F_name}.SVG"
# Define raw material and fixation parameters
Raw_length=650
Raw_width=450
Raw_Thickness=5    
Bolt_Slot=5
Bolt_Length=20   #must > Raw_Thickness*3+Bolt_Slot
Bolt_Tip_Slot=Bolt_Length-Raw_Thickness*3-Bolt_Slot
if Bolt_Tip_Slot<0:
    print("Bolt length is not enough,increase bolt length or reduce bolt slot")
Bolt_Diameter=5
Bolt_Stopper_Width=Bolt_Diameter*3
Sawtooth_Length=max(Raw_Thickness*2+5,Bolt_Stopper_Width)
# define drawing geometry
Bottom_Length=80
Bottom_Width=80
Front_Length=80
Front_width=80
Left_Length=80
Left_width=80
# Define box geometry
Box_length=300
Box_width=200
Box_height=150
Start_X=Raw_Thickness # define margin X as 1 time Raw_Thickness
Start_Y=Raw_Thickness+Box_width # define margin Y as 1 time Raw_Thickness
#Define operation geometry
Direction='X' # another is Y
Sawtooth_Direction=1 # +1 means the first line is extrude;-1 means the first line is groove
r_c=1 # first fixation is groove=1, hole=-1
r_c_p=1 # first sawtooth 1 or second sawtooth 2 for groove/cricle position
# Check input geometry
def Check_input():
    Err_sign=0
    A_W1=(Bolt_Length-Raw_Thickness)*2+Bottom_Width   #check width
    A_W2=Raw_Thickness*4+Sawtooth_Length*7
    A_W=max(A_W1,A_W2)
    if A_W>Box_width:
        print(f"Error:Box width is not enough,minimum requirement is {A_W}")
        Err_sign=1 
    B_W1=Raw_Thickness*2+Bottom_Length   #check length
    B_W2=Raw_Thickness*4+Sawtooth_Length*7
    B_W=max(B_W1,B_W2)
    if B_W>Box_length:              
        print(f"Error:Box length is not enough,minimum requirement is {B_W}")
        Err_sign=1
    C_W1=Raw_Thickness*2+Bottom_Length   #check height
    C_W2=Raw_Thickness*4+Sawtooth_Length*7
    C_W=max(C_W1,C_W2)
    if C_W>Box_height:              
        print(f"Error:Box height is not enough,minimum requirement is {C_W}")
        Err_sign=1
    if Raw_length<Box_length:   # check raw material size length 
        print(f"Error:Box length over material limit {Raw_length}")  
        Err_sign=1 
    if Raw_length<max(Box_height,Box_width):  # check raw material size height and width
        print(f"Error:Box height or width over material limit {Raw_width}")  
        Err_sign=1 
    return Err_sign
        
Check_input()

def ST(I_X:int, I_Y:int,SL:int,step:int,Dr:int): 
    '''I_X: initial X coordinate;I_Y: initial Y coordinate;SL: step length;
       step: step number;Dr: direction vector +1 or -1 for tooth'''
    if step<0:                      #check input
        print('step must >=0')
    elif SL<0:
        print('SL must >=0')  
    elif Dr!=1 and Dr!=-1:
        print('Dr must be 1 or -1')  
    Main_list=[]
    for e in range(step):
        if e%4==0:
            Main_list.append(I_X+e*SL/2)
            Main_list.append(I_Y)
        elif e%4==1:
            Main_list.append(I_X+(int(e/2)+1)*SL)
            Main_list.append(I_Y) 
        elif e%4==2:   
            Main_list.append(I_X+(int(e/2))*SL)
            Main_list.append(I_Y+Dr*Raw_Thickness) 
        elif e%4==2:   
            Main_list.append(I_X+((e+1)/2)*SL)
            Main_list.append(I_Y+Dr*Raw_Thickness) 
    return Main_list
    
# Draw sawtooth function
def Sawtooth_X(length:int,direction:str,sawtooth_direction:int,S_X:int, S_Y:int,R_C:int,R_C_P:int):
    tooth_no=int((length-Raw_Thickness*4)/Sawtooth_Length)
    if tooth_no%2==0:
       tooth_no=tooth_no-1
    Ad=(length-tooth_no*Sawtooth_Length)/2 #  first tooth length
    Ct=(tooth_no-7)/2 # center teeth number
    Pola=[]     # main matrix
    S_Pola=[]   # groove

    Pola_S1=[S_X,S_Y,S_X+Ad,S_Y,S_X+Ad,S_Y-Raw_Thickness]  # first covex tooth
    Pola_S11=[S_X,S_Y,S_X+Ad,S_Y,S_X+Ad,S_Y+Raw_Thickness] # first covave tooth
    if R_C_P==1:
        Pola_S1=Pola_S1+[S_X+Ad+Sawtooth_Length,S_Y-Raw_Thickness,S_X+Ad+Sawtooth_Length,\
             S_Y,S_X+Ad+Sawtooth_Length*2,S_Y,S_X+Ad+Sawtooth_Length*2,S_Y-Raw_Thickness]
        Pola_S11=Pola_S11+[S_X+Ad+Sawtooth_Length,S_Y-Raw_Thickness,S_X+Ad+Sawtooth_Length,\
             S_Y,S_X+Ad+Sawtooth_Length*2,S_Y,S_X+Ad+Sawtooth_Length*2,S_Y-Raw_Thickness]
    if R_C==1      :    #groove
        Pola_S2=[(S_X+Ad+Sawtooth_Length*2+(Sawtooth_Length/2)-(Bolt_Diameter/2)),S_Y-Raw_Thickness]
        Pola_S3=[Pola_S2[0],S_Y-Raw_Thickness*2,Pola_S2[0]-(Bolt_Stopper_Width-Bolt_Diameter)/2,S_Y-Raw_Thickness*2]
        Pola_S4=[Pola_S3[2],Pola_S3[3]-Bolt_Slot,Pola_S2[0],Pola_S3[3]-Bolt_Slot,Pola_S2[0],Pola_S3[3]-Bolt_Slot-Bolt_Tip_Slot]
        Pola_S5=[Pola_S2[0]+Bolt_Diameter,Pola_S4[5],Pola_S2[0]+Bolt_Diameter,Pola_S4[5]+Bolt_Tip_Slot]
        Pola_S6=[Pola_S5[2]+(Bolt_Stopper_Width-Bolt_Diameter)/2,Pola_S5[3],Pola_S5[2]+(Bolt_Stopper_Width-Bolt_Diameter)/2,Pola_S5[3]+Bolt_Slot]
        Pola_S7=[Pola_S5[2],Pola_S6[3],Pola_S5[2],Pola_S6[3]+Raw_Thickness,Pola_S5[2]+(Sawtooth_Length-Bolt_Diameter)/2,S_Y-Raw_Thickness]
        Pola_S8=[Pola_S7[4],S_Y]
        Pola=Pola_S1+Pola_S2+Pola_S3+Pola_S4+Pola_S5+Pola_S6+Pola_S7+Pola_S8    
        S_Pola=[S_X+Ad+Sawtooth_Length*2,S_Y,S_X+Ad+Sawtooth_Length*2,S_Y-Raw_Thickness]
        S_Pola=S_Pola+Pola_S2+Pola_S3+Pola_S4+Pola_S5+Pola_S6+Pola_S7+Pola_S8
        for i in range(int(1+Ct*4)):
            if i%4==0 :
                Pola.append(Pola[len(Pola)-2]+Sawtooth_Length) 
                Pola.append(S_Y)
            elif i%4==1:
                Pola.append(Pola[len(Pola)-2]) 
                Pola.append(S_Y-Raw_Thickness)
            elif i%4==2:    
                Pola.append(Pola[len(Pola)-2]+Sawtooth_Length)      
                Pola.append(S_Y-Raw_Thickness)
            elif i%4==3 : 
                Pola.append(Pola[len(Pola)-2])      
                Pola.append(S_Y)
        for j in range(len(S_Pola)): # transform fixation geometry
            if j%2==0 :
                S_Pola[j]=S_Pola[j]+(Ct*2+2)*Sawtooth_Length
        Pola=Pola+S_Pola
        Pola_S9=[Pola[len(Pola)-2]+Sawtooth_Length,S_Y,Pola[len(Pola)-2]+Sawtooth_Length,S_Y-Raw_Thickness]
        Pola_S10=[Pola_S9[0]+Sawtooth_Length,Pola_S9[3],Pola_S9[0]+Sawtooth_Length,S_Y,Pola_S9[0]+Sawtooth_Length+Ad,S_Y]
        Pola=Pola+Pola_S9+Pola_S10

    if sawtooth_direction==1: #change sawtooth_direction
        for t in range(len(Pola)):
            if t%2!=0:
                delta=S_Y-Pola[t]
                Pola[t]=S_Y+delta
    if direction=="Y":# change directions
        Dx=S_X-S_Y #offset original point X
        Dy=S_Y-S_X #offset original point Y
        for k in range(len(Pola)):
            if k%2!=0:
                X=Pola[k-1]
                Pola[k-1]=Pola[k]+Dx
                Pola[k]=X+Dy



    #translate to suitable format for svg
    P_svg=(f'{Pola[0]}')
    for m in range(1 ,len(Pola)):     
        P_svg=(f"{P_svg},{Pola[m]}")
    return P_svg    

        
L=Sawtooth_X(300,"Y",1,5,40,1)   
C=Sawtooth_X(300,"X",1,5,40,1) 

F=open(F_address, 'x')
F.write(f"<svg height='{Raw_length*2}' xmlns='http://www.w3.org/2000/svg' width='{Raw_width*2}'>\n")
F.write(f"  <polyline points='{L}' stroke='black' stroke-width='1' fill='none' />\n")
F.write(f"  <polyline points='{C}' stroke='black' stroke-width='1' fill='none' />\n")
F.write("</svg>")

"""try:
    F=open(F_address, 'x')
except FileExistsError:
    print("Error: File name already exists")  
F.write(f"<svg height='{Raw_length*8}' xmlns='http://www.w3.org/2000/svg' width='{Raw_width*8}'>\n")
F.write(f"  <polyline points='{P_svg}' stroke='black' stroke-width='1' fill='none' />\n")
F.write("</svg>")"""