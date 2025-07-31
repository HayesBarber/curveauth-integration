import 'dart:convert';
import 'package:curveauth_dart/curveauth_dart.dart';

void main(List<String> args) async {
  final json = args[0];
  final challenge = args[1];

  final keyPair = ECCKeyPair.fromJson(jsonDecode(json));

  final signature = await keyPair.createSignature(challenge);

  print(signature);
}
