//week10_1_happy_bubble_part2
PImage toy1,toy2,toy3;
//int a,b;
void setup(){
  size(400,453);
  toy1 = loadImage("toy1.jpg");
  toy2 = loadImage("toy2.jpg");
}
void draw(){
  background(toy1);
  if(toy3 !=null) image(toy3,0,0);
}
void mousePressed(){
  toy3 = toy2.get(mouseX, mouseY, 100,100);
}
