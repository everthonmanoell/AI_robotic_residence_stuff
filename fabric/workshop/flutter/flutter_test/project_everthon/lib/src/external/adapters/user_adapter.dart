import 'package:project_everthon/src/external/proto/package.pb.dart';
import 'dart:typed_data';

class UserAdapter {
  static User decodeProto(Uint8List encondeUser){
    try{
      final user = User.fromBuffer(encondeUser);
      return user;
    }
    catch(e){
      throw Exception("Filed on decodifier proto");
    }
  }

  static Uint8List encodeProto (User user){
    final encodeUser = user.writeToBuffer();
    return encodeUser;
  }
}

