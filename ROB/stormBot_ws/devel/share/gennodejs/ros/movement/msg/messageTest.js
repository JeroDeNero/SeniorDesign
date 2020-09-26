// Auto-generated. Do not edit!

// (in-package movement.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class messageTest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.name = null;
      this.id = null;
      this.xLin = null;
      this.xAng = null;
      this.yAng = null;
    }
    else {
      if (initObj.hasOwnProperty('name')) {
        this.name = initObj.name
      }
      else {
        this.name = '';
      }
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = 0;
      }
      if (initObj.hasOwnProperty('xLin')) {
        this.xLin = initObj.xLin
      }
      else {
        this.xLin = 0.0;
      }
      if (initObj.hasOwnProperty('xAng')) {
        this.xAng = initObj.xAng
      }
      else {
        this.xAng = 0.0;
      }
      if (initObj.hasOwnProperty('yAng')) {
        this.yAng = initObj.yAng
      }
      else {
        this.yAng = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type messageTest
    // Serialize message field [name]
    bufferOffset = _serializer.string(obj.name, buffer, bufferOffset);
    // Serialize message field [id]
    bufferOffset = _serializer.int32(obj.id, buffer, bufferOffset);
    // Serialize message field [xLin]
    bufferOffset = _serializer.float32(obj.xLin, buffer, bufferOffset);
    // Serialize message field [xAng]
    bufferOffset = _serializer.float32(obj.xAng, buffer, bufferOffset);
    // Serialize message field [yAng]
    bufferOffset = _serializer.float32(obj.yAng, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type messageTest
    let len;
    let data = new messageTest(null);
    // Deserialize message field [name]
    data.name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [id]
    data.id = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [xLin]
    data.xLin = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [xAng]
    data.xAng = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [yAng]
    data.yAng = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.name.length;
    return length + 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'movement/messageTest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e15c1b00b8cc33d2ad11a9fcc899b06f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string name
    int32 id
    float32 xLin
    float32 xAng
    float32 yAng
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new messageTest(null);
    if (msg.name !== undefined) {
      resolved.name = msg.name;
    }
    else {
      resolved.name = ''
    }

    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = 0
    }

    if (msg.xLin !== undefined) {
      resolved.xLin = msg.xLin;
    }
    else {
      resolved.xLin = 0.0
    }

    if (msg.xAng !== undefined) {
      resolved.xAng = msg.xAng;
    }
    else {
      resolved.xAng = 0.0
    }

    if (msg.yAng !== undefined) {
      resolved.yAng = msg.yAng;
    }
    else {
      resolved.yAng = 0.0
    }

    return resolved;
    }
};

module.exports = messageTest;
