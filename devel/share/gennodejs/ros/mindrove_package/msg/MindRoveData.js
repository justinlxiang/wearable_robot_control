// Auto-generated. Do not edit!

// (in-package mindrove_package.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class MindRoveData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.data = null;
    }
    else {
      if (initObj.hasOwnProperty('data')) {
        this.data = initObj.data
      }
      else {
        this.data = new Array(14000).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MindRoveData
    // Check that the constant length array field [data] has the right length
    if (obj.data.length !== 14000) {
      throw new Error('Unable to serialize array field data - length must be 14000')
    }
    // Serialize message field [data]
    bufferOffset = _arraySerializer.float64(obj.data, buffer, bufferOffset, 14000);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MindRoveData
    let len;
    let data = new MindRoveData(null);
    // Deserialize message field [data]
    data.data = _arrayDeserializer.float64(buffer, bufferOffset, 14000)
    return data;
  }

  static getMessageSize(object) {
    return 112000;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mindrove_package/MindRoveData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '86daf2bf043daacec99b385ed93f47b1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[14000] data
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MindRoveData(null);
    if (msg.data !== undefined) {
      resolved.data = msg.data;
    }
    else {
      resolved.data = new Array(14000).fill(0)
    }

    return resolved;
    }
};

module.exports = MindRoveData;
