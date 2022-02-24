import numpy as np
#import os
#import goto
#from goto import with_goto
#from dominate.tags import label
#input 

#Label .begin1
Raw_length,Raw_width,Raw_Thickness=input("please enter raw material length,width and thickness in mm:\
 (separate with space,recommended input is: (457.2 304.8 3)\n").split(" ")
#if any(type(Raw_length),type(Raw_width),type(Raw_Thickness))!='float' and any(type(Raw_length),type(Raw_width),type(Raw_Thickness))!='int':
    #print("geometry must be numbers" )
    #goto .begin1 
Raw_length=float(Raw_length)
Raw_width=float(Raw_width)
Raw_Thickness=float(Raw_Thickness)
if min(Raw_length,Raw_width,Raw_Thickness)<0:
    print("geometry must be positive" )
elif Raw_length<Raw_width:
    print("length must >= width" )    
    #goto .begin1
elif Raw_Thickness>40 or Raw_Thickness<1:
    print("Raw material thickness must in range from 1mm to 40mm" )  
    #goto .begin1  
elif Raw_Thickness*29>Raw_length:
    print(f"Raw material length is not enough to make the minimum box, must >= {Raw_Thickness*31}mm" )     
    #goto .begin1
elif Raw_Thickness*29>Raw_width:
    print(f"Raw material width is not enough to make the minimum box, must >={Raw_Thickness*30}mm" )     
    #goto .begin1
#label .begin2
Bolt_Stopper_Width,Bolt_Slot=input("please enter nut length,thickness in mm:\
(separate with space,recommended input is: 5 3)\n").split(" ") 
Bolt_Stopper_Width=float(Bolt_Stopper_Width)
Bolt_Slot=float(Bolt_Slot)
#if any(type(Bolt_Stopper_Width),type(Bolt_Slot))!='float' and any(type(Bolt_Stopper_Width),type(Bolt_Slot))!='int':
    #print("geometry must be numbers" )
    #goto .begin2  
if min(Bolt_Stopper_Width,Bolt_Slot)<0:
    print("geometry must be positive" )
    #goto .begin2
elif Bolt_Stopper_Width>Raw_Thickness*3 or Bolt_Stopper_Width<Raw_Thickness*1.2:
    print(f"nut length must in range: ({1.2*Raw_Thickness},{3*Raw_Thickness}" )   
    #goto .begin2
elif Bolt_Slot>4*Raw_Thickness or Bolt_Slot<1:
    print(f"nut thickness must in range: ({Raw_Thickness},{4*Raw_Thickness}" )   
    #goto .begin2
#label .begin3
Bolt_Diameter,Bolt_Length=input("please enter bolt diameter,bolt length in mm:\
(separate with space,recommended input is: 1.8 10)\n").split(" ")
Bolt_Diameter=float(Bolt_Diameter)
Bolt_Length=float(Bolt_Length)
#if any(type(Bolt_Diameter),type(Bolt_Length))!='float' and any(type(Bolt_Diameter),type(Bolt_Length))!='int':
    #print("geometry must be numbers" )
    #goto .begin3
if min(Bolt_Diameter,Bolt_Length)<0:
    print("geometry must be positive" )
    #goto .begin3
elif Bolt_Diameter>Raw_Thickness:
    print("bolt diameter must <= material thickness{Raw_Thickness}" )
    #goto .begin3
elif Bolt_Length<Raw_Thickness*2+Bolt_Slot or Bolt_Length>7.5*Raw_Thickness-1 :
    print(f"bolt length must in range:({Raw_Thickness*4},{7.5*Raw_Thickness-1}" )
#label .begin4
Box_length,Box_height,Box_width=input(f"please enter box length,width and height in mm:(separate with space)\n\
    to get maximum height: LxHxW=({Raw_width-Raw_Thickness*2},{Raw_length-Raw_Thickness*6},{Raw_width-Raw_Thickness*2}),\n\
    to get maximum length: LxHxW=({Raw_length-Raw_Thickness*2},{Raw_width-Raw_Thickness*2},{Raw_width-Raw_Thickness*2}),\n\
    minimum LxHxW=({25*Raw_Thickness},{25*Raw_Thickness},{19*Raw_Thickness})\n").split(" ")
