import numpy as np
import os
# Define file name/address
Root_address = r'C:\Users\liuch\Desktop\Courses\MECE 4606 Digital manufacturing\HW\Laserbox'
F_name='SSS'
F_address=Root_address +f"\{F_name}.SVG"
# Define raw material and fixation parameters
Raw_length=400
Raw_width=250
Raw_Thickness=5   
# Define fixation components
Bolt_Slot=4
Bolt_Length=20   #must > Raw_Thickness*3+Bolt_Slot
Bolt_Tip_Slot=Bolt_Length-Raw_Thickness*3-Bolt_Slot
Bolt_Diameter=4
Bolt_Stopper_Width=9
Sawtooth_Length=max(Raw_Thickness*2,Bolt_Stopper_Width)
# Define box geometry
Box_length=300
Box_width=200
Box_height=100
# define drawing geometry(center)
DL=10
DW=10
DH=10
Input_Text="I love digital manufacturing"

#Define operation geometry
Direction='X' # another is Y
Sawtooth_Direction=1 # +1 means the first line is extrude;-1 means the first line is groove
r_c=1 # first fixation is groove=1, hole=-1
r_c_p=1 # first sawtooth 1 or second sawtooth 2 for groove/cricle position
# Check input geometry
def Check_input(): 
    Err_sign=0
    if min(DL,DW,DH)<2*Raw_Thickness:    # check center area
        print(f"Error:DL,DW,DH must>={4*Raw_Thickness}mm")
        Err_sign=1
    if Bolt_Diameter<1 or Bolt_Diameter>Raw_Thickness:  #check fixation part
        print(f"Error:Bolt_diameter is not in the range between 1mm-{Raw_Thickness}mm")
        Err_sign=1
    elif Bolt_Tip_Slot<0: #check Bolt length
        print("Error:Bolt length is not enough,increase bolt length or reduce bolt slot")
        Err_sign=1
    elif Bolt_Slot<1 or Bolt_Slot>20: #check Bolt length
        print("Error:Blocker slot height is not in the range between 1mm-20mm")
        Err_sign=1
    elif Bolt_Stopper_Width<Bolt_Diameter+Raw_Thickness or Bolt_Stopper_Width>20: 
        print(f"Error:Blocker slot is not in the range between {Bolt_Diameter+Raw_Thickness}mm-20mm")
        Err_sign=1
    A_W1=(Bolt_Length-Raw_Thickness)*2+DW   #check width
    A_W2=Raw_Thickness*4+Sawtooth_Length*7
    A_W=max(A_W1,A_W2)
    if A_W>Box_width:
        print(f"Error:Box width is not enough,minimum requirement is {A_W}mm")
        Err_sign=1 
    B_W1=(Bolt_Length-Raw_Thickness)*2+DL   #check length
    B_W2=Raw_Thickness*4+Sawtooth_Length*7
    B_W=max(B_W1,B_W2)
    if B_W>Box_length:              
        print(f"Error:Box length is not enough,minimum requirement is {B_W}mm")
        Err_sign=1
    C_W1=(Bolt_Length-Raw_Thickness)*2+DH  #check height
    C_W2=Raw_Thickness*4+Sawtooth_Length*7
    C_W=max(C_W1,C_W2)
    if C_W>Box_height:              
        print(f"Error:Box height is not enough,minimum requirement is {C_W}mm")
        Err_sign=1
    if Box_length<Box_width:  # Basic geometry check
        print(f"Error:Length must >= Width")
    elif Box_length+4.5*Raw_Thickness>Raw_length:
        print(f"Error:Length must <={Raw_length-4.5*Raw_Thickness}mm")
        Err_sign=1
    elif Box_width>Raw_width:
        print(f"Error:Width must <={Raw_width}mm")
        Err_sign=1
    elif Box_height+5*Raw_Thickness>Raw_length and Box_height+0.5*Raw_Thickness>=Box_length:
        print(f"Error:Height must <={Raw_length-5*Raw_Thickness}mm")
    elif Box_height+5*Raw_Thickness<Raw_length and Box_height+0.5*Raw_Thickness>=Box_length and Box_length+4.5*Raw_Thickness>Raw_width:
        print(f"Error:Length must <={Raw_width-4.5*Raw_Thickness}mm")        
        Err_sign=1
    elif Box_height+5*Raw_Thickness>Raw_width and Box_height+0.5*Raw_Thickness<Box_length:
        print(f"Error:Height must <={Raw_width-5*Raw_Thickness}mm")
        Err_sign=1
    return Err_sign


