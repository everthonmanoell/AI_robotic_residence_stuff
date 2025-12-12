import 'package:flutter/material.dart';
import 'package:project_everthon/src/presenter/pages/first_page.dart';
import 'package:project_everthon/src/presenter/pages/form_page.dart';
import 'package:project_everthon/src/presenter/pages/second_page.dart';
import 'package:project_everthon/src/presenter/stores/second_store.dart';
import 'package:project_everthon/src/presenter/stores/form_store.dart';
import 'package:provider/provider.dart';
// import 'package:project_everthon/src/presenter/pages/first_page.dart';


void main() {
  runApp(
    MultiProvider(
      providers: [
        // ChangeNotifierProvider(create: (context) => SecondStore()),
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
    return MaterialApp(home: FormPage(),);
  }
}