Box_length=float(Box_length)
Box_width=float(Box_width)
Box_height=float(Box_height)
#if any(type(Box_length),type(Box_width),type(Box_height))!='float' and any(type(Box_length),type(Box_width),type(Box_height))!='int':
    #print("geometry must be numbers" )
    #goto .begin4
if min(Box_length,Box_width,Box_height)<0:
    print("geometry must be positive" )
    #goto .begin4
elif Box_length!=max(Box_length,Box_width):
    print("box length must >= Box_width" )
    #goto .begin4   
elif Box_length<=25*Raw_Thickness:
    print(f"box length must =>{25*Raw_Thickness} mm" )
    #goto .begin4   
elif Box_height<=25*Raw_Thickness:
    print(f"box height must =>{25*Raw_Thickness} mm" )
    #goto .begin4   
elif Box_width<=19*Raw_Thickness:
    print(f"box width must =>{19*Raw_Thickness} mm" )
    #goto .begin4  
elif Box_length-Box_height>4*Raw_Thickness:
    if Box_length>Raw_length-2*Raw_Thickness:
        print(f"box length over the limit of raw material:{Raw_length-Raw_Thickness*2} mm" )
       # goto .begin4
    elif Box_height+6*Raw_Thickness>Raw_width:
        print(f"box height over the limit of raw material:{Raw_width-6*Raw_Thickness} mm" )
        #goto .begin4
elif Box_length-Box_height<=4*Raw_Thickness: 
    if Box_height+6*Raw_Thickness>Raw_length:
        print(f"box height over the limit of raw material:{Raw_length-Raw_Thickness*6} mm" )
        #goto .begin4
    elif Box_length>Raw_width-2*Raw_Thickness:
        print(f"box length over the limit of raw material:{Raw_width-2*Raw_Thickness} mm" )
        #goto .begin4    
elif Box_width>Raw_width-2*Raw_Thickness: 
    print(f"box width over the limit of raw material:{Raw_width-2*Raw_Thickness} mm" )
    #goto .begin4     
#label .begin5
Precentage=input("please enter logo size in precentage(%):\n").split(" ")
Precentage=float(Precentage[0])
#if type(Precentage)!='float' and type(Precentage)!='int':
    #print("input must be numbers" )
    #goto .begin5
if Precentage<0 or Precentage>100 :
    print(f"logo size range from 0% to 100%" )
    #goto .begin5
Precentage=Precentage/100
# define drawing geometry(center of plate)
DL=(Box_length-2-Bolt_Length*2)*Precentage+Raw_Thickness*4
DW=(Box_width-2-Bolt_Length*2)*Precentage+Raw_Thickness*4
DH=(Box_height-2-Bolt_Length*2)*Precentage+Raw_Thickness*4
if Box_width-3*Raw_Thickness<42*Raw_Thickness:
    print("the logo area is too small to add text")
    #if Back=="Y":
         #goto .begin5
    #elif Back=="N":   
        #goto .begin6
    #else:
        #print("input not defined. only 'Y' or 'N' is allowed")
        #goto .begin5
#label .begin6
C=input("please enter fractual complexily index:\
    (0.5~0.78)\n").split(" ")
C=float(C[0])
#if type(C)!='float' and type(Precentage)!='int':
    #print("input must be numbers" )
    #goto .begin
if C<0 or C>1 :
    print(f"complexily index range from 0.1 to 0.9" )
    #goto .begin6 
#label .begin7  
Input_Text=input(f"please enter text on the top of box:\
    (allow  characters number={round(Box_length/(1.5*Raw_Thickness),0)})\n").split(",")
if len(Input_Text)>Box_length/(1.5*Raw_Thickness):
    print("text too long" )
    #goto .begin7
