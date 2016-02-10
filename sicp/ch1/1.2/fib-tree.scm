;;; This program demonstrates how a procedure to compute Fibonaci numbers
;;; can be written to be tree recursive. This is useful in showing a 
;;; prototypical tree recursion, but hardly anything else; there are a lot
;;; of redundant comuptations and the number of steps grows exponentionally
;;; with the number n. However, please note, dear readers, that tree recursions
;;; are not a bad thing. They are very useful when it comes to processes that
;;; operate on hierarchially structed data rather than numbers.
;;;
;;; TL;DR This bad not good. Tree recursion good not here.
;;;
;;; Finally, please don't compile and run this. It probably won't do you any
;;; good outside of an interpreter.

(define (fib n)
  (cond ((= n 0) 0)
	((= n 1) 1)
	(else (+ (fib (- n 1))		; the fib procedure calls itself twice
		 (fib (- n 2))))))	; when it doesn't make a leaf, therefore
					; a tree structure is created
