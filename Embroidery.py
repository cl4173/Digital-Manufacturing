import numpy as np
ll,ww,cc,tt=input('please input length,width,loop number,twist angle: ').split(" ")
ll=int(ll)
ww=int(ww)
cc=int(cc)
tt=int(tt)
cll=input('please input color style: (1,2,3,4,5,6)')
cll=int(cll)
#ll=16
#ww=3
#cc=24
#tt=-8
#cll=3
# Function to create stitch sequence
def col(t,cll):# add color code/t is how many colors whould added
    col=[]
    for s in range(t):
        col.extend([s*7+cll,0,0,0,])
    col.extend([13,0,0,0])# Thread type (unknown)
    return col   
def negative(neg):#convert negative distance to byte value 
    reneg=0
    if neg<0:
        reneg=(1*neg+256)
    else:
        print("not a negative value")
    return reneg
def Com(com):# function commend,1-change thread/2-move forward/16-end stitch
    cth=[128, 16,]
    if com==1:
        cth=[128, 1,]
    elif com==2:
        cth=[128, 2,]
    elif com==16:
        cth=[128, 16]
    return cth
def ellip(a,b,t,q):#draw elliptic/t is resolution/q is rotation angle/m is thickness of line
    X=0
    Y=0
    ell=[]
    Ell=[]
    m=5
    h=3
    j=1
    #ell.extend([x+a,y,])
    step=t
    c=np.cos(np.pi*q/180)
    s=np.sin(np.pi*q/180)
    u=2*np.pi/step
    for i in range(step+2):
        x_0=a*(np.cos((i+1)*u)-np.cos(i*u))
        y_0=b*(np.sin((i+1)*u)-np.sin(i*u))      
        x1=c*x_0+s*y_0
        y1=-s*x_0+c*y_0
        ll=np.sqrt(x1*x1+y1*y1)*0.3
        x_00=-y1/ll*h
        y_00=x1/ll*h
        x11=x1/ll
        y11=y1/ll
        for k in range(int(round(ll,0))+2):
            x13=int(round(x_00*j+x11,0))
            y13=int(round(y_00*j+y11,0))
            X=X+x13
            Y=Y+y13
            Ell.extend([-x13,-y13,])
            if x13<0:
                x13=negative(x13)
            if y13<0:
                y13=negative(y13)
            ell.extend([x13,y13,])
            j=j*(-1)      
    #ell.extend(Com(16))
    return ell,X,Y
def circ(r,t):#draw circle /t is resolution
    cir=[]
    step=t
    #cir.extend([128,2,])
    u=2*np.pi/step
    for i in range(step+2):
        x1=int(round(r*(np.cos((i+1)*u)-np.cos(i*u)),0))
        y1=int(round(r*(np.sin((i+1)*u)-np.sin(i*u)),0))
        if x1<0:
            x1=negative(x1)
        if y1<0:
            y1=negative(y1)
        cir.extend([x1,y1,])
    #cir.extend([128,16,])
    return cir
def fra(l,w,c,t):# draw fractal 
    c1=6
    c2=c
    k=np.pi*2/c1
    fra=[]
    fra.extend(Com(2))
    fra.extend([0,0,])
    for m in range(c1):
        for n in range(c2):
            T1,T2,T3=ellip(l+n*6,w+n*2,90,t*n+m*60)
            fra.extend(T1) 
        fra.extend(Com(1))      
    fra.extend(Com(16))
    return fra
# Function to create JEF file header
def getJefHeader(num_stitches):
    jefBytes = [    204, 0, 0, 0,   # The byte offset of the first stitch
                    10, 0, 0, 0,   # unknown command
                    ord("2"), ord("0"), ord("2"), ord("1"), #YYYY
                    ord("0"), ord("2"), ord("2"), ord("4"), #MMDD
                    ord("1"), ord("5"), ord("2"), ord("1"), #HHMM
                    ord("0"), ord("0"), 99, 0, #SS00
                    210, 0, 0, 0,   # Thread count nr. (nr of thread changes)
                    (num_stitches) & 0xff, (num_stitches) >> 8 & 0xff, 0, 0, # Number of stitches
                      3, 0, 0, 0, # Sewing machine Hoop
                    # Extent 1
                     0, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     0, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     0, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     0, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 2
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 3
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 4
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                    # Extent 5
                     50, 0, 0, 0, # Left boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Top boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Right boundary dist from center (in 0.1mm)
                     50, 0, 0, 0, # Bottom boundary dist from center (in 0.1mm)
                      #9, 0, 0, 0, # Thread Color (white)
                     # 20, 0, 0, 0, # Thread Color (white)
                     # 65, 0, 0, 0, # Thread Color (white)
                     # 63, 0, 0, 0, # Thread Color (white)
                     # 42, 0, 0, 0, # Thread Color (white)
                     # 40, 0, 0, 0, # Thread Color (white)
                     #13, 0, 0, 0, # Thread type (unknown)
                ]
    jefBytes.extend(col(6,cll))    
    return jefBytes
#Main program combines headers and stich sequence
# Define file name/address
Root_address = r'C:\Users\liuch\Desktop\Courses\MECE 4606 Digital manufacturing\HW\Embroidery\a.jef'
def main():
    stitchseq= fra(ll,ww,cc,tt)
    header = getJefHeader(len(stitchseq)//2)
    data = bytes(header) + bytes(stitchseq)
    with open(Root_address, "wb") as f:
        f.write(data)
if __name__ == '__main__':
    main()