C=Check_input()
if C==1:
    print('Program will exit due to wrong set up characters, please correct')
    os._exit(0)
#Function to draw uni sawtooth
'''I_X: initial X coordinate;  I_Y: initial Y coordinate;
   SL: step length;   step: step number;
   Dr: direction vector +1 or -1 for tooth;
   Orientation: along X axis or Y axis'''
def ST(I_X:float, I_Y:float,SL:float,step:int,Dr:int,Orientation:str): 
    if step<0:                      #check input
        print('step must >=0')
    elif Dr!=1 and Dr!=-1:
        print('Dr must be 1 or -1')  
    elif Orientation!="X" and Orientation!="Y":
        print('Orientation must be "X" or "Y"')  
    Main_list=[]
    for a in range(step):          # start drawing
        if a%4==0:
            Main_list.append(I_X+(a*SL)/2)
            Main_list.append(I_Y)
        elif a%4==1:
            Main_list.append(I_X+(int(a/2)+1)*SL)
            Main_list.append(I_Y) 
        elif a%4==2:   
            Main_list.append(I_X+(int(a/2))*SL)
            Main_list.append(I_Y+Dr*Raw_Thickness) 
        elif a%4==3:   
            Main_list.append(I_X+((a+1)/2)*SL)
            Main_list.append(I_Y+Dr*Raw_Thickness) 
    if Orientation=="Y": # Rotate 90 degree
        Dx=I_X-I_Y #offset original point X
        Dy=I_Y-I_X #offset original point Y
        for b in range(len(Main_list)):
            if b%2!=0:
                X_temp=Main_list[b-1]
                Main_list[b-1]=Main_list[b]+Dx
                Main_list[b]=X_temp+Dy
    End_X=Main_list[len(Main_list)-2]   # record end coordinate X
    End_Y=Main_list[len(Main_list)-1]   # record end coordinate Y
    return Main_list,End_X,End_Y

#Function to draw unique sawtooth
'''I_X: initial X coordinate;  I_Y: initial Y coordinate;
   SL: step length;
   Dr: direction vector +1 or -1 for groove or circle;
   Orientation: along X axis or Y axis
   R_C: define groove +1 or circle -1
   BD: bolt diameter;    BSH: Bolcker Slot height;   BTH: Bolt tile height     BSW: Blocker slot width
   CR: hole diameter'''
