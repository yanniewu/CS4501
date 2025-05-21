// Auto-generated. Do not edit!

// (in-package simple_control.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class toggle_geofenceRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.geofence_on = null;
    }
    else {
      if (initObj.hasOwnProperty('geofence_on')) {
        this.geofence_on = initObj.geofence_on
      }
      else {
        this.geofence_on = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type toggle_geofenceRequest
    // Serialize message field [geofence_on]
    bufferOffset = _serializer.bool(obj.geofence_on, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type toggle_geofenceRequest
    let len;
    let data = new toggle_geofenceRequest(null);
    // Deserialize message field [geofence_on]
    data.geofence_on = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'simple_control/toggle_geofenceRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '33283065de6845546e39497d7e980b9d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool geofence_on
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new toggle_geofenceRequest(null);
    if (msg.geofence_on !== undefined) {
      resolved.geofence_on = msg.geofence_on;
    }
    else {
      resolved.geofence_on = false
    }

    return resolved;
    }
};

class toggle_geofenceResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type toggle_geofenceResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type toggle_geofenceResponse
    let len;
    let data = new toggle_geofenceResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'simple_control/toggle_geofenceResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '358e233cde0c8a8bcfea4ce193f8fc15';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool success
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new toggle_geofenceResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    return resolved;
    }
};

module.exports = {
  Request: toggle_geofenceRequest,
  Response: toggle_geofenceResponse,
  md5sum() { return '08263b5cc812a6e30c6226c22efcab08'; },
  datatype() { return 'simple_control/toggle_geofence'; }
};
