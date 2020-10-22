
(cl:in-package :asdf)

(defsystem "movement-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "messageTest" :depends-on ("_package_messageTest"))
    (:file "_package_messageTest" :depends-on ("_package"))
  ))