def GrCi(I_X:float, I_Y:float,SL:float,Dr:int,Orientation:str,BD:float,BSH:float,BTH:float,BSW:float): 
#check input
    if SL<0 or SL<Raw_Thickness*2:
        print(f'SL must >=0 and =>{Raw_Thickness*2}')  
    elif Dr!=1 and Dr!=-1:
        print('Dr must be 1 or -1')  
    elif Orientation!="X" and Orientation!="Y":
        print('Orientation must be "X" or "Y"')  
    elif BD<0 or BD>SL/2:
        print(f'BD must between 0 to {BD>SL/2}')
    elif BSH<0:
        print('BSH must >0')     
    elif BSW>SL:
        print(f'BSW must <={SL}')   
    Main_list=[]
    t1=[I_X,I_Y,I_X+(SL-BD)/2,I_Y,I_X+(SL-BD)/2,I_Y-Raw_Thickness,I_X+(SL-BSW)/2,I_Y-Raw_Thickness,I_X+(SL-BSW)/2,I_Y-Raw_Thickness-BSH]
    t2=[t1[2],t1[9],t1[2],t1[9]-BTH,t1[2]+BD,t1[9]-BTH,t1[2]+BD,t1[9],I_X+(SL+BSW)/2,t1[9],I_X+(SL+BSW)/2,t1[9]+BSH,I_X+(SL+BD)/2,t1[9]+BSH]
    t3=[t2[12],I_Y,I_X+SL,I_Y]
    Main_list=t1+t2+t3  
    if  Dr==-1:  #reflection
        for a in range(len(Main_list)):
            if a%2!=0:
                delta=I_Y-Main_list[a]
                Main_list[a]=I_Y+delta 
    if Orientation=="Y": # Rotate 90 degree
        Dx=I_X-I_Y #offset original point X
        Dy=I_Y-I_X #offset original point Y
        for c in range(len(Main_list)):
            if c%2!=0:
                X_temp=Main_list[c-1]
                Main_list[c-1]=Main_list[c]+Dx
                Main_list[c]=X_temp+Dy
    End_X=Main_list[len(Main_list)-2]   # record end coordinate X
    End_Y=Main_list[len(Main_list)-1]   # record end coordinate Y     
    return Main_list,End_X,End_Y

#Define hole function
def hole(I_X:float,I_Y:float):
    Output=[I_X,I_Y]
    return Output
# Define transformation function
def tran(In_Data,TX:int,TY:int):  #TX: target point X TY: target point X
    TX=TX-In_Data[0]
    TY=TY-In_Data[1]
    Out_Data=[]
    for t in range(len(In_Data)):
        if t%2==0:
           Out_Data.append(In_Data[t]+TX)
        elif t%2==1:
           Out_Data.append(In_Data[t]+TY)  
    return Out_Data
def ref(In_Data,X_Y:int):  #reflection,X_Y=1 for x-axis, X_Y=-1 for y=axis
    if X_Y==1:
        for t in range(len(In_Data)):
            if t%2==1:
                delta=In_Data[1]-In_Data[t]
                In_Data[t]=In_Data[1]+delta
    elif X_Y==-1:  
        for t in range(len(In_Data)):
            if t%2==0:
                delta=In_Data[0]-In_Data[t]
                In_Data[t]=In_Data[0]+delta

# Define translate function to suitable format for svg
def Tr(Input_D):
    P_svg=(f'{Input_D[0]}')
    for m in range(1 ,len(Input_D)):     
       P_svg=(f"{P_svg},{Input_D[m]}")
    return P_svg    

''' ------------draw whole box --------------'''
#first plate-Bottom plate
TN=int((Box_length-4*Raw_Thickness)/Sawtooth_Length) #how many tooth in center along X
if TN%2==0: 
    TN=TN-1
Ad=(Box_length-TN*Sawtooth_Length)/2 #  first tooth length X
'''upper length line'''
M_stream_1,st01,st02=ST(Raw_Thickness*6,Raw_Thickness,Ad,3,1,"X")
M_stream_2,st11,st12=ST(st01,st02,Sawtooth_Length,5,-1,"X")
M_stream_3,st21,st22=GrCi(st11,st12,Sawtooth_Length,-1,"X",Bolt_Diameter,Bolt_Slot,Bolt_Tip_Slot,Bolt_Stopper_Width)
M_stream_3.append(st21)
M_stream_3.append(st22-Raw_Thickness)
M_stream_4,st31,st32=ST(st21,st22-Raw_Thickness,Sawtooth_Length,(TN-6)*2+1,1,"X")
M_stream_5,st41,st42=GrCi(st31,st32,Sawtooth_Length,-1,"X",Bolt_Diameter,Bolt_Slot,Bolt_Tip_Slot,Bolt_Stopper_Width)
M_stream_5.append(st41)
M_stream_5.append(st42-Raw_Thickness)
M_stream_6,st51,st52=ST(st41,st42-Raw_Thickness,Sawtooth_Length,5,1,"X")
M_stream_7,st61,st62=ST(st51,st52,Ad,2,-1,"X")
M_stream_A=M_stream_1+M_stream_2+M_stream_3+M_stream_4+M_stream_5+M_stream_6+M_stream_7
'''lower length line'''
M_stream_B=tran(M_stream_A,Raw_Thickness*6,Raw_Thickness+Box_width)
ref(M_stream_B,1)
'''left width line'''
tn=int((Box_width-4*Raw_Thickness)/Sawtooth_Length) #how many tooth in center along Y
if tn%2==0: 
    tn=tn-1
