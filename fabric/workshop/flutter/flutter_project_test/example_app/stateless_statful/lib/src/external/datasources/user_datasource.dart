import 'package:http/http.dart' as http;
import 'package:stateless_statful/src/external/adapters/user_adapter.dart';
import 'package:stateless_statful/src/external/protos/package.pb.dart';
import 'package:stateless_statful/src/external/server_address.dart';

class UserDatasource {
  final client = http.Client();

  Future<List<User>> getUsers() async {
    try {
      final response = await client.get(Uri.parse("$serverAddress/get-users"));
      return UserAdapter.decodeProto(response.bodyBytes);
    } catch (e) {
      throw Exception(e.toString());
    }
  }

  Future<bool> addUser(User user) async {
    final userEncoded = UserAdapter.encodeProto(user);
    final response = await client.post(
      Uri.parse("$serverAddress/add-user"),
      body: userEncoded,
    );

    return response.statusCode == 200;
  }

  Future<bool> removeUser(User user) async {
    final userEncoded = UserAdapter.encodeProto(user);
    final response = await client.post(
      Uri.parse("$serverAddress/remove-user"),
      body: userEncoded,
    );

    return response.statusCode == 200;
  }
}
