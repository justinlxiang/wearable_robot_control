
(cl:in-package :asdf)

(defsystem "mindrove_package-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MindRoveData" :depends-on ("_package_MindRoveData"))
    (:file "_package_MindRoveData" :depends-on ("_package"))
  ))