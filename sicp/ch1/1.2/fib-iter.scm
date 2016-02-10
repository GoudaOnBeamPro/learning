;;; This program shows a way to compute Fibonaci numbers in an interative
;;; process. Just from looking at the code, the idea of it will not be as
;;; straightforward as it is with the tree recursion, but for this type of
;;; procedure, it is inherently better. The idea here is to use a pair of
;;; integers, a & b, initialized as Fib(1)=1 and Fib(0)=0, and to repeatedly
;;; apply the simultaneous transformations of 'a <-- a + b' and 'b <-- a'
;;; n number of times. This can be written as Fib(n + 1) and Fib(n), and
;;; be used to compute Fibonaci numbers in an interative process.
;;;
;;; TL;DR This good not bad. Tree recursive still good not bad.
;;;
;;; Thanks for reading all of my crap. Don't compile this, just throw it in
;;; an interpreter. I like CHICKEN.

(define (fib n)				; I tried to remake this in block
  (define (fib-iter a b n)		; structure... let's see how it works.
    (if (= n 0)				; Welp, I got it in block structure,
      b					; but I can't seem to figure out the
      (fib-iter (+ a b) a (- n 1))))	; lexical scoping since I need to n - 1.
  (fib-iter 1 0 n))			; Works great though!!
