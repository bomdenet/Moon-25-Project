function WaitBeforeStart {
    clearscreen.
    set timer to 3.
    until timer = 0 {
        print timer.
        set timer to timer - 1.
        wait 1.
        clearscreen.
    }
    print "ПОЕХАЛИ!".
    wait 1.
}

function FirstStage {
    clearscreen.

    print "Набираем высоту до 30км и наклон ракеты".
    lock steering to heading(90, 90).
    lock throttle to 1.
    stage.

    until ship:altitude > 30000 {
        lock steering to heading(90, 90 - 50 * (ship:altitude / 30000)).
    }
    lock steering to heading(90, 20).

    wait until stage:liquidfuel < 1.
    print "У первой ступени закончилось топливо, начинаю отстыковку".
    lock throttle to 0.
    wait 3.
    stage.
    wait 15.
}

function SecondStage {
    clearscreen.

    print "Произвожу запуск второй ступени".
    lock throttle to 1.

    wait until ship:altitude > 70000.
    print "Вышли за пределы орбиты Земли. Произвожу сброс обтекателей".
    stage.

    wait until ship:apoapsis > 200000.
}

function CircleOrbit {
    clearscreen.

    print "Выходим на апоцентр в 200км".
    lock throttle to 0.
    wait 3.
    stage.
    lock steering to heading(90, 0).
    wait until eta:apoapsis < 10.
    lock throttle to 1.

    wait until ship:apoapsis > 205000.
    lock throttle to 0.

    set b to 1.
    until b = 0 {
        if ship:apoapsis > 205000 {
            lock steering to heading(90, -5).
            lock throttle to 1.
        }
        else if ship:apoapsis < 200000 {
            lock steering to heading(90, 5).
            lock throttle to 1.
        }
        else {
            lock steering to heading(90, 0).
            lock throttle to 0.
        }
        wait 1.
    }

    wait ship:altitude > 7000000.
}

WaitBeforeStart.
FirstStage.
SecondStage.
CircleOrbit.