import 'dart:convert';
import 'package:curveauth_dart/curveauth_dart.dart';

void main() {
  final keyPair = ECCKeyPair.generate();

  final jsonKey = jsonEncode(keyPair.toJson());
  final pubKey = keyPair.exportPublicKeyRawBase64();

  print(jsonEncode([jsonKey, pubKey]));
}