ad=(Box_width-tn*Sawtooth_Length)/2 #  first tooth length Y
S_stream_1,s01,s02=ST(Raw_Thickness*6,Raw_Thickness,ad,3,1,"Y")
S_stream_2,s11,s12=ST(s01,s02,Sawtooth_Length,tn*2,-1,"Y")
S_stream_3,s21,s22=ST(s11-Raw_Thickness,s12,ad,2,1,"Y")
S_stream_A=S_stream_1+S_stream_2+S_stream_3
'''right width line'''
S_stream_B=tran(S_stream_A,Raw_Thickness*6+Box_length,Raw_Thickness)
ref(S_stream_B,-1)
'''Main stream'''
Main_stream=[]
Main_stream.append(Tr(M_stream_A))
Main_stream.append(Tr(M_stream_B))
Main_stream.append(Tr(S_stream_A))
Main_stream.append(Tr(S_stream_B))
'''holes'''
H1=hole(S_stream_A[0]+Raw_Thickness/2,S_stream_A[1]+ad+1.5*Sawtooth_Length)
H2=hole(S_stream_A[0]+Raw_Thickness/2,S_stream_A[len(S_stream_B)-1]-ad-1.5*Sawtooth_Length)
H3=hole(S_stream_B[0]-Raw_Thickness/2,S_stream_B[1]+ad+1.5*Sawtooth_Length)
H4=hole(S_stream_B[0]-Raw_Thickness/2,S_stream_B[len(S_stream_B)-1]-ad-1.5*Sawtooth_Length)
H=H1+H2+H3+H4

#H x L plates
'''upper length line'''
P_stream_1,sp01,sp02=ST(Raw_Thickness*6,Raw_Thickness*3+Box_width,Ad,3,-1,"X")
P_stream_2,sp11,sp12=ST(sp01,sp02,Sawtooth_Length,TN*2,1,"X")
P_stream_3,sp21,sp22=ST(sp11,sp12+Raw_Thickness,Ad,2,-1,"X")
P_stream=P_stream_1+P_stream_2+P_stream_3
'''Left Side line'''
tnn=int((Box_height-4*Raw_Thickness)/Sawtooth_Length) #how many tooth in center along Y
if tnn%2==0: 
    tnn=tnn-1
