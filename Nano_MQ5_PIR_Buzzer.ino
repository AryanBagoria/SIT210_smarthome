#define MQ A7
#define PIR 2
#define LED 3
#define Buzz 4

void setup() {
pinMode(MQ,INPUT);
pinMode(PIR,INPUT);
Serial.begin(9600);
pinMode(LED,OUTPUT);
pinMode(Buzz,OUTPUT);

}
int flag=0,td1=0;
int f1=1,f2=1;
void loop() {

  if (Serial.available()) {
     char Val = (char)Serial.read(); 
     if (Val>=49 && Val<=50)
     {
       if (flag!=Val){
           flag=Val;           
       if (Val==49)
         {td1=1;} 
        if (Val==50)
        {td1=0;}         
        digitalWrite(LED, td1);               
       }
     }
   } 

   
  int MQ5=analogRead(MQ);
  MQ5=map(MQ5,0,1023,0,100);  
  int PD=digitalRead(PIR);
  if (PD==1 && f1==0){
    Serial.println("P");
     }
  if (PD==0 && f1==1){
    f1=0;
    }
  if (MQ5>50 && f2==0){
    Serial.println("G");
    f2=1;
    }
  if (MQ5<50 && f2==1){
    f2=0;
    }      
  
  if(MQ5>50){  
    digitalWrite(Buzz,HIGH); 
    delay(200); 
    digitalWrite(Buzz,LOW); 
    delay(200); 
    digitalWrite(Buzz,HIGH); 
    delay(200); 
    digitalWrite(Buzz,LOW); 
    delay(200); 
    digitalWrite(Buzz,HIGH); 
    delay(200); 
    digitalWrite(Buzz,LOW); 
    delay(200);      }    
   else{digitalWrite(Buzz,LOW);} 
   
   
   delay(500);

}
