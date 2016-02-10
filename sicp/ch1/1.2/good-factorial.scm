;;; This is the better way to do a computation of the factorial of
;;; the number n. It uses three "state variables" that maintain a running 
;;; product as well as a counter that counts from 1 to n. This program is 
;;; an example of a linear iterative process. In contrast to the other method,
;;; this program does NOT expand in size as it computes, since there are not
;;; any deffered operations. The state variables provide a complte description
;;; of the state of the process at any given point. If the computation were to
;;; be interrupted, it could be resumed by supplying the interpreter with the
;;; three variables. Thanks to tail recursion, iterative processes like this 
;;; one will never take up extra memory.
;;;
;;; TL;DR This good not bad.
;;; 
;;; Remember that this is for an interpreter only. Do not try to compile
;;; and run this code. You will be disappointed.

(define (factorial n)			; this multiplies 1 by 2, then that
  (define (fact-iter product counter)	; result by 3, then result by 4,
    (if (> counter n) 			; and so on, until we reach n
      product
      (fact-iter (* counter product)
		 (+ counter 1))))
  (fact-iter 1 1))			; reproduced in block structure by moi
