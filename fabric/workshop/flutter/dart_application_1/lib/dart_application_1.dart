int calculate() {
  return 6 * 7;
}

int sumAB(int a, int b){
  return a + b;
}

int subAb(int a, int b){
  return a - b;
}

int multAb(int a, int b){
  return a * b;
}

Future<double> divAb(int a, int b) async{
 
  if (b == 0){
    return 0.0;
  }
  return a / b;

    
}
