;; Auto-generated. Do not edit!


(when (boundp 'mindrove_package::MindRoveData)
  (if (not (find-package "MINDROVE_PACKAGE"))
    (make-package "MINDROVE_PACKAGE"))
  (shadow 'MindRoveData (find-package "MINDROVE_PACKAGE")))
(unless (find-package "MINDROVE_PACKAGE::MINDROVEDATA")
  (make-package "MINDROVE_PACKAGE::MINDROVEDATA"))

(in-package "ROS")
;;//! \htmlinclude MindRoveData.msg.html


(defclass mindrove_package::MindRoveData
  :super ros::object
  :slots (_data ))

(defmethod mindrove_package::MindRoveData
  (:init
   (&key
    ((:data __data) (make-array 14000 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _data __data)
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; float64[14000] _data
    (* 8    14000)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[14000] _data
     (dotimes (i 14000)
       (sys::poke (elt _data i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[14000] _data
   (dotimes (i (length _data))
     (setf (elt _data i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(setf (get mindrove_package::MindRoveData :md5sum-) "86daf2bf043daacec99b385ed93f47b1")
(setf (get mindrove_package::MindRoveData :datatype-) "mindrove_package/MindRoveData")
(setf (get mindrove_package::MindRoveData :definition-)
      "float64[14000] data

")



(provide :mindrove_package/MindRoveData "86daf2bf043daacec99b385ed93f47b1")


