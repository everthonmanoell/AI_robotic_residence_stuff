import 'package:http/http.dart' as http;
import 'package:project_everthon/src/external/adapters/user_adapter.dart';
import 'package:project_everthon/src/external/proto/package.pb.dart';

class UserDatasource {
  final user = http.Client();

  // Método para recuperar as informações do usuário da API
  Future<User> showInformations() async {
    try {
      // Faz uma requisição GET para o endpoint especificado
      final response = await user.get(
        Uri.parse('http://127.0.0.1:8000/show-informations'),
      );
      // Retorna os bytes se a requisição foi bem-sucedida
      if (response.statusCode == 200) {
        return UserAdapter.decodeProto(response.bodyBytes);
      } else {
        throw Exception('Server can\'t process request');
      }
    } catch (e) {
      throw Exception('Can\'t connect to server');
    }
  }

  // Método para atualizar as informações do usuário na API
  Future<bool> updateInformations(User userToUpdate) async {
    try {
      final response = await user.post(
        Uri.parse('http://127.0.0.1:8000/update-informations'),
        body: UserAdapter.encodeProto(userToUpdate),
        
        // headers: {'Content-Type': 'application/octet-stream'},
      );
      return response.statusCode == 200;
    } catch (e) {
      throw Exception('Can\'t connect to server');
    }
  }
}

