import 'package:flutter/material.dart';
import 'package:project_everthon/src/presenter/pages/second_page.dart';

class FirstPage extends StatefulWidget {
  const FirstPage({super.key});

  @override
  State<FirstPage> createState() => _FirstPageState();
}

class _FirstPageState extends State<FirstPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        mainAxisAlignment:  MainAxisAlignment.center,
        children: [
          Column(
            
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              
              Text('First Page'),
              ElevatedButton(onPressed: (){
                Navigator.push(
                  context, MaterialPageRoute(builder: (context) => SecondPage()),
                  );
              }, child: Text('Go to Second Page'))
            ],
          ),
        ],
      ),
    );
  }
}