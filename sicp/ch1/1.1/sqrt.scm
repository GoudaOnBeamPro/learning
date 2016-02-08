;;; This is from the end of 1.1, where we take about block structure
;;; and lexical scoping and apply it to out sqrt program.

(define (sqrt x)
  (define (good-enough? guess)
    (< (abs (/ (- (improve guess) guess)
	       guess))
       0.001))
  (define (improve guess) ;;; This is something I saw online. Works great!
    (/ (+ (/ x guess) guess)
       2))
  (define (sqrt-iter guess)
    (if (good-enough? guess)
      guess
      (sqrt-iter (improve guess))))
  (sqrt-iter 1.0))

(define (abs x)
  (if (< x 0)
    (- x)
    x))