F_name=input("all set, please enter file name:\n")
print("done. please wait...")
# Define file name/address
Root_address = r'C:\Users\liuch\Desktop\Courses\MECE 4606 Digital manufacturing\HW\Laserbox'
#F_name='draft'
F_address=Root_address +f"\{F_name}.SVG"
Logo='https://yt3.ggpht.com/ytc/AKedOLRSzyfUti-CpOY-d0XZCmXUsdnx2qGWZ8ZvC67-=s900-c-k-c0x00ffffff-no-rj' #columbia logo
# Define raw material and fixation parameters
#Raw_length=457.2
#Raw_width=304.8
#Raw_Thickness=3
# Define fixation components
#Bolt_Slot=3
#Bolt_Length=10   #must > Raw_Thickness*3+Bolt_Slot
Bolt_Tip_Slot=Bolt_Length-Raw_Thickness*2-Bolt_Slot+1
#Bolt_Diameter=1.8
#Bolt_Stopper_Width=5
Sawtooth_Length=max(Raw_Thickness*3,Bolt_Stopper_Width)
# Define box geometry
#Box_length=120
#Box_width=80
#Box_height=66
# define drawing geometry(center of plate)
#Translate px to mm
Raw_length=Raw_length*3.7793
Raw_width=Raw_width*3.7793
Raw_Thickness=Raw_Thickness*3.7793
Bolt_Slot=Bolt_Slot*3.7793
Bolt_Length=Bolt_Length*3.7793
Bolt_Tip_Slot=Bolt_Tip_Slot*3.7793
Bolt_Diameter=Bolt_Diameter*3.7793
Bolt_Stopper_Width=Bolt_Stopper_Width*3.7793
Sawtooth_Length=Sawtooth_Length*3.7793
Box_length=Box_length*3.7793
Box_width=Box_width*3.7793
Box_height=Box_height*3.7793
DL=DL*3.7793
DW=DW*3.7793
DH=DH*3.7793
#Define operation geometry
Direction='X' # another is Y
Sawtooth_Direction=1 # +1 means the first line is extrude;-1 means the first line is groove
r_c=1 # first fixation is groove=1, hole=-1
r_c_p=1 # first sawtooth 1 or second sawtooth 2 for groove/cricle position

#if CC==1:
    #print('Program will exit due to wrong set up characters, please correct')
    #os._exit(0)
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

'''I_X/I_Y: start coordinate
 W:   first branch length
 rot: initial degree with Y axis
 RT: branch separate degree
 C: complex index from most complex 0.9 to 0.1'''
pol=[] # record fracture svg texts
pol_X=[] # record X coordinates
pol_Y=[] # record Y coordinates
def fractal_calc(I_X:float,I_Y:float,W:float,rot:float,RT:float,C:float):
    if C<0.1 or C>0.9:
        print("Err: complex index over the limit (0.1 0.9)")
    elif W>7:
        X1=I_X+W*np.sin(RT*np.pi/180+rot)
        X2=I_X+W*np.sin(-RT*np.pi/180+rot)
        Y1=I_Y+W*np.cos(RT*np.pi/180+rot)
        Y2=I_Y+W*np.cos(-RT*np.pi/180+rot)
        pol_X.append(X1)
        pol_X.append(X2)
        pol_Y.append(Y1)
        pol_Y.append(Y2)
        W=W*C
        fractal_calc(X1,Y1,W,RT*np.pi/180+rot,RT,C)
        fractal_calc(X2,Y2,W,-RT*np.pi/180+rot,RT,C)
