clearscreen.
set timer to 10.
until timer = 0 {
    print timer.
    set timer to timer - 1.
    wait 1.
    clearscreen.
}
print "ПОЕХАЛИ!".
wait 1.



stage.


until false {
    lock steering to heading(90, 90).
    lock throttle to 1.
    wait until stage:liquidfuel < 1.
    lock throttle to 0.
    wait 3.
    stage.
    wait 3.
}