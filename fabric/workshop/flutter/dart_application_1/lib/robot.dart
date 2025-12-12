abstract class Robot{
  late int _dof;
  List<double> _joints = [];

  Robot(this._dof);

  int get dof => _dof;
  List<double> get joints => _joints;

  bool moveJoints(List<double> graus);

}