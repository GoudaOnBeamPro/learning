;;; This one is a bit of a doozy...
;;; First, let's observe that for n >= 3, the equation is:
;;; f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3). This can be rewritten as
;;; f(n) = (a * f(n - a)) + (b * f(n - b)) + (c * f(n - c)) where a = 1, b = 2,
;;; c = 3, and n >= 3. Let's see what that looks like with just n plugged in.
;;; f(3) = a*f(3 - a) + b*f(3 - b) + c*f(3 - c). The community on schemewiki.org
;;; has a great suggestion of calculating this by manipulating the coefficients
;;; and decreasing n by one until n = 3, then applying what we know 3 plugged in
;;; which is f(3) = 1*f(2) + 2*f(1) + 3f(0), and since n < 3 in those cases, 
;;; it will look like this f(3) = 1*2 + 2*1 + 3*0. What's important to notice
;;; here is that, after we've manipulated the coefficients, they can replace 
;;; the 1, 2, and 3 respectively in the last written equation, which will give 
;;; us our answer. Ain't that fancy?
;;;
;;; TL;DR This is crazy, but it works!
;;;
;;; Remember kids, load this in an interpreter. Don't try (to compile) at home!

(define (f n)
  (define (f-iter n a b c)
    (if (= n 3)
      (+ (* a 2)
	 (* b 1)
	 (* c 0))
      (f-iter (- n 1)
	      (+ b a)
	      (+ c (* 2 a))
	      (* 3 a))))
  (if (< n 3)
    n
    (f-iter n 1 2 3)))