def fractal(I_X:float,I_Y:float,W:float,rot:float,RT:float,C:float):
    if C<0.1 or C>0.9:
        print("Err: complex index over the limit (0.1 0.9)")
    elif W>7:
        X1=I_X+W*np.sin(RT*np.pi/180+rot)
        X2=I_X+W*np.sin(-RT*np.pi/180+rot)
        Y1=I_Y+W*np.cos(RT*np.pi/180+rot)
        Y2=I_Y+W*np.cos(-RT*np.pi/180+rot)
        pol.append(f" <line x1='{I_X}' y1='{I_Y}' x2='{X1}' y2='{Y1}' style='stroke:rgb(255,0,0);stroke-width:2' />\n")
        pol.append(f" <line x1='{I_X}' y1='{I_Y}' x2='{X2}' y2='{Y2}' style='stroke:rgb(255,0,0);stroke-width:2' />\n")
        W=W*C
        fractal(X1,Y1,W,RT*np.pi/180+rot,RT,C)
        fractal(X2,Y2,W,-RT*np.pi/180+rot,RT,C)

'''---------function to draw tree fractal---------------'''
#function to calculate right size for fractal pic
#Max_X/Max_Y maximum allowed X/Y coordinates
'''I_X/I_Y: start coordinate
 W:   first branch length
 rot: initial degree with Y axis
 RT: branch separate degree
 C: complex index from most complex 0.9 to 0.1
 dir:+1 from up to down, -1 from down to up'''
pol=[] # record fracture svg texts
pol_X=[] # record X coordinates
pol_Y=[] # record Y coordinates
def fractal_calc(I_X:float,I_Y:float,W:float,rot:float,RT:float,C:float,dir:int):
    if C<0.1 or C>0.9:
        print("Err: complex index over the limit (0.1 0.9)")
    elif W>10:
        X1=I_X+dir*W*np.sin(RT*np.pi/180+rot)
        X2=I_X+dir*W*np.sin(-RT*np.pi/180+rot)
        Y1=I_Y+dir*W*np.cos(RT*np.pi/180+rot)
        Y2=I_Y+dir*W*np.cos(-RT*np.pi/180+rot)
        pol_X.append(X1)
        pol_X.append(X2)
        pol_Y.append(Y1)
        pol_Y.append(Y2)
        W=W*C
        fractal_calc(X1,Y1,W,RT*np.pi/180+rot,RT,C,dir)
        fractal_calc(X2,Y2,W,-RT*np.pi/180+rot,RT,C,dir)
#mian Function to draw fractal
def fractal(I_X:float,I_Y:float,W:float,rot:float,RT:float,C:float,dir:int):
    if C<0.1 or C>0.9:
        print("Err: complex index over the limit (0.1 0.9)")
    elif W>10:
        X1=I_X+dir*W*np.sin(RT*np.pi/180+rot)
        X2=I_X+dir*W*np.sin(-RT*np.pi/180+rot)
        Y1=I_Y+dir*W*np.cos(RT*np.pi/180+rot)
        Y2=I_Y+dir*W*np.cos(-RT*np.pi/180+rot)
        pol.append(f" <line x1='{I_X}' y1='{I_Y}' x2='{X1}' y2='{Y1}' style='stroke:rgb(255,0,0);stroke-width:3' />\n")
        pol.append(f" <line x1='{I_X}' y1='{I_Y}' x2='{X2}' y2='{Y2}' style='stroke:rgb(255,0,0);stroke-width:3' />\n")
        W=W*C
        fractal(X1,Y1,W,RT*np.pi/180+rot,RT,C,dir)
        fractal(X2,Y2,W,-RT*np.pi/180+rot,RT,C,dir)

'''calculate right size for fractal pic
Max_X/Max_Y maximum allowed X/Y coordinates 
dir:+1 from up to down, -1 from down to up'''
def fractal_size(I_X:float,I_Y:float,W:float,rot:float,RT:float,Max_X:float, Max_Y:float,C:float,dir:int):
    SE=0
    WS=W
    if C<0.1 or C>0.9:
        print("Err: complex index over the limit (0.1 0.9)")
    else:
        while SE==0:
            pol_X.clear()
            pol_Y.clear()
            fractal_calc(I_X,I_Y,WS,rot,RT,C,dir)
            if max(pol_X)<Max_X and max(pol_Y)<Max_Y-WS/C:
                SE=1
            WS=WS-3
    return WS

