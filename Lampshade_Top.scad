$fn=50;
cylinder_L=90;//length
cylinder_W=25;//width
cylinder_H=35;
radi_X=cylinder_L+15;//convex X,top point
radi_Z=50;//convex Z
radi_Y=40;//convex Y
TT=3;//thickness
TW=3;//line width
LK=15;//how many pieces
LL=6;//how many layers
Agl=18;//start angle
offset_Z=TT;//offset layers
conn_H=65;//height of connection

module apc(cylinder_L,cylinder_W,cylinder_H,radi_X,radi_Y,radi_Z,TT,TW,LK,Agl,offset_Z){//build layers of features
for(s1=[0:1:LK-1]){
    rotate([0,0,360*s1/LK]){

translate([radi_Y/2,0,offset_Z]){
rotate([0,Agl,0]){
translate([0,0,-radi_Z/2]){
intersection(){
difference(){    
resize([cylinder_L,cylinder_W,cylinder_H])//outside
cylinder(h=30,r1=20,r2=20,center=false);   
resize([cylinder_L-TW,cylinder_W-TW,cylinder_H+5])//inside
cylinder(h=30,r1=20,r2=20,center=false);
}

difference(){
resize([radi_X,radi_Y,radi_Z])//outside shell
sphere(r=20);
resize([radi_X-TT,radi_Y-TT,radi_Z-TT])//inside shell
sphere(r=20);
             }
       }
     }
   }
  }
 }
}
}

/*------------------------------------------------------*/
union(){

for(l1=[0:1:LL-1]){
    color( [0.4+l1*0.1, 0.15+l1*0.06, 0.35+l1*0.13] )
    rotate([0,0,l1*15])
apc(cylinder_L*0.8^l1,cylinder_W*0.8^l1,cylinder_H*0.8^l1,radi_X*0.8^l1,radi_Y*0.8^l1,radi_Z*0.8^l1,TT,TW,LK,Agl+8*l1,-offset_Z*l1);
                   }
                   
translate([0,0, conn_H/2-9]){ 
intersection(){    
cube([4.5,71,conn_H-18],center=true);//connection plates
cylinder(h=conn_H-18,r1=12,r2=5,center=true);                
               }   
                            }
                            
                          
translate([0,0, conn_H/2-9]){  
intersection(){     
cube([71,4.5,conn_H-18],center=true);//connection plates     
cylinder(h=conn_H-18,r1=8,r2=8,center=true); }                 
              }      
translate([0,0, conn_H-9])             
cube([71,4.5,18],center=true);                    
                     
         }                   
                     
                     
                     
                     
                     
                     
                     
                          