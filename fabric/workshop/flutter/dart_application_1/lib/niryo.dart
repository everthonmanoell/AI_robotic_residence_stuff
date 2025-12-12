import 'package:dart_application_1/robot.dart';
import 'dart:math';

import 'package:path/path.dart';

// ● Criar classe Niryo em um arquivo separado, essa classe precisa herdar de Robot:
// ○ Atributos:
// ■ Um atributo privado para armazenar o workspace do robô (medidos em metros)
// ■ Um atributo privado, para armazenar a posição atual de x e y, iniciado com 0
// ■ Um atributo privado para armazenar o limite de juntas do robô em graus

// ○ O construtor precisa receber o valor de graus de liberdades, herdados da classe Robot, o
// valor para o limite das juntas e o valor que representa o workspace do robô. Dentro do
// construtor, inicie os valores de juntas, preenchendo os valores com zero, usando a função
// .addAll(List.generate(dof_do_robô, (index) => 0)) para a lista das juntas.
// ○ Métodos de acesso:
// ■ Fazer um get para o atributo que armazena a posição atual (currentPosition)
// ■ Fazer um get que retorna o valor das juntas em metros (workspace / graus de liberdade - 1).
class Niryo extends Robot{
  late double _workspace;
  late List<double> _position = [0.0, 0.0];
  late double _joint_limit;

  Niryo(
    super._dof,
    this._joint_limit,
    this._workspace
  ){
    joints.addAll(List.generate(dof.toInt(), (index) => 0));
  }


  List<double> get currentPosition => _position;
  double get jointsInMeters => _workspace / (dof - 1);
  

  @override
  bool moveJoints(List<double> graus){
    if (graus.length <= dof){
      for (var g in graus){
        if (g < 0 || g > _joint_limit) {
          return false;
        }
      }
      joints.clear();
      joints.addAll(graus);
      return true;
    }
    return false;

  }

  double getAngleRoutation(double x, double y){
    double radiating = atan2(y, x);
    double degree = (radiating * _joint_limit / pi);

    return degree;
    
  }

  double linearAngleValue(double x, double y){
    double correctionFactor = jointsInMeters / _workspace;

    if (x == 0 && y == 0){
      return 0;
    }
    else if(x == 0){
      return (y * correctionFactor * _joint_limit / jointsInMeters);
    }
    else if(y == 0){
      return (x*correctionFactor * _joint_limit /jointsInMeters);

    }
    else{
      return ((x+y)/2 * correctionFactor * _joint_limit / jointsInMeters);
    }
    
  }

  bool movieCartesian(double x, double y){
    if (x > _workspace || y > _workspace){
      return false;
    }
    else{
      double angleRoutation = getAngleRoutation(x, y); 
      joints[0] = angleRoutation.truncateToDouble();
      double linearAngle  = linearAngleValue(x, y);


      //update the value
      for (int i = 1; i < joints.length; i++) {
        joints[i] = linearAngle.truncateToDouble();
      }

      currentPosition[0] = x.toDouble();
      currentPosition[1] = y.toDouble();

      return true;      

      
    }
  }
}