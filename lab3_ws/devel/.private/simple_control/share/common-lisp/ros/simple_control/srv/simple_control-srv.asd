
(cl:in-package :asdf)

(defsystem "simple_control-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "toggle_geofence" :depends-on ("_package_toggle_geofence"))
    (:file "_package_toggle_geofence" :depends-on ("_package"))
  ))