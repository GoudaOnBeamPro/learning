;;; This is the program we were asked to create ourselves based off of the 
;;; sqrt program. It uses Newton's formula for approximating the cube-root.
;;; I was pretty darn proud of this.
;;;
;;; This is meant to be loaded in an interpreter. Do not try to compile and run!


(define (cbrt x)
  (define (good-enough? guess)
    (< (abs (/ (- (imrpove guess) guess)
	       guess))
       0.001))
  (define (improve guess)
    (/ (+ (/ x (square guess))
	  (* 2 guess))
       3))
  (define (cbrt-iter guess)
    (if (good-enough? guess)
      guess
      (cbrt-iter (improve guess))))
  (cbrt-iter 1.0))

(define (square x) (* x x))

(define (abs x)
  (if (< x 0)
    (- x)
    x))
