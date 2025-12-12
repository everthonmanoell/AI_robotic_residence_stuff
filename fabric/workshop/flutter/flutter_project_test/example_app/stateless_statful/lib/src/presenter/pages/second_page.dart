import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:stateless_statful/src/presenter/stores/second_store.dart';

class SecondPage extends StatefulWidget {
  const SecondPage({super.key});

  @override
  State<SecondPage> createState() => _SecondPageState();
}

class _SecondPageState extends State<SecondPage> {
  final _controller = TextEditingController(text: '');

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          Text(context.watch<SecondStore>().textScreen),
          SizedBox(
            width: 400,
            child: TextField(
              controller: _controller,
              decoration: InputDecoration(border: OutlineInputBorder()),
            ),
          ),
          ElevatedButton(
            onPressed: () {
              context.read<SecondStore>().updateText(_controller.text);
            },
            child: Text('Update'),
          ),
          ElevatedButton(
            onPressed: () {              
              Navigator.pop(context);
            },
            child: Text('Back to First Page'),
          ),
        ],
      ),
    );
  }
}