add=(Box_height-tnn*Sawtooth_Length)/2 #  first tooth length Y
PL_stream_1,pl01,pl02=ST(Raw_Thickness*6,Raw_Thickness*3+Box_width,add-Raw_Thickness,3,1,"Y")
PL_stream_2,pl11,pl12=ST(pl01,pl02,Sawtooth_Length,5,-1,"Y")
PL_stream_3,pl21,pl22=GrCi(pl11,pl12,Sawtooth_Length,-1,"Y",Bolt_Diameter,Bolt_Slot,Bolt_Tip_Slot,Bolt_Stopper_Width)
PL_stream_3.append(pl21-Raw_Thickness)
PL_stream_3.append(pl22)
PL_stream_4,pl31,pl32=ST(pl21-Raw_Thickness,pl22,Sawtooth_Length,(tnn-6)*2+1,1,"Y")
PL_stream_5,pl41,pl42=GrCi(pl31,pl32,Sawtooth_Length,-1,"Y",Bolt_Diameter,Bolt_Slot,Bolt_Tip_Slot,Bolt_Stopper_Width)
PL_stream_5.append(pl41-Raw_Thickness)
PL_stream_5.append(pl42)
PL_stream_6,pl51,pl52=ST(pl41-Raw_Thickness,pl42,Sawtooth_Length,5,1,"Y")
PL_stream=PL_stream_1+PL_stream_2+PL_stream_3+PL_stream_4+PL_stream_5+PL_stream_6
'''Right Side line'''
PR_stream=tran(PL_stream,Raw_Thickness*6+Box_length,Raw_Thickness*3+Box_width)
ref(PR_stream,-1)
#PR_stream.append(PR_stream[len(PR_stream)-2])
PR_stream.append(PR_stream[len(PR_stream)-2])
PR_stream.append((PR_stream[len(PR_stream)-2]+add))
'''Bearing'''
del PL_stream[len(PL_stream)-6:] 
PL_stream.append(PL_stream[len(PL_stream)-2]-Raw_Thickness*4.5)
PL_stream.append(PL_stream[len(PL_stream)-2])
PL_stream.append(PL_stream[len(PL_stream)-2])
PL_stream.append(PL_stream[len(PL_stream)-2]+add+Sawtooth_Length+Raw_Thickness*4)
PL_stream.append(PL_stream[len(PL_stream)-2]+Raw_Thickness*8)
PL_stream.append(PL_stream[len(PL_stream)-2])
PL_stream.append(PL_stream[len(PL_stream)-2])
PL_stream.append(PL_stream[len(PL_stream)-2]-Raw_Thickness*4)
PL_stream.append(PR_stream[len(PR_stream)-2])
PL_stream.append(PR_stream[len(PR_stream)-1])
'''Holes'''
#Bearing
h1=hole(Raw_Thickness*5.5,PR_stream[len(PR_stream)-1]-0.5*Raw_Thickness)
h1_1=hole(Raw_Thickness*5.5,PR_stream[len(PR_stream)-1]+Raw_Thickness*7+Box_height)
h2=hole(Raw_Thickness*6+Ad+2.5*Sawtooth_Length,Raw_Thickness*2.5+Box_width)
h3=hole(Raw_Thickness*6+Box_length-Ad-2.5*Sawtooth_Length,Raw_Thickness*2.5+Box_width)
h4=hole(Raw_Thickness*6+Ad+2.5*Sawtooth_Length,Raw_Thickness*2.5+Box_width+Raw_Thickness*8+Box_height)
h5=hole(Raw_Thickness*6+Box_length-Ad-2.5*Sawtooth_Length,Raw_Thickness*2.5+Box_width+Raw_Thickness*8+Box_height)
H=H+h2+h3+h4+h5
'''Update Main stream'''
Main_stream.append(Tr(P_stream))
Main_stream.append(Tr(PL_stream))
Main_stream.append(Tr(PR_stream))
Main_stream.append(Tr(tran(P_stream,Raw_Thickness*6,P_stream[1]+Box_height+Raw_Thickness*7.5)))
Main_stream.append(Tr(tran(PL_stream,Raw_Thickness*6,PL_stream[1]+Box_height+Raw_Thickness*7.5)))
Main_stream.append(Tr(tran(PR_stream,Raw_Thickness*6+Box_length,PR_stream[1]+Box_height+Raw_Thickness*7.5)))

