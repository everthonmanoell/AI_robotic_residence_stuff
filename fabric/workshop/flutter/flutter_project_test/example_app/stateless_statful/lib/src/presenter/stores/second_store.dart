import 'package:flutter/foundation.dart';

class SecondStore extends ChangeNotifier {
  var _textScreen = 'Second Page';

  String get textScreen => _textScreen;

  void updateText(String text) {
    _textScreen = text;
    notifyListeners();
  }
}
