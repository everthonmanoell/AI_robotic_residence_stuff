import 'package:dart_application_1/dart_application_1.dart' as dart_application_1;

void main(List<String> arguments) async {
  print('Hello world: ${dart_application_1.calculate()}!');
  print('${dart_application_1.sumAB(1,2)}');
  print('${dart_application_1.subAb(1,2)}');
  print('${dart_application_1.multAb(1,2)}');
  print('${await dart_application_1.divAb(1, 2)}');
  print('${await dart_application_1.divAb(1, 0)}');
}
