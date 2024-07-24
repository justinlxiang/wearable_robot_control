; Auto-generated. Do not edit!


(cl:in-package mindrove_package-msg)


;//! \htmlinclude MindRoveData.msg.html

(cl:defclass <MindRoveData> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type (cl:vector cl:float)
   :initform (cl:make-array 14000 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass MindRoveData (<MindRoveData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MindRoveData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MindRoveData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mindrove_package-msg:<MindRoveData> is deprecated: use mindrove_package-msg:MindRoveData instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <MindRoveData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mindrove_package-msg:data-val is deprecated.  Use mindrove_package-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MindRoveData>) ostream)
  "Serializes a message object of type '<MindRoveData>"
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MindRoveData>) istream)
  "Deserializes a message object of type '<MindRoveData>"
  (cl:setf (cl:slot-value msg 'data) (cl:make-array 14000))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i 14000)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MindRoveData>)))
  "Returns string type for a message object of type '<MindRoveData>"
  "mindrove_package/MindRoveData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MindRoveData)))
  "Returns string type for a message object of type 'MindRoveData"
  "mindrove_package/MindRoveData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MindRoveData>)))
  "Returns md5sum for a message object of type '<MindRoveData>"
  "86daf2bf043daacec99b385ed93f47b1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MindRoveData)))
  "Returns md5sum for a message object of type 'MindRoveData"
  "86daf2bf043daacec99b385ed93f47b1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MindRoveData>)))
  "Returns full string definition for message of type '<MindRoveData>"
  (cl:format cl:nil "float64[14000] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MindRoveData)))
  "Returns full string definition for message of type 'MindRoveData"
  (cl:format cl:nil "float64[14000] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MindRoveData>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MindRoveData>))
  "Converts a ROS message object to a list"
  (cl:list 'MindRoveData
    (cl:cons ':data (data msg))
))
