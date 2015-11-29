#include <Bridge.h>
#include <HttpClient.h>
#include <ZumoMotors.h>

ZumoMotors motors;

void setup() {
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  Bridge.begin();
  Serial.begin(9600);
  // while (!Serial);
}

void loop() {

  int goalDist = getGoalDistance();
  int totalDist = getTotalDistance();

  Serial.print(goalDist);
  Serial.print(" vs ");
  Serial.println(totalDist);

  //---if the value reaches the goal
  if (totalDist > goalDist) {
    digitalWrite(13, HIGH);

    int steps = 12;
    for (int i = 0; i < steps; i++) {
      forward(200);
      delay(3000);
    }
    exit(0);
  };

  //---check for every three seconds
  Serial.flush();
  int seconds = 3;
  int milSeconds = seconds * 1000;
  delay(milSeconds);

}

int getGoalDistance() {
  HttpClient client;

  //---build URL
  String domain = "http://myserver.com";
  String file = "/projects/goalrobot/www/py/getTarget.py";
  String url = domain + file;

  Serial.println(url);

  //---get a value from the server
  client.get(url);

  //---char to string to int
  String numStr = "";
  while (client.available()) {
    char c = client.read();
    numStr += c;
  };
  int dist = atoi(numStr.c_str());

  return dist;
}

int getTotalDistance() {

  HttpClient client;

  //---build URL
  String domain = "http://myserver.com";
  String file = "/projects/goalrobot/www/py/getDistance.py";
  String param = "?activity=total";
  String url = domain + file + param;

  //---get a value from the server
  client.get(url);

  //---char to string to int
  String numStr = "";
  while (client.available()) {
    char c = client.read();
    numStr += c;
  };

  int dist = atoi(numStr.c_str());

  return dist;
}


void forward(int dist) {

  for (int speed = 0; speed <= -dist; speed--) {
    motors.setRightSpeed(speed);
    motors.setLeftSpeed(speed);
    delay(2);
  }

  for (int speed = -dist; speed <= 0; speed++) {
    motors.setRightSpeed(speed);
    motors.setLeftSpeed(speed);
    delay(2);
  }
}


