; Auto-generated. Do not edit!


(cl:in-package simple_control-srv)


;//! \htmlinclude toggle_geofence-request.msg.html

(cl:defclass <toggle_geofence-request> (roslisp-msg-protocol:ros-message)
  ((geofence_on
    :reader geofence_on
    :initarg :geofence_on
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass toggle_geofence-request (<toggle_geofence-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <toggle_geofence-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'toggle_geofence-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name simple_control-srv:<toggle_geofence-request> is deprecated: use simple_control-srv:toggle_geofence-request instead.")))

(cl:ensure-generic-function 'geofence_on-val :lambda-list '(m))
(cl:defmethod geofence_on-val ((m <toggle_geofence-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simple_control-srv:geofence_on-val is deprecated.  Use simple_control-srv:geofence_on instead.")
  (geofence_on m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <toggle_geofence-request>) ostream)
  "Serializes a message object of type '<toggle_geofence-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'geofence_on) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <toggle_geofence-request>) istream)
  "Deserializes a message object of type '<toggle_geofence-request>"
    (cl:setf (cl:slot-value msg 'geofence_on) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<toggle_geofence-request>)))
  "Returns string type for a service object of type '<toggle_geofence-request>"
  "simple_control/toggle_geofenceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'toggle_geofence-request)))
  "Returns string type for a service object of type 'toggle_geofence-request"
  "simple_control/toggle_geofenceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<toggle_geofence-request>)))
  "Returns md5sum for a message object of type '<toggle_geofence-request>"
  "08263b5cc812a6e30c6226c22efcab08")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'toggle_geofence-request)))
  "Returns md5sum for a message object of type 'toggle_geofence-request"
  "08263b5cc812a6e30c6226c22efcab08")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<toggle_geofence-request>)))
  "Returns full string definition for message of type '<toggle_geofence-request>"
  (cl:format cl:nil "bool geofence_on~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'toggle_geofence-request)))
  "Returns full string definition for message of type 'toggle_geofence-request"
  (cl:format cl:nil "bool geofence_on~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <toggle_geofence-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <toggle_geofence-request>))
  "Converts a ROS message object to a list"
  (cl:list 'toggle_geofence-request
    (cl:cons ':geofence_on (geofence_on msg))
))
;//! \htmlinclude toggle_geofence-response.msg.html

(cl:defclass <toggle_geofence-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass toggle_geofence-response (<toggle_geofence-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <toggle_geofence-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'toggle_geofence-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name simple_control-srv:<toggle_geofence-response> is deprecated: use simple_control-srv:toggle_geofence-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <toggle_geofence-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader simple_control-srv:success-val is deprecated.  Use simple_control-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <toggle_geofence-response>) ostream)
  "Serializes a message object of type '<toggle_geofence-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <toggle_geofence-response>) istream)
  "Deserializes a message object of type '<toggle_geofence-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<toggle_geofence-response>)))
  "Returns string type for a service object of type '<toggle_geofence-response>"
  "simple_control/toggle_geofenceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'toggle_geofence-response)))
  "Returns string type for a service object of type 'toggle_geofence-response"
  "simple_control/toggle_geofenceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<toggle_geofence-response>)))
  "Returns md5sum for a message object of type '<toggle_geofence-response>"
  "08263b5cc812a6e30c6226c22efcab08")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'toggle_geofence-response)))
  "Returns md5sum for a message object of type 'toggle_geofence-response"
  "08263b5cc812a6e30c6226c22efcab08")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<toggle_geofence-response>)))
  "Returns full string definition for message of type '<toggle_geofence-response>"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'toggle_geofence-response)))
  "Returns full string definition for message of type 'toggle_geofence-response"
  (cl:format cl:nil "bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <toggle_geofence-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <toggle_geofence-response>))
  "Converts a ROS message object to a list"
  (cl:list 'toggle_geofence-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'toggle_geofence)))
  'toggle_geofence-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'toggle_geofence)))
  'toggle_geofence-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'toggle_geofence)))
  "Returns string type for a service object of type '<toggle_geofence>"
  "simple_control/toggle_geofence")