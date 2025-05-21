;; Auto-generated. Do not edit!


(when (boundp 'simple_control::toggle_geofence)
  (if (not (find-package "SIMPLE_CONTROL"))
    (make-package "SIMPLE_CONTROL"))
  (shadow 'toggle_geofence (find-package "SIMPLE_CONTROL")))
(unless (find-package "SIMPLE_CONTROL::TOGGLE_GEOFENCE")
  (make-package "SIMPLE_CONTROL::TOGGLE_GEOFENCE"))
(unless (find-package "SIMPLE_CONTROL::TOGGLE_GEOFENCEREQUEST")
  (make-package "SIMPLE_CONTROL::TOGGLE_GEOFENCEREQUEST"))
(unless (find-package "SIMPLE_CONTROL::TOGGLE_GEOFENCERESPONSE")
  (make-package "SIMPLE_CONTROL::TOGGLE_GEOFENCERESPONSE"))

(in-package "ROS")





(defclass simple_control::toggle_geofenceRequest
  :super ros::object
  :slots (_geofence_on ))

(defmethod simple_control::toggle_geofenceRequest
  (:init
   (&key
    ((:geofence_on __geofence_on) nil)
    )
   (send-super :init)
   (setq _geofence_on __geofence_on)
   self)
  (:geofence_on
   (&optional __geofence_on)
   (if __geofence_on (setq _geofence_on __geofence_on)) _geofence_on)
  (:serialization-length
   ()
   (+
    ;; bool _geofence_on
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _geofence_on
       (if _geofence_on (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _geofence_on
     (setq _geofence_on (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass simple_control::toggle_geofenceResponse
  :super ros::object
  :slots (_success ))

(defmethod simple_control::toggle_geofenceResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass simple_control::toggle_geofence
  :super ros::object
  :slots ())

(setf (get simple_control::toggle_geofence :md5sum-) "08263b5cc812a6e30c6226c22efcab08")
(setf (get simple_control::toggle_geofence :datatype-) "simple_control/toggle_geofence")
(setf (get simple_control::toggle_geofence :request) simple_control::toggle_geofenceRequest)
(setf (get simple_control::toggle_geofence :response) simple_control::toggle_geofenceResponse)

(defmethod simple_control::toggle_geofenceRequest
  (:response () (instance simple_control::toggle_geofenceResponse :init)))

(setf (get simple_control::toggle_geofenceRequest :md5sum-) "08263b5cc812a6e30c6226c22efcab08")
(setf (get simple_control::toggle_geofenceRequest :datatype-) "simple_control/toggle_geofenceRequest")
(setf (get simple_control::toggle_geofenceRequest :definition-)
      "bool geofence_on
---
bool success

")

(setf (get simple_control::toggle_geofenceResponse :md5sum-) "08263b5cc812a6e30c6226c22efcab08")
(setf (get simple_control::toggle_geofenceResponse :datatype-) "simple_control/toggle_geofenceResponse")
(setf (get simple_control::toggle_geofenceResponse :definition-)
      "bool geofence_on
---
bool success

")



(provide :simple_control/toggle_geofence "08263b5cc812a6e30c6226c22efcab08")


