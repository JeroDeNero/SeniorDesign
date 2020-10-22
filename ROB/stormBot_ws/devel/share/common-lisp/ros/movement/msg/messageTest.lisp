; Auto-generated. Do not edit!


(cl:in-package movement-msg)


;//! \htmlinclude messageTest.msg.html

(cl:defclass <messageTest> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0)
   (xLin
    :reader xLin
    :initarg :xLin
    :type cl:float
    :initform 0.0)
   (xAng
    :reader xAng
    :initarg :xAng
    :type cl:float
    :initform 0.0)
   (yAng
    :reader yAng
    :initarg :yAng
    :type cl:float
    :initform 0.0))
)

(cl:defclass messageTest (<messageTest>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <messageTest>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'messageTest)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name movement-msg:<messageTest> is deprecated: use movement-msg:messageTest instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <messageTest>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement-msg:name-val is deprecated.  Use movement-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <messageTest>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement-msg:id-val is deprecated.  Use movement-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'xLin-val :lambda-list '(m))
(cl:defmethod xLin-val ((m <messageTest>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement-msg:xLin-val is deprecated.  Use movement-msg:xLin instead.")
  (xLin m))

(cl:ensure-generic-function 'xAng-val :lambda-list '(m))
(cl:defmethod xAng-val ((m <messageTest>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement-msg:xAng-val is deprecated.  Use movement-msg:xAng instead.")
  (xAng m))

(cl:ensure-generic-function 'yAng-val :lambda-list '(m))
(cl:defmethod yAng-val ((m <messageTest>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader movement-msg:yAng-val is deprecated.  Use movement-msg:yAng instead.")
  (yAng m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <messageTest>) ostream)
  "Serializes a message object of type '<messageTest>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let* ((signed (cl:slot-value msg 'id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'xLin))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'xAng))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'yAng))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <messageTest>) istream)
  "Deserializes a message object of type '<messageTest>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'xLin) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'xAng) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yAng) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<messageTest>)))
  "Returns string type for a message object of type '<messageTest>"
  "movement/messageTest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'messageTest)))
  "Returns string type for a message object of type 'messageTest"
  "movement/messageTest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<messageTest>)))
  "Returns md5sum for a message object of type '<messageTest>"
  "e15c1b00b8cc33d2ad11a9fcc899b06f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'messageTest)))
  "Returns md5sum for a message object of type 'messageTest"
  "e15c1b00b8cc33d2ad11a9fcc899b06f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<messageTest>)))
  "Returns full string definition for message of type '<messageTest>"
  (cl:format cl:nil "string name~%int32 id~%float32 xLin~%float32 xAng~%float32 yAng~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'messageTest)))
  "Returns full string definition for message of type 'messageTest"
  (cl:format cl:nil "string name~%int32 id~%float32 xLin~%float32 xAng~%float32 yAng~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <messageTest>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <messageTest>))
  "Converts a ROS message object to a list"
  (cl:list 'messageTest
    (cl:cons ':name (name msg))
    (cl:cons ':id (id msg))
    (cl:cons ':xLin (xLin msg))
    (cl:cons ':xAng (xAng msg))
    (cl:cons ':yAng (yAng msg))
))
