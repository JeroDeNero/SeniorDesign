;; Auto-generated. Do not edit!


(when (boundp 'movement::serviceTest)
  (if (not (find-package "MOVEMENT"))
    (make-package "MOVEMENT"))
  (shadow 'serviceTest (find-package "MOVEMENT")))
(unless (find-package "MOVEMENT::SERVICETEST")
  (make-package "MOVEMENT::SERVICETEST"))
(unless (find-package "MOVEMENT::SERVICETESTREQUEST")
  (make-package "MOVEMENT::SERVICETESTREQUEST"))
(unless (find-package "MOVEMENT::SERVICETESTRESPONSE")
  (make-package "MOVEMENT::SERVICETESTRESPONSE"))

(in-package "ROS")





(defclass movement::serviceTestRequest
  :super ros::object
  :slots (_a _b ))

(defmethod movement::serviceTestRequest
  (:init
   (&key
    ((:a __a) 0.0)
    ((:b __b) 0.0)
    )
   (send-super :init)
   (setq _a (float __a))
   (setq _b (float __b))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:serialization-length
   ()
   (+
    ;; float32 _a
    4
    ;; float32 _b
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _a
       (sys::poke _a (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _b
       (sys::poke _b (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _a
     (setq _a (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _b
     (setq _b (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass movement::serviceTestResponse
  :super ros::object
  :slots (_sum ))

(defmethod movement::serviceTestResponse
  (:init
   (&key
    ((:sum __sum) 0.0)
    )
   (send-super :init)
   (setq _sum (float __sum))
   self)
  (:sum
   (&optional __sum)
   (if __sum (setq _sum __sum)) _sum)
  (:serialization-length
   ()
   (+
    ;; float32 _sum
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _sum
       (sys::poke _sum (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _sum
     (setq _sum (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass movement::serviceTest
  :super ros::object
  :slots ())

(setf (get movement::serviceTest :md5sum-) "210a18f816d5b88becb133b82fae0c4c")
(setf (get movement::serviceTest :datatype-) "movement/serviceTest")
(setf (get movement::serviceTest :request) movement::serviceTestRequest)
(setf (get movement::serviceTest :response) movement::serviceTestResponse)

(defmethod movement::serviceTestRequest
  (:response () (instance movement::serviceTestResponse :init)))

(setf (get movement::serviceTestRequest :md5sum-) "210a18f816d5b88becb133b82fae0c4c")
(setf (get movement::serviceTestRequest :datatype-) "movement/serviceTestRequest")
(setf (get movement::serviceTestRequest :definition-)
      "float32 a
float32 b
---
float32 sum
")

(setf (get movement::serviceTestResponse :md5sum-) "210a18f816d5b88becb133b82fae0c4c")
(setf (get movement::serviceTestResponse :datatype-) "movement/serviceTestResponse")
(setf (get movement::serviceTestResponse :definition-)
      "float32 a
float32 b
---
float32 sum
")



(provide :movement/serviceTest "210a18f816d5b88becb133b82fae0c4c")


