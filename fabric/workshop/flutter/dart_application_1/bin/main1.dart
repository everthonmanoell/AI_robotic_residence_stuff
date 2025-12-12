

import 'package:dart_application_1/class_robot.dart';

void main() {
  ClassRobot robot = ClassRobot(1, 3.0);
  print(robot.position);
  print(robot.move(1));
  print(robot.position);
  print(robot.move(0));
  print(robot.position);
  print(robot.move(2));
  print(robot.position);
}