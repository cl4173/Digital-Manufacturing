import numpy as np
# Function to create stitch sequence

def col(t):# add color code/t is how many colors whould added
    col=[]
    for s in range(t):
        col.extend([s,0,0,0,])
    col.extend([13,0,0,0])# Thread type (unknown)
    return col

    
def negative(neg):#convert negative distance to byte value 
    reneg=0
    if neg<0:
        reneg=int(1*neg+256)
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
def mov(lx,ly):#move to specified point 
    mov=[]
    leng=np.sqrt(lx*lx+ly*ly)
    if leng>127:
        lx1=int(round(lx/leng,0))
        ly1=int(round(ly/leng,0))
        if lx1<0:
            lx1=negative(lx1)
        if ly1<0:
            ly1=negative(ly1)
        z1=lx//127
        z2=127
        z3=lx%127
        for e1 in range(z1):
            for e2 in range(z2):                       
                mov.extend([lx1,ly1,])
        for e3 in range(z3):
            mov.extend([lx1,ly1,])
    return mov
drag=[]
drag.extend(Com(2))
count=[0]
f=np.sqrt(2)/2
def dra(l,q,z):
    if l*f>2:
        count[0]=count[0]+1
        q=q-45*np.pi/180
        q1=q-90*np.pi/180
        if z==-1:
            drag.extend([l*f*np.cos(q),l*f*np.sin(q),])
            drag.extend([l*f*np.sin(q),-l*f*np.cos(q),])
            drag.extend([128,1])
            dra(l*f,q,-1)
            dra(l*f,q1,1)
        else:
            drag.extend([l*f*np.sin(q1),-l*f*np.cos(q1),]) 
            drag.extend([l*f*np.cos(q1),l*f*np.sin(q1),])
            
            dra(l*f,q,-1)
            dra(l*f,q1,1)



   
dra(250,0,-1)
for o in range(len(drag)):
    drag[o]=(int(round(drag[o],0)))
for t in range(len(drag)):
    if drag[t]<0:
        drag[t]=negative(drag[t])


drag.extend(Com(16))


# Function to create JEF file header

def getJefHeader(num_stitches):
    jefBytes = [    5, 0, 0, 0,   # The byte offset of the first stitch
                    10, 0, 0, 0,   # unknown command
                    ord("2"), ord("0"), ord("2"), ord("1"), #YYYY
                    ord("0"), ord("2"), ord("2"), ord("4"), #MMDD
                    ord("1"), ord("5"), ord("2"), ord("1"), #HHMM
                    ord("0"), ord("0"), 99, 0, #SS00
                    1, 0, 0, 0,   # Thread count nr. (nr of thread changes)
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
    jefBytes.extend(col(75))    
    return jefBytes

#Main program combines headers and stich sequence
# Define file name/address
Root_address = r'C:\Users\liuch\Desktop\Courses\MECE 4606 Digital manufacturing\HW\Embroidery\a.jef'
def main():
    stitchseq= drag

    header = getJefHeader(len(stitchseq)//2)
    data = bytes(header) + bytes(stitchseq)
    with open(Root_address, "wb") as f:
        f.write(data)
if __name__ == '__main__':
    main()
