import 'package:flutter/material.dart';
import 'package:project_everthon/src/external/proto/package.pb.dart';
import 'package:project_everthon/src/presenter/stores/form_store.dart';
import 'package:provider/provider.dart';

class FormPage extends StatefulWidget {
  const FormPage({super.key});

  @override
  State<FormPage> createState() => _FormPageState();
}

class _FormPageState extends State<FormPage> {
  @override
  void initState() {
  super.initState();
  context.read<FormStore>().showInformations();

  }

  

  final String _textScreen = "Formulário";
  final String _textDados = 'Dados';
  final String _textName = "Name";
  final String _textEmail = "E-mail";
  final String _textAddress = 'Address';
  final double _borderRadius = 10;

  final double _dataOutputSize = 18;

  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _addressController = TextEditingController();

  

  void _onConfirm(BuildContext context) {

    setState(() {
    User user = User(
    name: _nameController.text,
    email: _emailController.text,
    address: _addressController.text,
    );

      context.read<FormStore>().saveUserInformations(user.name, user.email, user.address);
      
      // _dadosName = _nameController.text;
      // _dadosEmail = _emailController.text;
      // _dadosAddress = _addressController.text;
    });
  }

  void _onCancel() {
    setState(() {
      _nameController.clear();
      _emailController.clear();
      _addressController.clear();
      
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(_textScreen, style: const TextStyle(fontSize: 30)),
        backgroundColor: Colors.purple[100],
        
      ),
      body: Stack(
        
        children: [
          Opacity(
            opacity: 0.5,
            child: Image(
              repeat: ImageRepeat.repeat,
              width: double.maxFinite,
              height: double.maxFinite,
              image: const AssetImage('assets/image.png')),
          ),
          Padding(
            padding: const EdgeInsets.all(25.0),
            child: Center(
              child: Column(
                children: [
                  SizedBox(
                    child: TextField(
                      controller: _nameController,
                      decoration: InputDecoration(
                        labelText: _textName,
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(_borderRadius),
                        ),
                      ),
                    ),
                  ),
                  const Padding(padding: EdgeInsets.symmetric(vertical: 5)),
                  SizedBox(
                    child: TextField(
                      controller: _emailController,
                      decoration: InputDecoration(
                        labelText: _textEmail,
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(_borderRadius),
                        ),
          
                      ),
                    ),
                  ),
                  const Padding(padding: EdgeInsets.symmetric(vertical: 5)),
                  SizedBox(
                    child: TextField(
                      controller: _addressController,
                      decoration: InputDecoration(
                        labelText: _textAddress,
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(_borderRadius),
                        ),
                      ),
                    ),
                  ),
                  const Padding(padding: EdgeInsets.symmetric(vertical: 10)),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      SizedBox(
                        child: ElevatedButton(
                          onPressed: _onCancel,
                          child: const Text('Cancel'),
                        ),
                      ),
                      const SizedBox(width: 10),
                      SizedBox(
                        child: ElevatedButton(
                          onPressed: () => _onConfirm(context),
                          child: const Text('Confirm'),
                        ),
                      ),
                    ],
                  ),
                  const Padding(padding: EdgeInsets.only(top: 15)),
                  Container(
                    decoration: BoxDecoration(
                      border: Border.all(color: Colors.blue),
                      borderRadius: BorderRadius.circular(10),
                    ),
                    padding: const EdgeInsets.all(10),
                    child: Column(
                      children: [
                        Center(
                          child: Text(
                            _textDados,
                            style: const TextStyle(fontSize: 20),
                          ),
                        ),
                        Align(
                          alignment: Alignment.centerLeft,
                          child: Row(children: [
                            Text("$_textName: ",
                            style: TextStyle(fontSize: _dataOutputSize),),
                            Text(
                              context.watch<FormStore>().user.name,
                              style: const TextStyle(fontWeight: FontWeight.bold),
                            )
                          ],)
                          // child: Text("$_textName: $_dadosName"),
                        ),
                        Align(
                          alignment: Alignment.centerLeft,
                          child: Row(children: [
                            Text("$_textEmail: ",
                            style: TextStyle(fontSize: _dataOutputSize),),
                            Text(
                              context.watch<FormStore>().user.email,
                              style: const TextStyle(fontWeight: FontWeight.bold)
                            )
                          ],)
                          
                        ),
                        Align(
                          alignment: Alignment.centerLeft,
                            child: Row(
                            children: [
                              Text("$_textAddress: ",
                              style: TextStyle(fontSize: _dataOutputSize),),
                              Text(
                              context.watch<FormStore>().user.address,
                              style: TextStyle(
                                fontWeight: FontWeight.bold,
                                fontSize: _dataOutputSize),
                              ),
                            ],
                            )
                          
                        ),
                      ],
                    ),
                  )
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}