#H x W plates
'''upper length line'''
T_stream_1,tp01,tp02=ST(Raw_Thickness*10+Box_length,Raw_Thickness*2,add-Raw_Thickness,3,-1,"X")
T_stream_2,tp11,tp12=ST(tp01,tp02,Sawtooth_Length,tnn*2,1,"X")
T_stream_2.append(T_stream_2[len(T_stream_2)-2])
T_stream_2.append(Raw_Thickness*2)
T_stream_2.append(T_stream_2[len(T_stream_2)-2]+add)
T_stream_2.append(Raw_Thickness*2)
T_stream=T_stream_1+T_stream_2
'''left line'''
TL_stream_1,tl01,tl02=ST(Raw_Thickness*10+Box_length,Raw_Thickness*2,ad-Raw_Thickness,3,-1,"Y")
TL_stream_2,tl11,tl12=ST(tl01,tl02,Sawtooth_Length,3,1,"Y")
TL_stream_3,tl21,tl22=GrCi(tl11,tl12,Sawtooth_Length,-1,"Y",Bolt_Diameter,Bolt_Slot,Bolt_Tip_Slot,Bolt_Stopper_Width)
TL_stream_3.append(tl21-Raw_Thickness)
TL_stream_3.append(tl22)
TL_stream_4,tl31,tl32=ST(tl21-Raw_Thickness,tl22,Sawtooth_Length,(tn-4)*2+1,1,"Y")
TL_stream_5,tl41,tl42=GrCi(tl31,tl32,Sawtooth_Length,-1,"Y",Bolt_Diameter,Bolt_Slot,Bolt_Tip_Slot,Bolt_Stopper_Width)
TL_stream_5.append(tl41-Raw_Thickness)
TL_stream_5.append(tl42)
TL_stream_6,tl51,tl52=ST(tl41-Raw_Thickness,tl42,Sawtooth_Length,3,1,"Y")
TL_stream_6.append(tl51)
TL_stream_6.append(tl52+ad-Raw_Thickness)
TL_stream=TL_stream_1+TL_stream_2+TL_stream_3+TL_stream_4+TL_stream_5+TL_stream_6
'''bottom line'''
TK_stream=tran(T_stream,tl51,tl52+ad-Raw_Thickness)
ref(TK_stream,1)
'''right line'''
TR_stream,tr01,tr02=ST(T_stream[len(T_stream)-2],Raw_Thickness*2,(Box_width-Raw_Thickness*2)/5,11,-1,"Y")
'''holes'''
th1=hole(Raw_Thickness*9+add+Box_length+2.5*Sawtooth_Length,Raw_Thickness*1.5)
th2=hole(Raw_Thickness*9+Box_length+Box_height-add-2.5*Sawtooth_Length,Raw_Thickness*1.5)
th3=hole(th1[0],th1[1]+Box_width-Raw_Thickness)
th4=hole(th2[0],th2[1]+Box_width-Raw_Thickness)
H=H+th1+th2+th3+th4
'''Update Main stream'''
Main_stream.append(Tr(T_stream))
Main_stream.append(Tr(TL_stream))
Main_stream.append(Tr(TK_stream))
Main_stream.append(Tr(TR_stream))

# unique plate
#Top line
TU_stream_1,tu01,tu02=ST(Raw_Thickness*13+Box_length+Box_height,Raw_Thickness*2,add-Raw_Thickness,3,-1,"X")
TU_stream_2,tu11,tu12=ST(tu01,tu02,Sawtooth_Length,(tnn-1)*2,1,"X")
TU_stream_2.append(tu11+add+Raw_Thickness)
TU_stream_2.append(tu12)
TU_stream=TU_stream_1+TU_stream_2
#Left line
TV_stream=tran(TL_stream,Raw_Thickness*13+Box_length+Box_height,Raw_Thickness*2)
'''bottom line'''
TB_stream=tran(TU_stream,TV_stream[len(TV_stream)-2],TV_stream[len(TV_stream)-1])
ref(TB_stream,1)
TB_stream.append(TU_stream_2[len(TU_stream_2)-2])
TB_stream.append(TU_stream_2[len(TU_stream_2)-1])
'''holes'''
tb1=hole(th1[0]+Box_height+Raw_Thickness*3,th1[1])
tb2=hole(th2[0]+Box_height+Raw_Thickness*3,th2[1])
tb3=hole(th3[0]+Box_height+Raw_Thickness*3,th3[1])
tb4=hole(th4[0]+Box_height+Raw_Thickness*3,th4[1])
H=H+tb1+tb2+tb3+tb4
'''Update Main stream'''
Main_stream.append(Tr(TU_stream))
Main_stream.append(Tr(TV_stream))
Main_stream.append(Tr(TB_stream))

