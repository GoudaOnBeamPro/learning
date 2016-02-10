;;; This is an example of a program that computes the factorial of the 
;;; number n. As far as I know so far, this is a bad way to do it because
;;; the resulting computation will expand as the process builds up a chain
;;; of deferred opeations. The interpreter keeps track of the progress of
;;; the place in the computation with "hidden info" that grows in size
;;; as the process expands linerally.
;;;
;;; TL;DR This bad not good.
;;;
;;; Remember folks, this is to be run in an interpreter only, not compiled
;;; and run.


(define (factorial n)
  (if (= n 1)
    1
    (* n (factorial (- n 1)))))
