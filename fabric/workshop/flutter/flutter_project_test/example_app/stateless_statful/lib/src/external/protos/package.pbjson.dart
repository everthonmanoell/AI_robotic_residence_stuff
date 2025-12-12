//
//  Generated code. Do not modify.
//  source: package.proto
//
// @dart = 2.12

// ignore_for_file: annotate_overrides, camel_case_types, comment_references
// ignore_for_file: constant_identifier_names, library_prefixes
// ignore_for_file: non_constant_identifier_names, prefer_final_fields
// ignore_for_file: unnecessary_import, unnecessary_this, unused_import

import 'dart:convert' as $convert;
import 'dart:core' as $core;
import 'dart:typed_data' as $typed_data;

@$core.Deprecated('Use userDescriptor instead')
const User$json = {
  '1': 'User',
  '2': [
    {'1': 'name', '3': 1, '4': 2, '5': 9, '10': 'name'},
    {'1': 'email', '3': 2, '4': 2, '5': 9, '10': 'email'},
    {'1': 'address', '3': 3, '4': 2, '5': 9, '10': 'address'},
  ],
};

/// Descriptor for `User`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List userDescriptor = $convert.base64Decode(
    'CgRVc2VyEhIKBG5hbWUYASACKAlSBG5hbWUSFAoFZW1haWwYAiACKAlSBWVtYWlsEhgKB2FkZH'
    'Jlc3MYAyACKAlSB2FkZHJlc3M=');

@$core.Deprecated('Use userListDescriptor instead')
const UserList$json = {
  '1': 'UserList',
  '2': [
    {'1': 'users', '3': 1, '4': 3, '5': 11, '6': '.User', '10': 'users'},
  ],
};

/// Descriptor for `UserList`. Decode as a `google.protobuf.DescriptorProto`.
final $typed_data.Uint8List userListDescriptor = $convert.base64Decode(
    'CghVc2VyTGlzdBIbCgV1c2VycxgBIAMoCzIFLlVzZXJSBXVzZXJz');

