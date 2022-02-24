/*outside layers-first*/

L2=35;  // how many lines created
Diameter_all=500; // overall diameter
Margin_all=5;// margin added 
Width_in=2;  //thickness of ribs
Height_in=75*2;//height of ribs
Twist_in=60;//twist degree
T_in=3;// thickness
Diameter_1=200;//first layer ball diameter(internal)
Diameter_2=Diameter_1+T_in;//second layer ball diameter(external)
$fn=200;
difference(){
union(){
difference(){
intersection(){//first layer
 difference(){
  difference(){//first layer shell         
     sphere(r=Diameter_2/2,$fn=200);//create outside shells
     sphere(r=Diameter_1/2,$fn=200);//create inside shells
          }
     }      

    union(){
    translate([0,0,Height_in/4])   
    for(q=[1:1:L2]){// create ribs
        linear_extrude(height = Height_in/2, center = true, convexity = 10,slices = 200,twist=Twist_in)
        rotate(a=[0,0,q*180/L2])
            square([Diameter_all+Margin_all,Width_in],center=true);
                   }
    translate([0,0,(Height_in-T_in)/2])//create top ring
        cylinder(T_in,r=Diameter_1);          
          }                 
         }  
 
         
/*--------------------- pentagram-------------------------------------------*/
ar=30;//radius of pentagram
tr=ar*(1+tan(18)*tan(18))/(3-tan(18)*tan(18));

union(){
  for(a1=[1:1:2]){
        rotate([60*a1,0,0])
        linear_extrude(height = Diameter_all, center = true, convexity = 12,slices = 10,twist=0)
        polygon([[0,ar],[cos(54)*tr,sin(54)*tr],[cos(18)*ar,sin(18)*ar],[cos(18)*tr,-sin(18    )*tr],[cos(54)*ar,-sin(54)*ar],[0,-tr],[-cos(54)*ar,-sin(54)*ar],[-cos(18)*tr,-sin(    18)*tr],[-cos(18)*ar,sin(18)*ar],[-cos(54)*tr,sin(54)*tr]],convexity=12);     
       }  
   }
 }   
/*--------------------- pentagram-------------------------------------------*/
         
          
         

/*----------------------------------------------------*/             
Width_out=Width_in;  //thickness of ribs
Height_out=Height_in;//height of ribs
Twist_out=-Twist_in;//twist degree
T_out=T_in;// thickness
D=2; //joint area between first layer to second layer
Diameter_3=Diameter_2-D;//third layer ball diameter(internal)
Diameter_4=Diameter_3+T_out;//fourth layer ball diameter(external)   
difference(){ 
intersection(){//fourth layer
  difference(){//third layer shell         
     sphere(r=Diameter_4/2,$fn=200);//create outside shells
     sphere(r=Diameter_3/2,$fn=200);//create oinside shells
          }
    union(){
    translate([0,0,Height_out/4]) 
    for(k=[1:1:L2]){// create ribs
        linear_extrude(height = Height_out/2, center = true, convexity = 10,slices = 200,twist=Twist_out)
        rotate(a=[0,0,k*180/L2])
            square([Diameter_all+Margin_all,Width_out],center=true);
                   }
          }   
             }
             
/*--------------------- pentagram-------------------------------------------*/
ar=30;//radius of pentagram
tr=ar*(1+tan(18)*tan(18))/(3-tan(18)*tan(18));
union(){
  for(a2=[1:1:2]){
        rotate([60*a2,0,90])
        linear_extrude(height = Diameter_all, center = true, convexity = 12,slices = 200,twist=0)
        polygon([[0,ar],[cos(54)*tr,sin(54)*tr],[cos(18)*ar,sin(18)*ar],[cos(18)*tr,-sin(18    )*tr],[cos(54)*ar,-sin(54)*ar],[0,-tr],[-cos(54)*ar,-sin(54)*ar],[-cos(18)*tr,-sin(    18)*tr],[-cos(18)*ar,sin(18)*ar],[-cos(54)*tr,sin(54)*tr]],convexity=12);     
       }  
   }
}   
/*--------------------- pentagram-------------------------------------------*/
}            
 

margin_D=5;//bottom margin
translate([0,0,-Height_in/2-margin_D])//reduce bottom
cylinder(Height_in,d1=Diameter_all,d2=Diameter_all,center=true);
}

/*--------------------- bottom-------------------------------------------*/
bottom_T=3;//bottom line thickness
L3=15;//lines on bottom
translate([0,0,-5/2]){
difference(){
cylinder(bottom_T,d1=Diameter_2+T_in,d2=Diameter_2+T_in,center=true);
cylinder(bottom_T+2,d1=Diameter_2-T_in,d2=Diameter_2-T_in,center=true);
            }
                     }
linear_extrude(height = bottom_T, center = true, convexity = 10,slices = 200,twist=0)
for(ey=[1:1:20]){
    rotate([0,0,ey*360/L3])
    square([Diameter_2-T_in,Width_in*4],center=true);    
                }           
            
           
 /*-----------------------center components-------------------------*/L1=4;  
/*center disk*/

L11=8;  // how many lines created
Diameter=88; // candle diameter
Margin=5;// margin from candle to disk outside surface
Width=15;  //thickness of ribs
Height=38;//height of ribs
Twist_A=60;//twist degree
Diameter_B=Diameter+Margin;//bottom plate diameter
T=3;// final disk thickness
translate([0,0,Height/2]){
difference(){// reduce negative disk
  union(){
    for(t=[1:1:L11]){// create ribs
        linear_extrude(height = Height, center = true, convexity = 10,    slices = 200,twist=Twist_A)
        rotate(a=[0,0,t*180/L1])
            square([Diameter+Margin,Width],center=true);
                   }
    translate([0,0,Height/2+T/4-0.002])//top ring
    difference(){
    cylinder(h=T*2,r=(Diameter+Margin)/2,center=true);
    cylinder(h=T*2+2,r=(Diameter)/2,center=true);
                }
     translate([0,0,-Height/2+T/2])   //bottom plate       
     cylinder(h=(T+0.002),r=(Diameter_B)/2,center=true);
          }   
  union(){ // create negative holes  
    k=ceil((Height-T+10)/(Width/2))-1;

   for(u=[1:1:k-1]){
               translate([0,0,T-Height/2+10+(u-1)*(Width/2)])
     for(e=[1:1:L1]){

        rotate(a=[0,0,Twist_A/(-Height/(T+10+(u-1)*(Width/2)))])
        rotate(a=[0,90,e*180/L1])
        rotate(a=(u-1)*Twist_A)
        linear_extrude(height = Diameter+Margin+10, center = true,       convexity = 10,slices = 200,twist=Twist_A)
        resize([Width/(2.5)+Width/8*(u/k),Width/(3.5)+Width/10*(u/k)])// increasing hole size
            circle(r=Width/3);}
          }
      }  
translate([0,0,T])//create negative candle
cylinder(h=Height,r1=Diameter/2,r2=(Diameter+5)/2,center=true);
}
}
             
             
             
             
             