#Lid plate
'''top line'''
Lid1,li01,li02=ST(T_stream_1[0],P_stream_1[1],3.873*Raw_Thickness,3,1,"X")
Lid1.append(li01)
Lid1.append(li02+Raw_Thickness)
Lid1.append(li01-2.4365*Raw_Thickness+Box_length)
Lid1.append(li02+Raw_Thickness)
'''bottom line'''
Lid2=tran(Lid1,T_stream_1[0],P_stream_1[1]+Box_width+2*Raw_Thickness)
ref(Lid2,1)
'''Left line'''
Lid3=[Lid1[0],Lid1[1],Lid2[0],Lid2[1]]
'''Right line'''
Lid4,li03,li04=ST(Lid1[len(Lid1)-2],Lid1[len(Lid1)-1],(Box_width-Raw_Thickness*2)/5,10,1,"Y")
Main_stream.append(Tr(Lid1))
Main_stream.append(Tr(Lid2))
Main_stream.append(Tr(Lid3))
Main_stream.append(Tr(Lid4))

Lid_CX=Lid1[0]+(Lid1[len(Lid1)-2]-Lid1[0]+Raw_Thickness)/2
Lid_CY=Lid1[len(Lid1)-1]+(Box_width-Raw_Thickness*2)/2


''' ------------draw whole box --------------'''

''' ------------input text --------------'''
#define function
'''I_X: start position X
   I_Y: start position Y
   I_F: font size         
   I_text: input text  rot: angle to rotate from horizontal'''
def text(I_X:float,I_Y:float,I_F:int,I_text:str,rot:int):
    Main_text=f"<text x='{I_X}' y='{I_Y+50}' style='text-anchor: middle' transform='translate({0},{0}) rotate({rot})' fill='blue' font-size='{I_F}'>{I_text}</text>\n"
    text_length_X=(len(I_text)*I_F*0.45)*np.cos(rot*np.pi/180)+I_F*0.45
    text_length_Y=(len(I_text)*I_F*0.45)*np.sin(rot*np.pi/180)+I_F*0.45
    return Main_text,text_length_X,text_length_Y
MA,XX,YY=text(Lid_CX,Lid_CY,15,Input_Text,0)
if XX>Box_length:
    print("text length over the maximum")

'''input logo'''


'''------------Draw SVG file-------------'''
try:
    F=open(F_address, 'w')
except FileExistsError:
    print("Error: File name already exists,can not overwrite file")   
    os._exit(0)   
F.write(f"<svg height='{Raw_length*8}' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='{Raw_length*8}'>\n")
for M in range(len(Main_stream)):
    F.write(f"  <polyline points='{Main_stream[M]}' stroke='black' stroke-width='1' fill='none' />\n")
for n in range(int(len(H)/2)):
    F.write(f"  <circle cx='{H[n*2]}' cy='{H[n*2+1]}' r='{Bolt_Diameter/2}' stroke='black' stroke-width='1' fill='none' />\n")
F.write(f"  <circle cx='{h1[0]}' cy='{h1[1]}' r='{Raw_Thickness*2}' stroke='black' stroke-width='1' fill='none' />\n")
F.write(f"  <circle cx='{h1_1[0]}' cy='{h1_1[1]}' r='{Raw_Thickness*2}' stroke='black' stroke-width='1' fill='none' />\n")
F.write(MA)
#F.write(f"<image x='{Lid_CX-20}' y='{Lid_CY-20}' width='50px' height='50px' transform='translate({0},{0}) rotate(0)' xlink:href='{Root_address}\c.svg'/>\n")
F.write(f"<image x='{Lid_CX-20}' y='{Lid_CY-20}' width='50px' height='50px' transform='translate({0},{0}) rotate(0)' xlink:href='https://yt3.ggpht.com/ytc/AKedOLRSzyfUti-CpOY-d0XZCmXUsdnx2qGWZ8ZvC67-=s900-c-k-c0x00ffffff-no-rj'/>\n")
F.write("</svg>")  
