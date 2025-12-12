import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:stateless_statful/src/presenter/stores/form_store.dart';

class FormPage extends StatefulWidget {
  const FormPage({super.key});

  @override
  State<FormPage> createState() => _FormPageState();
}

class _FormPageState extends State<FormPage> {
  final _controllerName = TextEditingController(text: '');
  final _controllerEmail = TextEditingController(text: '');
  final _controllerAddress = TextEditingController(text: '');

  @override
  void initState() {
    context.read<FormStore>().getUsers();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Formulário'),
        backgroundColor: Colors.blueAccent,
      ),
      body: Stack(
        children: [
          Opacity(
            opacity: 0.5,
            child: Image(
              image: AssetImage('assets/image.png'),
              repeat: ImageRepeat.repeat,
              width: double.maxFinite,
              height: double.maxFinite,
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                Expanded(
                  child: Padding(
                    padding: const EdgeInsets.only(bottom: 16.0),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        TextField(
                          controller: _controllerName,
                          decoration: InputDecoration(
                            label: Text('Name'),
                            border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(10),
                            ),
                          ),
                        ),
                        TextField(
                          controller: _controllerEmail,
                          decoration: InputDecoration(
                            label: Text('E-mail'),
                            border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(10),
                            ),
                          ),
                        ),
                        TextField(
                          controller: _controllerAddress,
                          decoration: InputDecoration(
                            label: Text('Address'),
                            border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(10),
                            ),
                          ),
                        ),
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                          children: [
                            OutlinedButton(
                              onPressed: () {
                                setState(() {
                                  _controllerName.clear();
                                  _controllerEmail.clear();
                                  _controllerAddress.clear();
                                });
                              },
                              child: Text('Cancel'),
                            ),
                            ElevatedButton(
                              onPressed: () {
                                context.read<FormStore>().addUser(
                                  _controllerName.text,
                                  _controllerEmail.text,
                                  _controllerAddress.text,
                                );
                                _controllerName.clear();
                                _controllerEmail.clear();
                                _controllerAddress.clear();
                              },
                              child: Text('Confirm'),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                ),
                Expanded(
                  child: Container(
                    decoration: BoxDecoration(
                      border: Border.all(color: Colors.black),
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Column(
                        children: [
                          Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [Text('Dados')],
                          ),
                          Expanded(
                            child: ListView.builder(
                              itemCount: context
                                  .watch<FormStore>()
                                  .users
                                  .length,
                              itemBuilder: (context, index) {
                                final user = context
                                    .read<FormStore>()
                                    .users[index];

                                return ListTile(
                                  onTap: () {
                                    context.read<FormStore>().removeUser(user);
                                  },
                                  title: Column(
                                    children: [
                                      Row(
                                        children: [
                                          Text('Nome:'),
                                          Text(
                                            user.name,
                                            style: TextStyle(
                                              fontWeight: FontWeight.bold,
                                            ),
                                          ),
                                        ],
                                      ),
                                      Row(
                                        children: [
                                          Text('E-mail:'),
                                          Text(
                                            user.email,
                                            style: TextStyle(
                                              fontWeight: FontWeight.bold,
                                            ),
                                          ),
                                        ],
                                      ),
                                      Row(
                                        children: [
                                          Text('Address:'),
                                          Text(
                                            user.address,
                                            style: TextStyle(
                                              fontWeight: FontWeight.bold,
                                            ),
                                          ),
                                        ],
                                      ),
                                    ],
                                  ),
                                );
                              },
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
