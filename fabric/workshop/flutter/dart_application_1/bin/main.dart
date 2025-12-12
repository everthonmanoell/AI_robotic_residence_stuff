import 'package:dart_application_1/niryo.dart';

void main(){
  Niryo robot = Niryo(6, 180, 1.0);
  print(robot.currentPosition);
  robot.movieCartesian(0.3, 0.4);
  print(robot.currentPosition);
  print(robot.joints);
}