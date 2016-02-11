;;;                     This one is a bit of a doozy....		     ;;;
;;; First, let's observe that for n >= 3, the equation is:
;;; f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3). Because of their special relation,
;;; we can replace 1, 2, and 3 with a, b, and c, repectively, and get
;;; f(n) = a*f(n - a) + b*f(n - b) + c*f(n - c). If we plug in 3 for n, we could
;;; see that this would be the first iteration in a supposed process that would
;;; NOT have to be recursive any longer, since all of the proceeding a, b, and c
;;; values would be less than 3, which will just return the given value. Think
;;; on that one for a bit, and if it still doens't make since, there might be a
;;; hint or two below.
;;;
;;; TL;DR This is crazy, but it works!
;;;
;;; Remember kids, load this in an interpreter. Don't try this* at home!

(define (f n)
  (define (f-iter n a b c)
    (if (= n 3)
        (+ (* a 2)
	   (* b 1)
	   (* c 0))
        (f-iter (- n 1)		; This is where stuff gets crazy. How did we
	        (+ b a)		; come to these numbers? Try writing out the
	        (+ c (* 2 a))	; equation a few times, each using a value for
	        (* 3 a))))	; n that is one less than the last until n = 3.
  (if (< n 3)
    n
    (f-iter n 1 2 3)))		; * More precisely, don't try to compile this ;)