# Define translate function to suitable format for svg
def Tr(Input_D):
    P_svg=(f'{Input_D[0]}')
    for m in range(1 ,len(Input_D)):     
       P_svg=(f"{P_svg},{Input_D[m]}")
    return P_svg    
#define function to input text
'''I_X: start position X
   I_Y: start position Y
   I_F: font size      L:text length   
   I_text: input text  rot: angle to rotate from horizontal'''
def text(I_X:float,I_Y:float,I_F:float, I_text:str,rot:int):
    Main_text=f"<text x='{I_X}' y='{I_Y}' style='text-anchor: middle' transform='rotate({rot} {I_X},{I_Y})' \
         fill='blue' font-size='{I_F}' font-weight='bold' >{I_text}</text>\n"
    
    return Main_text
# Define functions to put picture in
'''I_X:center coordinate  I_Y:center coordinate  
I_pic:Picture link
ROT: Direction of rotation,'X' or 'Y'  
L:length of picture     W:width of picture'''
def pic(I_X:float,I_Y:float,L:float,W:float,I_pic:str,ROT:float):
    Main_text=(f"<image x='{I_X-L/2}' y='{I_Y-W/2}' width='{L}' height='{W}' transform='rotate({ROT} {I_X},{I_Y})' xlink:href='{I_pic}'/>\n")
    return Main_text

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
h2=hole(Raw_Thickness*6+Ad+2.5*Sawtooth_Length,Raw_Thickness*2.5+Box_width)
h3=hole(Raw_Thickness*6+Box_length-Ad-2.5*Sawtooth_Length,Raw_Thickness*2.5+Box_width)
H=H+h2+h3
'''second plate'''
def ref_box(input,Y_axis):
    for p in range(len(input)):
        if p%2==1:
            input[p]=Y_axis*2-input[p]
PA=PL_stream
PA1=tran(P_stream,Raw_Thickness*6,P_stream[1]+Box_height+Raw_Thickness*10)
PA2=tran(PL_stream,Raw_Thickness*6,P_stream[1]+Box_height+Raw_Thickness*10)
PA3=tran(PR_stream,PR_stream[0],P_stream[1]+Box_height+Raw_Thickness*10)
#ref_box(PA1,P_stream[1]+Box_height+Raw_Thickness*9+Box_height/2)
ref_box(PA1,P_stream[1]+Box_height+Raw_Thickness*9+Box_height/2)
ref_box(PA2,P_stream[1]+Box_height+Raw_Thickness*9+Box_height/2)
ref_box(PA3,PL_stream[1]+Box_height*1.5+Raw_Thickness*9)
h1_1=hole(Raw_Thickness*5.5,PA3[len(PA3)-1]+Raw_Thickness*0.5)
h4=hole(Raw_Thickness*6+Ad+2.5*Sawtooth_Length,PA3[1]+Raw_Thickness*0.5)
h5=hole(Raw_Thickness*6+Box_length-Ad-2.5*Sawtooth_Length,PA3[1]+Raw_Thickness*0.5)
H=H+h4+h5
'''Update Main stream'''
Main_stream.append(Tr(P_stream))
Main_stream.append(Tr(PL_stream))
Main_stream.append(Tr(PR_stream))
Main_stream.append(Tr(PA1))
Main_stream.append(Tr(PA2))
Main_stream.append(Tr(PA3))
HL1_X=P_stream_1[0]+Box_length/2                            #center coordinates
HL1_Y=P_stream_1[1]-Raw_Thickness+Box_height/2  
HL2_X=HL1_X
HL2_Y=HL1_Y+Raw_Thickness*10+Box_height

