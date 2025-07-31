import 'package:curveauth_dart/curveauth_dart.dart';

void main() {
  final keyPair = ECCKeyPair.generate();

  print(keyPair.toJson());
}
