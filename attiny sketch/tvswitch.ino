boolean mosFet = false;

void setup()
{
  pinMode(0, INPUT); //5v from tv usb
  pinMode(3, INPUT); //rpi gpio out pin

  pinMode(1, OUTPUT); //gate on p-channel mosfet
  pinMode(4, OUTPUT); //rpi gpio in pin
  
  digitalWrite(1, HIGH); //default mosfet off
}

void loop()
{
  if (digitalRead(3) && digitalRead(0) && !mosFet) { //if rpi gpio is low and tv is on
    mosFet = true;
    digitalWrite(1, LOW); //turn on mosfet
  }

  if (!digitalRead(3) && !digitalRead(0) && mosFet) { //if rpi gpio is pulled high and tv is off
    digitalWrite(4, HIGH); //set out pin to rpi high
    mosFet = false;
    while (!digitalRead(3)) { //wait for rpi to shutdown
    }
    delay(10000);
    digitalWrite(1, HIGH); //turn off mosfet
  }
  else {
    digitalWrite(4, LOW);
  }
}
