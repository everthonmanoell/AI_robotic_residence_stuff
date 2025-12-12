import 'package:flutter/material.dart';
import 'package:project_everthon/src/presenter/stores/second_store.dart';
import 'package:provider/provider.dart';

class SecondPage extends StatefulWidget {
  const SecondPage({super.key});

  @override
  State<SecondPage> createState() => _SecondPageState();
}

class _SecondPageState extends State<SecondPage> {
  final _controler = TextEditingController();
  var _textScreen = 'Second Page';


  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          leading: IconButton(onPressed: (){
            Navigator.pop(context);
          },
          icon: Icon(Icons.arrow_back_ios)),
          backgroundColor: Colors.teal,
        ),
        body: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Center(
            child: Column(
              children: [
                SizedBox(
                  width: 300,
                  child: TextField(
                    controller: _controler,
                    decoration: InputDecoration(
                      labelText: 'my lable',
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(20)
                      )
                    ),
                  ),
                ),
                Text(context.watch<SecondStore>().textScreen),
                ElevatedButton(
                  onPressed: () {
                    context.read<SecondStore>().updateText(_controler.text);
                  },
                  child: Text('Update'),
                )
              ],
            ),
          ),
        ),
    );
  }
}