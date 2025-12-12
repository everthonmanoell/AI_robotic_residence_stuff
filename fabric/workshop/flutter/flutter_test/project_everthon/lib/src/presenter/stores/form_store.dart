import 'package:flutter/material.dart';
import 'package:project_everthon/src/external/datasource/user_datasource.dart';
import 'package:project_everthon/src/external/proto/package.pb.dart';

class FormStore extends ChangeNotifier {
  final userDatasource = UserDatasource();
  User _user = User(name: '', email: '', address: '');
  String errorMessage = '';
  bool isLoading = false;


  User get user => _user;

  // Buscar informações do usuário da API
  Future<void> showInformations() async {
    isLoading = true;
    errorMessage = '';
    
    
    try {
      final user = await userDatasource.showInformations();
      _user = user;
    } catch (e) {
      errorMessage = e.toString();
    } finally {
      isLoading = false;
      notifyListeners();
    }
  }

  // Salvar informações do usuário na API
  Future<bool> saveUserInformations(String name, String email, String address) async {
    User user = User(name: name, email: email, address: address);
    isLoading = true;
    errorMessage = '';
    

    try {
      final success = await userDatasource.updateInformations(user);
      if (!success) {
        errorMessage = 'Falha ao salvar informações';
      }
      showInformations();
      return success;
    } catch (e) {
      errorMessage = e.toString();
      return false;
    } finally {
      isLoading = false;
      notifyListeners();
    }
  }

  // Limpar mensagem de erro
  void clearError() {
    errorMessage = '';
    notifyListeners();
  }
}
