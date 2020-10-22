; Auto-generated. Do not edit!


(cl:in-package movement-srv)


;//! \htmlinclude serviceTest-request.msg.html

(cl:defclass <serviceTest-request> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type cl:float
    :initform 0.0)
   (b
    :reader b
    :initarg :b
    :type cl:float
    :initform 0.0))
)

(cl:defclass serviceTest-request (<serviceTest-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <serviceTest-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'serviceTest-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement-srv:<serviceTest-request> is deprecated: use movement-srv:serviceTest-request instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <serviceTest-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement-srv:a-val is deprecated.  Use movement-srv:a instead.")
  (a m))

(cl:ensure-generic-function 'b-val :lambda-list '(m))
(cl:defmethod b-val ((m <serviceTest-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement-srv:b-val is deprecated.  Use movement-srv:b instead.")
  (b m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <serviceTest-request>) ostream)
  "Serializes a message object of type '<serviceTest-request>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'a))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'b))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <serviceTest-request>) istream)
  "Deserializes a message object of type '<serviceTest-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'a) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'b) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<serviceTest-request>)))
  "Returns string type for a service object of type '<serviceTest-request>"
  "movement/serviceTestRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'serviceTest-request)))
  "Returns string type for a service object of type 'serviceTest-request"
  "movement/serviceTestRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<serviceTest-request>)))
  "Returns md5sum for a message object of type '<serviceTest-request>"
  "210a18f816d5b88becb133b82fae0c4c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'serviceTest-request)))
  "Returns md5sum for a message object of type 'serviceTest-request"
  "210a18f816d5b88becb133b82fae0c4c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<serviceTest-request>)))
  "Returns full string definition for message of type '<serviceTest-request>"
  (cl:format cl:nil "float32 a~%float32 b~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'serviceTest-request)))
  "Returns full string definition for message of type 'serviceTest-request"
  (cl:format cl:nil "float32 a~%float32 b~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <serviceTest-request>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <serviceTest-request>))
  "Converts a ROS message object to a list"
  (cl:list 'serviceTest-request
    (cl:cons ':a (a msg))
    (cl:cons ':b (b msg))
))
;//! \htmlinclude serviceTest-response.msg.html

(cl:defclass <serviceTest-response> (roslisp-msg-protocol:ros-message)
  ((sum
    :reader sum
    :initarg :sum
    :type cl:float
    :initform 0.0))
)

(cl:defclass serviceTest-response (<serviceTest-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <serviceTest-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'serviceTest-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement-srv:<serviceTest-response> is deprecated: use movement-srv:serviceTest-response instead.")))

(cl:ensure-generic-function 'sum-val :lambda-list '(m))
(cl:defmethod sum-val ((m <serviceTest-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement-srv:sum-val is deprecated.  Use movement-srv:sum instead.")
  (sum m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <serviceTest-response>) ostream)
  "Serializes a message object of type '<serviceTest-response>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'sum))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <serviceTest-response>) istream)
  "Deserializes a message object of type '<serviceTest-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'sum) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<serviceTest-response>)))
  "Returns string type for a service object of type '<serviceTest-response>"
  "movement/serviceTestResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'serviceTest-response)))
  "Returns string type for a service object of type 'serviceTest-response"
  "movement/serviceTestResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<serviceTest-response>)))
  "Returns md5sum for a message object of type '<serviceTest-response>"
  "210a18f816d5b88becb133b82fae0c4c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'serviceTest-response)))
  "Returns md5sum for a message object of type 'serviceTest-response"
  "210a18f816d5b88becb133b82fae0c4c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<serviceTest-response>)))
  "Returns full string definition for message of type '<serviceTest-response>"
  (cl:format cl:nil "float32 sum~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'serviceTest-response)))
  "Returns full string definition for message of type 'serviceTest-response"
  (cl:format cl:nil "float32 sum~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <serviceTest-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <serviceTest-response>))
  "Converts a ROS message object to a list"
  (cl:list 'serviceTest-response
    (cl:cons ':sum (sum msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'serviceTest)))
  'serviceTest-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'serviceTest)))
  'serviceTest-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'serviceTest)))
  "Returns string type for a service object of type '<serviceTest>"
  "movement/serviceTest")