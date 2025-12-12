import 'dart:typed_data';

import 'package:stateless_statful/src/external/protos/package.pb.dart';

class UserAdapter {
  static List<User> decodeProto(Uint8List encodedUser) {
    try {
      final userList = UserList.fromBuffer(encodedUser);
      return userList.users;
    } catch (e) {
      throw Exception('Error to decode User Proto');
    }
  }

  static Uint8List encodeProto(User user) {
    final encodedUser = user.writeToBuffer();
    return encodedUser;
  }
}
