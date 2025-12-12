class ClassRobot {
  final int dof;
  final double workspace;
  double _position = 0.0;

  ClassRobot(this.dof, this.workspace);

  double get position => _position;

  bool move(double valor){
    if (valor >= 0.0 && valor <= 1.0){
      _position = valor;
      return true;
    }
    return false;
  }
  
}