#H x W plates
'''upper length line'''
T_stream_1,tp01,tp02=ST(Raw_Thickness*10+Box_length,Raw_Thickness*2,add-Raw_Thickness,3,-1,"X")
T_stream_2,tp11,tp12=ST(tp01,tp02,Sawtooth_Length,(tnn-2)*2,1,"X")
T_stream_2.append(T_stream_2[len(T_stream_2)-2])
T_stream_2.append(Raw_Thickness*2)
T_stream_2.append(T_stream_2[len(T_stream_2)-2]+add+Sawtooth_Length*2)
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
HW_CX=T_stream_1[0]+(Box_height-Bolt_Length)/2    # center coordinates
HW_CY=T_stream_1[1]+(Box_width-Raw_Thickness*2)/2
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
UP_CX=TU_stream_1[0]+(Box_height-Bolt_Length)/2    # center coordinates
UP_CY=TU_stream_1[1]+(Box_width-Raw_Thickness*2)/2
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
Lid_CX=Lid1[0]+(Lid1[len(Lid1)-2]-Lid1[0]+Raw_Thickness)/2 # center coordinates
Lid_CY=Lid1[len(Lid1)-1]+(Box_width-Raw_Thickness*2)/2
''' ------------draw whole box --------------'''

'''input logo and text'''
PIC_F=pic(UP_CX+Raw_Thickness*3,UP_CY,DH,DW,Logo,90)
PIC_R=pic(HW_CX+Raw_Thickness*3,HW_CY,DH,DW,Logo,90)
PIC_T=pic(Lid_CX,Lid_CY-Raw_Thickness,DL-Raw_Thickness, DW-Raw_Thickness,Logo,0)
TEXT_F=text(UP_CX-DH/2+Raw_Thickness*2,UP_CY,Raw_Thickness*2,"DIGITAL MANUFACTURING",90)
TEXT_R=text(HW_CX-DH/2+Raw_Thickness*2,HW_CY,Raw_Thickness*2,"DIGITAL MANUFACTURING",90)
TEXT_U=text(Lid_CX,Lid_CY+DW/2+Raw_Thickness*2,Raw_Thickness*2,Input_Text[0],0)
'''input fractual drawing'''
BL=fractal_size(HL1_X,HL1_Y-DH/3,800,0,25,HL1_X+DL/2,HL1_Y+DH/2+DH/3+Raw_Thickness*2,C,1)
fractal(HL1_X,HL1_Y-DH/3,BL,0,25,C,1)
fractal(HL2_X,HL2_Y+DH/3,BL,0,25,C,-1)

'''------------Draw SVG file-------------'''
try:
    F=open(F_address, 'x')
except FileExistsError:
    print("Error: File name already exists,can not overwrite file")   
    os._exit(0)   
F.write(f"<svg height='{Box_width+Box_height*2+Raw_Thickness*15}' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='{Box_length+Box_height*2+Raw_Thickness*15}'>\n")
for M in range(len(Main_stream)):
    F.write(f"  <polyline points='{Main_stream[M]}' stroke='black' stroke-width='1' fill='none' />\n")
for n in range(int(len(H)/2)):
    F.write(f"  <circle cx='{H[n*2]}' cy='{H[n*2+1]}' r='{Bolt_Diameter/2}' stroke='black' stroke-width='1' fill='none' />\n")
F.write(f"  <circle cx='{h1[0]}' cy='{h1[1]}' r='{Raw_Thickness*2}' stroke='black' stroke-width='1' fill='none' />\n")
F.write(f"  <circle cx='{h1_1[0]}' cy='{h1_1[1]}' r='{Raw_Thickness*2}' stroke='black' stroke-width='1' fill='none' />\n")
#F.write(f"<image x='{HL1_X}' y='{HL1_Y}' width='50px' height='50px' transform='translate({0},{0}) rotate(0)' xlink:href='{Root_address}\c.svg'/>\n")
F.write(PIC_F)
F.write(PIC_R)
F.write(PIC_T)
F.write(TEXT_F)
F.write(TEXT_R)
F.write(TEXT_U)
for TY in range(len(pol)-1):   #write fractal into svg file
    F.write(pol[TY])
F.write("</svg>")  
print(f"svg file successfully generated! under location:{F_address}")