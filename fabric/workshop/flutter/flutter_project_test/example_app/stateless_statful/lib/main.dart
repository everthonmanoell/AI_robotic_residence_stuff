import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:stateless_statful/src/presenter/pages/first_page.dart';
import 'package:stateless_statful/src/presenter/stores/form_store.dart';
import 'package:stateless_statful/src/presenter/stores/frist_store.dart';
import 'package:stateless_statful/src/presenter/stores/second_store.dart';

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (context) => FristStore()),
        ChangeNotifierProvider(create: (context) => SecondStore()),
        ChangeNotifierProvider(create: (context) => FormStore()),
      ],
      child: MainApp(),
    ),
  );
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(home: FirstPage());
  }
}
