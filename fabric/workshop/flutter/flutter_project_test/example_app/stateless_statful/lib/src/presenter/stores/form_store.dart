import 'package:flutter/foundation.dart';
import 'package:stateless_statful/src/external/datasources/user_datasource.dart';
import 'package:stateless_statful/src/external/protos/package.pbserver.dart';

class FormStore extends ChangeNotifier {
  final userDatasource = UserDatasource();

  var _users = <User>[];

  List<User> get users => _users;

  var _errorMessage = '';

  String get errorMessage => _errorMessage;

  Future<void> getUsers() async {
    try {
      _users = await userDatasource.getUsers();
    } catch (e) {
      _errorMessage = e.toString();
    }
    notifyListeners();
  }

  Future<void> addUser(String name, String email, String address) async {
    final user = User(name: name, email: email, address: address);
    try {
      final response = await userDatasource.addUser(user);
      if (response) {
        getUsers();
      }
    } catch (e) {
      _errorMessage = e.toString();
    }
  }

  Future<void> removeUser(User user) async {
    try {
      final response = await userDatasource.removeUser(user);
      if (response) {
        getUsers();
      }
    } catch (e) {
      _errorMessage = e.toString();
    }
  }

  void clearInformations() {
    addUser('', '', '');
  }
}
