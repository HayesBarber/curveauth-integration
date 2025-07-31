import 'dart:convert';
import 'dart:io';
import 'package:curveauth_dart/curveauth_dart.dart';

void main(List<String> args) async {
  if (args.length != 2) {
    print('Usage: dart sign_challenge.dart <keypair_json> <challenge>');
    exit(1);
  }

  final jsonStr = args[0];
  final challenge = args[1];

  late final ECCKeyPair keyPair;
  try {
    keyPair = ECCKeyPair.fromJson(jsonDecode(jsonStr));
  } catch (e) {
    print('Invalid keypair JSON: $e');
    exit(1);
  }

  final signature = await keyPair.createSignature(challenge);
  print(signature);
}
