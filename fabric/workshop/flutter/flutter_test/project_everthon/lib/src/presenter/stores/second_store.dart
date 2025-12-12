import 'package:flutter/material.dart';

class SecondStore extends ChangeNotifier {
  var _textScreen = 'Second Page';

  String get textScreen => _textScreen;

  void updateText(String newText){
    _textScreen = newText;
    notifyListeners();
  }

}