;; Auto-generated. Do not edit!


(when (boundp 'movement::messageTest)
  (if (not (find-package "MOVEMENT"))
    (make-package "MOVEMENT"))
  (shadow 'messageTest (find-package "MOVEMENT")))
(unless (find-package "MOVEMENT::MESSAGETEST")
  (make-package "MOVEMENT::MESSAGETEST"))

(in-package "ROS")
;;//! \htmlinclude messageTest.msg.html


(defclass movement::messageTest
  :super ros::object
  :slots (_name _id _xLin _xAng _yAng ))

(defmethod movement::messageTest
  (:init
   (&key
    ((:name __name) "")
    ((:id __id) 0)
    ((:xLin __xLin) 0.0)
    ((:xAng __xAng) 0.0)
    ((:yAng __yAng) 0.0)
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _id (round __id))
   (setq _xLin (float __xLin))
   (setq _xAng (float __xAng))
   (setq _yAng (float __yAng))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:xLin
   (&optional __xLin)
   (if __xLin (setq _xLin __xLin)) _xLin)
  (:xAng
   (&optional __xAng)
   (if __xAng (setq _xAng __xAng)) _xAng)
  (:yAng
   (&optional __yAng)
   (if __yAng (setq _yAng __yAng)) _yAng)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; int32 _id
    4
    ;; float32 _xLin
    4
    ;; float32 _xAng
    4
    ;; float32 _yAng
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; int32 _id
       (write-long _id s)
     ;; float32 _xLin
       (sys::poke _xLin (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _xAng
       (sys::poke _xAng (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _yAng
       (sys::poke _yAng (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _xLin
     (setq _xLin (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _xAng
     (setq _xAng (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _yAng
     (setq _yAng (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get movement::messageTest :md5sum-) "e15c1b00b8cc33d2ad11a9fcc899b06f")
(setf (get movement::messageTest :datatype-) "movement/messageTest")
(setf (get movement::messageTest :definition-)
      "string name
int32 id
float32 xLin
float32 xAng
float32 yAng
")



(provide :movement/messageTest "e15c1b00b8cc33d2ad11a9fcc899b06f")


