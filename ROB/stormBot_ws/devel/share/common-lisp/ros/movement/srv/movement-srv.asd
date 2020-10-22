
(cl:in-package :asdf)

(defsystem "movement-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "serviceTest" :depends-on ("_package_serviceTest"))
    (:file "_package_serviceTest" :depends-on ("_package"))
  ))